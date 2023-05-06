#!/bin/env/python3

from pathlib import Path


def process_and_write_opml(opml, lang):
    res = ""
    with open(opml) as opml_file:
        for line in opml_file.readlines():
            stripped_line = line.strip()
            is_outline_entry = stripped_line.startswith(
                "<outline") and stripped_line.endswith("/>")
            if not is_outline_entry:
                res += line
            elif stripped_line.endswith(f'language="{lang}"/>') or stripped_line.endswith(f'language="{lang}" />'):
                res += line

    opml_path = Path(opml)
    output_path = Path(
        opml_path.parent, f"{opml_path.stem}-{lang}{opml_path.suffix}")
    with open(output_path, "w") as file:
        file.write(res)


def main():
    process_and_write_opml("./Feeds.opml", "zh")
    process_and_write_opml("./Feeds.opml", "en")
    process_and_write_opml("./Podcasts.opml", "zh")


if __name__ == "__main__":
    main()
