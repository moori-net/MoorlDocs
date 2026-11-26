import re
from collections import defaultdict
from html import unescape
from pathlib import Path

from markdown import Markdown
from mkdocs.plugins import event_priority
from mkdocs.utils.meta import get_data


NAV_SECTION = "Plugin Dokumentation"
DATE_IN_FILENAME = re.compile(r"(?<!\d)\d{4}-\d{2}-\d{2}(?!\d)")


def plugin_title(index, markdown):
    source = Path(index.abs_src_path).read_text(encoding="utf-8-sig")
    content, metadata = get_data(source)
    markdown.reset().convert(content)
    for token in markdown.toc_tokens:
        if token["level"] == 1 and (heading := unescape(token["name"]).strip()):
            title = metadata.get("title")
            return title.strip() if isinstance(title, str) and title.strip() else heading
    return None


# Run after i18n (-100), which selects the pages for the current locale.
@event_priority(-101)
def on_files(files, config):
    plugin_pages = defaultdict(dict)
    for file in files.documentation_pages():
        if not file.inclusion.is_in_nav():
            continue

        # i18n's normalized path omits the language suffix.
        parts = getattr(file, "norm_src_uri", file.src_uri).split("/")
        if len(parts) < 3 or parts[0] != "plugin":
            continue
        if DATE_IN_FILENAME.search(parts[-1]) or any(
            part.casefold() == "superpowers" for part in parts[1:-1]
        ):
            continue

        _, directory, *path = parts
        plugin_pages[directory]["/".join(path)] = file

    markdown = Markdown(extensions=["attr_list", "fenced_code", "toc"])
    plugins = []
    for directory, pages in plugin_pages.items():
        index_path = next((path for path in pages if path.rsplit(".", 1)[0] == "index"), None)
        if index_path is None:
            continue
        index = pages.pop(index_path)
        title = plugin_title(index, markdown)
        if title is None:
            continue
        if title.startswith("{var:"):
            title = directory

        target = index.src_uri
        if pages:
            target = [{"Übersicht": index.src_uri}]
            target.extend(pages[path].src_uri for path in sorted(pages, key=str.casefold))
        plugins.append((directory, title, target))

    plugins.sort(key=lambda plugin: (plugin[0] != "MoorlFoundation", plugin[0].casefold()))
    for item in config.nav:
        if isinstance(item, dict) and NAV_SECTION in item:
            # Keep the overview and replace the generated entries on each build.
            item[NAV_SECTION][1:] = [{title: target} for _, title, target in plugins]
            break
