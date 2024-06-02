from collections.abc import Iterable
from abc import ABC, abstractmethod
from enum import Flag, auto
from dataclasses import make_dataclass


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


# --------------------------------------------------
# class OptionFlag(Flag):
#     BYTES = auto()
#     WORDS = auto()
#     LINES = auto()
#     CHARS = auto()
#     ALL = LINES | WORDS | BYTES

#     def __str__(self):
#         return f"{self.name.lower()}"


# class FileCountData(ABC):
#     # def __init__(self, file: TextIO):
#     #     self.file = file

#     def count(self):
#         self.reset()
#         for line in self.file:
#             self.increase()

#     @abstractmethod
#     def reset(self): ...

#     @abstractmethod
#     def increase(self): ...


# class FileLineCountData(FileCountData):
#     def reset(self):
#         self.lines = 0

#     def inclease(self):
#         self.lines += 1


# class FileWordCountData(FileCountData):
#     def reset(self):
#         self.words = 0

#     def inclease(self):
#         self.words += 1


# class FileByteCountData(FileCountData):
#     def reset(self):
#         self.bytes = 0

#     def inclease(self):
#         self.bytes += 1


# class FileCharCountData(FileCountData):
#     def reset(self):
#         self.chars = 0

#     def inclease(self):
#         self.chars += 1


# class FileAllCountData(FileCountData):
#     def count(self):
#         self.num_lines, self.num_words, self.num_bytes, self.num_chars = 0, 0, 0, 0
#         for line in self.file:
#             self.num_lines += 1
#             self.num_words += len(line.split())
#             self.num_bytes += len(line.encode())
#             self.num_chars += len(line)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
