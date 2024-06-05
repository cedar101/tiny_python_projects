from abc import ABC, abstractmethod
from enum import Flag, auto
from dataclasses import make_dataclass


class OptionFlag(Flag):
    BYTES = auto()
    WORDS = auto()
    LINES = auto()
    CHARS = auto()
    ALL = LINES | WORDS | BYTES

    def __str__(self):
        return f"{self.name.lower()}"


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


class FileLineCountData(FileCountData):
    def reset(self):
        self.lines = 0

    def inclease(self, line):
        self.lines += 1


class FileWordCountData(FileCountData):
    def reset(self):
        self.words = 0

    def inclease(self, line):
        self.words += len(line.split())


class FileByteCountData(FileCountData):
    def reset(self):
        self.bytes = 0

    def inclease(self, line):
        self.bytes += len(line.encode())


class FileCharCountData(FileCountData):
    def reset(self):
        self.chars = 0

    def inclease(self, line):
        self.chars += len(line)


# class FileAllCountData(FileCountData):
#     def count(self):
#         self.num_lines, self.num_words, self.num_bytes, self.num_chars = 0, 0, 0, 0
#         for line in self.file:
#             self.num_lines += 1
#             self.num_words += len(line.split())
#             self.num_bytes += len(line.encode())
#             self.num_chars += len(line)


def make_counter(options: OptionFlag):
    fields = [(str(opt), int) for opt in options]
    namespace = {"reset"}

    def reset(self):
        pass

    make_dataclass(
        "FileCounter",
    )
