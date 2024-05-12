#!/usr/bin/env python3
"""
usage: {} [-h] [-f FILE] <letter>...

Gashlycrumb

positional arguments:
  <letter>              Letter(s)

options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  Input file [type: path] [default: gashlycrumb.txt]
"""
from typing import Annotated

import typer


# --------------------------------------------------
def main(
    letter: Annotated[list[str], typer.Argument(help="Letter(s)")],
    file: Annotated[
        typer.FileText, typer.Option("--file", "-f", help="Input file")
    ] = "gashlycrumb.txt",
):
    """Gashlycrumb"""
    lookup = {line[0].upper(): line.rstrip() for line in file}

    for lt in letter:
        print(lookup.get(lt.upper(), f'I do not know "{lt}".'))


# --------------------------------------------------
if __name__ == "__main__":
    typer.run(main)
