import { readFileSync } from 'node:fs';

/**
 * Give every block of prose its own "suggest an edit" link.
 *
 * The link opens a prefilled GitHub issue naming the section the block sits in,
 * which paragraph of that section it is, and the text as it currently reads. A
 * reader who spots a wrong term does not have to find the page, the section or
 * the wording again — the issue already carries all three, so the only thing
 * left to write is the correction itself.
 *
 * A section is the address, not a line number: the heading is what both the
 * reader and the editor already navigate by, it survives every edit above it,
 * and it anchors a URL on the site and on GitHub alike. A line number is none
 * of those things — it moves with the paragraph above it and points at nothing
 * a person recognizes. The line still goes in as a hint, last and labelled as
 * "at the time of writing", because it saves a scroll when it is still right
 * and costs nothing when it is not.
 *
 * This runs at build time rather than in the browser: the href is a plain
 * anchor in the HTML, so it works with JavaScript off, and the positions and
 * headings only exist during the build.
 */

/**
 * How many lines to add to a position remark reports.
 *
 * Remark never sees the frontmatter or the blank lines after it, so it counts
 * from the first line of real prose. Finding that line in the file gives the
 * shift back to file lines, which is what a link to GitHub needs.
 */
const lineShift = new Map();
function offsetOf(filePath) {
  if (!lineShift.has(filePath)) {
    const lines = readFileSync(filePath, 'utf8').split('\n');
    let start = 0;
    if (lines[0].trim() === '---') {
      const end = lines.indexOf('---', 1);
      start = end === -1 ? 0 : end + 1;
    }
    while (start < lines.length && lines[start].trim() === '') start += 1;
    lineShift.set(filePath, start);
  }
  return lineShift.get(filePath);
}

const REPO = 'https://github.com/quran-ws/guidelines';
const TEMPLATE = 'edit.yml';

/** Blocks worth quoting on their own. Headings carry too little to correct. */
const BLOCKS = new Set(['p', 'blockquote', 'ul', 'ol', 'table', 'pre']);

/** GitHub truncates long URLs; a quote past this adds nothing to the issue. */
const QUOTE_LIMIT = 600;

function text(node) {
  if (node.type === 'text') return node.value;
  if (!node.children) return '';
  const spaced = node.tagName === 'li' || node.tagName === 'td' || node.tagName === 'th';
  return node.children.map(text).join('') + (spaced ? '\n' : '');
}

const SITE = 'https://quran-ws.github.io/guidelines';

/** Headings open a section; everything under one belongs to it. */
const HEADINGS = new Set(['h2', 'h3', 'h4', 'h5', 'h6']);

/** `content/ar/03-terminology/standard.md` → `/ar/03-terminology/standard/` */
function pageUrl(source) {
  const path = source.replace(/^content\//, '').replace(/\.mdx?$/, '').replace(/\/?index$/, '');
  return `${SITE}/${path}/`.replace(/\/{2,}$/, '/');
}

/** `/…/content/ar/03-terminology/standard.md` → `content/ar/03-terminology/standard.md` */
function repoPath(filePath) {
  const at = filePath.replace(/\\/g, '/').lastIndexOf('/content/');
  return at === -1 ? null : filePath.slice(at + 1);
}

export function rehypeSuggestEdit() {
  return (tree, file) => {
    const source = repoPath(file.path ?? '');
    if (!source) return;
    const offset = offsetOf(file.path);

    const children = [];
    // The heading chain above the current block, e.g. an h3 under an h2, and
    // how many blocks have been seen since the last heading — enough to say
    // "the second paragraph under X" without asking anyone to count lines.
    let section = [];
    let anchor = '';
    let nth = 0;
    // A generated page names the file its section came from in a comment
    // (`<!-- source: standards/… -->`) right under the heading. An edit to
    // such a section belongs in that file, not in the page, so the link
    // points there. The comment holds until the next heading.
    let generatedFrom = '';

    for (const node of tree.children) {
      if (node.type === 'element' && HEADINGS.has(node.tagName)) {
        const depth = Number(node.tagName[1]);
        section = section.slice(0, depth - 2).concat(text(node).trim());
        anchor = typeof node.properties?.id === 'string' ? node.properties.id : '';
        nth = 0;
        generatedFrom = '';
        children.push(node);
        continue;
      }

      // Astro passes markdown's HTML through as `raw`, so the comment arrives
      // as its source text rather than as a `comment` node.
      if (node.type === 'raw' || node.type === 'comment') {
        const from = String(node.value ?? '').match(/(?:<!--)?\s*source:\s*(\S+)\s*(?:-->)?/)?.[1];
        if (from) generatedFrom = from;
        children.push(node);
        continue;
      }

      if (node.type !== 'element' || !BLOCKS.has(node.tagName) || !node.position) {
        children.push(node);
        continue;
      }

      const quote = text(node).replace(/\s+\n/g, '\n').trim();
      if (!quote) {
        children.push(node);
        continue;
      }

      nth += 1;
      const line = node.position.start.line + offset;
      const where = section.length ? section.join(' › ') : 'صدر الصفحة — page opening';
      // URLSearchParams encodes the whole value once; encoding the anchor
      // here as well would leave it unreadable in the issue.
      const url = anchor ? `${pageUrl(source)}#${anchor}` : pageUrl(source);
      const location = [
        `${where} — block ${nth}`,
        url,
        `${source}${anchor ? `#${anchor}` : ''}`,
        generatedFrom
          ? `${REPO}/blob/main/${generatedFrom} (the page is generated from this file; edit it there)`
          : `${REPO}/blob/main/${source}#L${line} (line at the time of writing)`,
      ].join('\n');

      const params = new URLSearchParams({
        template: TEMPLATE,
        title: `edit: ${where} — ${source.replace(/^content\//, '').replace(/\.mdx?$/, '')}`,
        location,
        quote: quote.length > QUOTE_LIMIT ? `${quote.slice(0, QUOTE_LIMIT)}…` : quote,
      });

      children.push({
        type: 'element',
        tagName: 'div',
        properties: { className: ['qw-block'] },
        children: [
          node,
          {
            type: 'element',
            tagName: 'a',
            properties: {
              className: ['qw-suggest'],
              href: `${REPO}/issues/new?${params}`,
              target: '_blank',
              rel: ['noopener'],
              title: 'اقترح تعديلًا على هذه الفقرة — Suggest an edit',
              'aria-label': 'Suggest an edit to this paragraph',
            },
            children: [{ type: 'text', value: '✎' }],
          },
        ],
      });
    }
    tree.children = children;
  };
}
