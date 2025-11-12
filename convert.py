import argparse
from textwrap import dedent, indent
from typing import Sequence, NamedTuple
from pathlib import Path
import csv

TEMPLATE = dedent(
    """\
---
title: '{title}'
{authors}
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

{text}
{references}
"""
)

author_template = dedent(
    """\
- name: {name}
  affiliations:
    - {affiliation}"""
)


class Author(NamedTuple):
    name: str
    affiliation: str

    def to_str(self):
        return author_template.format(
            name=self.name,
            affiliation=self.affiliation,
        )


def read_paper(row: dict[str, str]) -> str:
    authors = []

    author_affiliation_list = row["List of authors and affiliations"].split(";")

    for entry in author_affiliation_list:
        parts = entry.strip().split(",", 1)  # Split only at the first comma
        if len(parts) == 2:
            author_name = parts[0].strip()
            affiliation = parts[1].strip()

            authors.append(
                Author(
                    name=author_name,
                    affiliation=affiliation,
                )
            )
    authors = "authors:\n" + indent("\n".join([a.to_str() for a in authors]), "  ")

    link_to_repo = row["Link to open-source software repository (if applicable)"]

    if len(link_to_repo) > 0:
        link_to_repo = f"\n# Repository\n{link_to_repo}\n"

    return TEMPLATE.format(
        title=row["Title"].replace("'", "''"),
        authors=authors,
        text=row["Abstract"],
        references=link_to_repo,
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("path", type=Path)
    parser.add_argument("-o", "--output", type=Path, default=None)
    args = vars(parser.parse_args(argv))

    outdir = args["output"] or Path("abstract_files")
    outdir.mkdir(parents=True, exist_ok=True)

    # count the words
    if not args["path"].is_file():
        print(f"{args['path']} is not a file")
        return 1

    with open(args["path"], "r") as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader if any(row.values())]
        for row in rows:
            # remove all linebreaks that would cause the markdown to break unless it's in the abstract
            for key, value in row.items():
                if key != "Abstract":
                    row[key] = value.replace("\n", " ")

            # filename is last-name of author + first word of title
            last_name = row["List of authors and affiliations"].split(",")[0].split()[0]
            first_word_title = row["Title"].replace("-", " ").split()[0]
            slug = f"{last_name}-{first_word_title}".lower()

            # remove invalid characters
            slug = slug.replace(" ", "").replace("/", "").replace(":", "").replace(",", "")

            output = read_paper(row)
            if row["Abstract decision"] in ["Poster", "Oral", "Plenary", "Tutorial"]:
                (outdir / f"{slug}.md").write_text(output)
            else:
                print(f"Skipping {slug} due to decision {row['Abstract decision']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
