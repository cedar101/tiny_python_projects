from collections.abc import Iterable


def wc_per_file(iterable: Iterable) -> tuple[int, int, int]:
    num_lines, num_words, num_bytes = 0, 0, 0
    for line in iterable:
        num_lines += 1
        num_words += len(line.split())
        num_bytes += len(line.encode())
    return num_lines, num_words, num_bytes


def print_per_file(
    num_lines: int, num_words: int, num_bytes: int, filename: str
) -> None:
    """
    >>> print_per_file(3, 4, 17, 'inputs/foo.txt')
           3       4      17 inputs/foo.txt
    """

    print(f"{num_lines:8}{num_words:8}{num_bytes:8} {filename}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
