import { existsSync, readdirSync, readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { rehypeHeadingIds } from '@astrojs/markdown-remark';
import { rehypeSuggestEdit } from './src/plugins/suggest-edit.mjs';

const BASE = '/guidelines';
const contentDir = fileURLToPath(new URL('../content/', import.meta.url));

/** Read `sidebar.order` out of a page's frontmatter; unordered pages sort last. */
function sidebarOrder(path) {
  const source = readFileSync(path, 'utf8');
  const block = source.startsWith('---') ? source.slice(3, source.indexOf('\n---', 3)) : '';
  const order = Number(block.match(/^sidebar:\s*\n(?:\s+.*\n)*?\s+order:\s*(-?\d+)/m)?.[1]);
  return Number.isFinite(order) ? order : Number.MAX_SAFE_INTEGER;
}

/**
 * Build one sidebar group from a content directory.
 *
 * Starlight's `autogenerate` cannot see this collection: it derives each page's
 * path by stripping `src/content/docs/` from the entry's filePath, and our pages
 * live in ../content so that they stay readable on GitHub. Nothing ever matched,
 * and every group rendered empty. Listing the directory ourselves keeps the
 * "add a file and it appears" behaviour that `autogenerate` was there for.
 *
 * Arabic is the authoring source, so it defines the structure. A page that also
 * exists in English becomes a `slug` entry, which Starlight resolves per locale
 * and labels from that locale's own frontmatter.
 *
 * A page with no English counterpart is left out. One sidebar is shared by both
 * locales, and neither way of expressing such an entry works: a `slug` throws
 * during the English build, and a `link` has the current locale injected into
 * it, pointing English readers at a page that does not exist. Give the page an
 * English counterpart and it is picked up automatically.
 */
function sectionItems(dir) {
  const arDir = `${contentDir}ar/${dir}`;
  return readdirSync(arDir)
    .filter((name) => name.endsWith('.md') || name.endsWith('.mdx'))
    .map((name) => {
      const stem = name.replace(/\.mdx?$/, '');
      return { stem, order: sidebarOrder(`${arDir}/${name}`) };
    })
    .sort((a, b) => a.order - b.order || a.stem.localeCompare(b.stem))
    .filter(
      ({ stem }) =>
        existsSync(`${contentDir}en/${dir}/${stem}.md`) ||
        existsSync(`${contentDir}en/${dir}/${stem}.mdx`)
    )
    .map(({ stem }) => ({ slug: stem === 'index' ? dir : `${dir}/${stem}` }));
}

export default defineConfig({
  // Every block of prose gets a link that opens a prefilled issue naming the
  // section it sits in. See src/plugins/suggest-edit.mjs. Astro adds heading
  // ids after user plugins, so it is named here to run before ours — the link
  // needs the anchor the heading will carry.
  markdown: { rehypePlugins: [rehypeHeadingIds, rehypeSuggestEdit] },
  site: 'https://quran-ws.github.io',
  base: BASE,
  // Neither language is the root: /ar/ and /en/ mirror each other, as the
  // content directories do. The bare base redirects to the default locale.
  redirects: {
    '/': `${BASE}/ar/`,
  },
  integrations: [
    starlight({
      title: 'Quran.ws Guidelines',
      description: 'Internal guidelines and open standards for the Quran.ws infrastructure.',
      defaultLocale: 'ar',
      locales: {
        // Arabic is the authoring source for text-adab and terminology.
        ar: { label: 'العربية', lang: 'ar', dir: 'rtl' },
        en: { label: 'English', lang: 'en' },
      },
      social: {
        github: 'https://github.com/quran-ws/guidelines',
      },
      sidebar: [
        { label: 'المدخل', translations: { en: 'Introduction' }, items: sectionItems('01-intro') },
        { label: 'النص القرآني', translations: { en: 'Quranic text' }, items: sectionItems('02-quranic-text') },
        { label: 'المصطلحات', translations: { en: 'Terminology' }, items: sectionItems('03-terminology') },
        { label: 'الإصدارات', translations: { en: 'Versioning' }, items: sectionItems('04-versioning') },
        { label: 'المصدر المفتوح', translations: { en: 'Open source' }, items: sectionItems('05-open-source') },
        { label: 'الهندسة', translations: { en: 'Engineering' }, items: sectionItems('06-engineering') },
      ],
      head: [
        { tag: 'link', attrs: { rel: 'preconnect', href: 'https://fonts.googleapis.com' } },
        { tag: 'link', attrs: { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: true } },
        {
          tag: 'link',
          attrs: {
            rel: 'stylesheet',
            // Rubik for everything it covers; Noto Naskh Arabic only catches the
            // Quranic marks Rubik has no glyphs for; IBM Plex Mono for anything
            // that is data rather than prose. See custom.css.
            href: 'https://fonts.googleapis.com/css2?family=Rubik:ital,wght@0,300..900;1,300..900&family=Noto+Naskh+Arabic:wght@400..700&family=IBM+Plex+Mono:wght@400;500;600&display=swap',
          },
        },
      ],
      customCss: ['./src/styles/custom.css'],
    }),
  ],
});
