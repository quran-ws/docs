"""Local guideline preview: python tools/preview.py (install requirements-preview.txt)."""

import argparse
import hashlib
import html
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import subprocess
import sys
from urllib.parse import unquote

import markdown
import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
last_sources = None
error = ""


def fingerprint(paths):
    return hashlib.sha256("".join(
        f"{p}:{p.stat().st_mtime_ns}:{p.stat().st_size}" for p in sorted(paths)
    ).encode()).hexdigest()


def refresh():
    global last_sources, error
    sources = fingerprint(list((CONTENT / "pages").glob("*.yml")) +
                          list((CONTENT / "fragments").rglob("*.md")) +
                          list((ROOT / "standards").rglob("*.yml")) +
                          list((ROOT / "standards").rglob("*.tsv")))
    if sources != last_sources:
        last_sources = sources
        error = ""
        for script in ("generate_pages.py", "generate_dictionary.py", "generate_registries.py"):
            result = subprocess.run([sys.executable, str(ROOT / "tools" / script)],
                                    cwd=ROOT, capture_output=True, text=True)
            if result.returncode:
                error = result.stdout + result.stderr
                break
    return fingerprint(list(CONTENT.rglob("*.md"))) + sources


def read_page(path):
    text = path.read_text()
    if text.startswith("---\n"):
        _, front, text = text.split("---", 2)
        return yaml.safe_load(front) or {}, text
    return {}, text


STYLE = """
:root{font-family:system-ui,sans-serif;color:#183d34;background:#fafbf8}
*{box-sizing:border-box}[hidden]{display:none!important}body{margin:0}a{color:#176a52}header{padding:18px 28px;
border-bottom:1px solid #dce4db;display:flex;justify-content:space-between;background:white}
.layout{display:grid;grid-template-columns:260px minmax(0,900px);max-width:1250px;margin:auto}
nav{padding:26px 20px;position:sticky;top:0;height:100vh;overflow:auto}
nav a{display:block;padding:9px 12px;text-decoration:none;border-radius:6px;font-size:14px}
nav a.active{background:#e1eee5;font-weight:650}nav input{width:100%;padding:10px;
border:1px solid #cedace;border-radius:6px;margin-bottom:16px;background:white}
main{padding:36px 48px;min-width:0;line-height:1.85}h1{font-size:38px;line-height:1.3}
h2{margin-top:48px;border-top:1px solid #dce4db;padding-top:28px;line-height:1.4}
h3{line-height:1.5}pre{direction:ltr;text-align:left;background:#edf1e9;padding:20px;
overflow:auto;border-radius:8px;line-height:1.65}code{font-size:.9em;unicode-bidi:isolate}
:not(pre)>code{font-family:ui-monospace,monospace;direction:ltr;display:inline-block;
background:#edf1e9;border:1px solid #d7e0d5;border-radius:4px;padding:0 .3em;line-height:1.5}
table{display:block;overflow:auto;border-collapse:collapse;font-size:14px}
td,th{border:1px solid #d7e0d5;padding:10px;text-align:start}blockquote{margin-inline:0;
border-inline-start:3px solid #4b8166;padding-inline-start:20px;color:#526b60}
.meta{font-size:13px;color:#536b60}.source{overflow-wrap:anywhere}.error{background:#ffe8dd;
color:#7a2814;padding:20px;white-space:pre-wrap}summary{cursor:pointer}.toc{font-size:14px}
@media(max-width:750px){.layout{display:block}nav{position:static;height:auto;padding:16px}
nav .pages{max-height:180px;overflow:auto}main{padding:24px}header{padding:16px;font-size:14px}}
"""


class Handler(BaseHTTPRequestHandler):
    def reply(self, status, body, kind="text/html; charset=utf-8"):
        data = body.encode()
        self.send_response(status)
        self.send_header("Content-Type", kind)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        version = refresh()
        route = unquote(self.path.split("?", 1)[0])
        if route == "/__version":
            self.reply(200, json.dumps(version), "application/json")
            return
        route = route.removeprefix("/docs").removeprefix("/guidelines").strip("/")
        if not route:
            route = "en/naming"
        if route.split("/")[0] not in ("en", "ar"):
            route = "en/" + route
        route = route.removesuffix(".md")
        path = (CONTENT / (route + ".md")).resolve()
        if not path.is_relative_to(CONTENT) or not path.is_file():
            self.reply(404, '<p>Page not available locally. <a href="/en/naming/">Guidelines</a></p>')
            return
        language, slug = route.split("/", 1)
        meta, body = read_page(path)
        title = meta.get("title", path.stem)
        renderer = markdown.Markdown(extensions=["extra", "toc", "sane_lists"])
        rendered = renderer.convert(body)
        links = []
        for page in sorted((CONTENT / language).rglob("*.md")):
            info, _ = read_page(page)
            relative = page.relative_to(CONTENT).with_suffix("").as_posix()
            links.append(f'<a class="{"active" if page == path else ""}" href="/{relative}/">'
                         f'{html.escape(str(info.get("title", page.stem)))}</a>')
        source = meta.get("generated", str(path.relative_to(ROOT)))
        if slug == "reference/dictionary":
            source = "standards/terminology/concepts/"
        elif slug == "reference/registries":
            source = "standards/terminology/registries/"
        alternate = "ar" if language == "en" else "en"
        direction = "rtl" if language == "ar" else "ltr"
        warning = f'<pre class="error">{html.escape(error)}</pre>' if error else ""
        self.reply(200, f'''<!doctype html><html lang="{language}"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(str(title))} · Quran.ws preview</title>
<style>{STYLE}</style><header><strong>Quran.ws · Local guidelines preview</strong>
<a href="/{alternate}/{slug}/">{'العربية' if alternate == 'ar' else 'English'}</a></header>
<div class="layout"><nav dir="{direction}"><input aria-label="Filter pages" placeholder="Filter pages…"
oninput="document.querySelectorAll('nav .pages a').forEach(a=>a.hidden=!a.textContent.toLowerCase().includes(this.value.toLowerCase()))">
<div class="pages">{''.join(links)}</div></nav><main dir="{direction}">{warning}
<div class="meta">{html.escape(str(meta.get('status', '')))} · Refreshes automatically on save</div>
<h1>{html.escape(str(title))}</h1><details class="meta source" dir="ltr"><summary>Source to edit</summary>
<code>{html.escape(str(ROOT / source))}</code></details>
<details><summary>{'في هذه الصفحة' if language == 'ar' else 'On this page'}</summary>{renderer.toc}</details>
{rendered}</main></div><script>
const version={json.dumps(version)};
const scrollKey='preview-scroll:'+location.pathname;
const previous=sessionStorage.getItem(scrollKey);
if(previous!==null){{scrollTo(0,Number(previous));sessionStorage.removeItem(scrollKey)}}
setInterval(async()=>{{try{{const next=await (await fetch('/__version')).json();
if(next!==version){{sessionStorage.setItem(scrollKey,String(scrollY));location.reload()}}}}catch(e){{}}}},1000);
</script></html>''')

    def log_message(self, format, *args):
        if "/__version" not in str(args):
            super().log_message(format, *args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    refresh()
    print(f"Guidelines preview: http://127.0.0.1:{args.port}/en/naming/", flush=True)
    ThreadingHTTPServer(("127.0.0.1", args.port), Handler).serve_forever()
