"""Read a registry or data table: one reader for every tab-separated file here.

A registry (`standards/terminology/registries/*.tsv`) opens with a comment
block, and the last comment line before the rows names the columns:

    # a paragraph saying what the set is and where it comes from
    # code	kind	arabic	ref
    nafi	qiraah	نَافِع	nashr 1/99

A data table (`standards/terminology/data/*.tsv`) may instead put the column
names in its first uncommented row. Both read the same way, and a caller
addresses a column by name rather than by counting tabs.

    from registry import read, records
    header, rows = read("standards/terminology/registries/qiraat.tsv")
    for row in records(path): row["code"], row["arabic"]

The file is split on tabs, not parsed as CSV: a registry cell never carries a
quote or a tab, and a comment line may carry anything.
"""
import os


def read(path, header_in_first_row=None):
    """(header, rows). Rows are lists of stripped cells, blank lines dropped.

    `header_in_first_row` says where the column names are: True for a data
    table, False for a registry, None to take the last comment line when one
    names more than one column and the first row otherwise.
    """
    header, rows = None, []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line.startswith("#"):
                fields = [c.strip() for c in line.lstrip("#").split("\t")]
                if len(fields) > 1 and header_in_first_row is not True:
                    header = fields
                continue
            if line.strip():
                rows.append([c.strip() for c in line.split("\t")])
    if header is None and rows and header_in_first_row is not False:
        header = rows.pop(0)
    if header is None:
        raise ValueError(f"{os.path.basename(path)}: no header line names the columns")
    return header, rows


def records(path, header_in_first_row=None):
    """The rows as dicts keyed by column name; a short row reads as empty cells."""
    header, rows = read(path, header_in_first_row)
    return [dict(zip(header, row + [""] * (len(header) - len(row)))) for row in rows]


def column(header, rows, name):
    """One column, by name; empty where a row is short."""
    i = header.index(name)
    return [row[i] if i < len(row) else "" for row in rows]
