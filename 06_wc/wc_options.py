from abc import ABC, abstractmethod
from enum import Flag, auto
from dataclasses import dataclass, InitVar, make_dataclass


class OptionFlag(Flag):
    BYTES = auto()
    WORDS = auto()
    LINES = auto()
    CHARS = auto()
    ALL = LINES | WORDS | BYTES

    def __str__(self):
        return f"{self.name.lower()}"


class ContentCounter(ABC):
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        setattr(obj, self.private_name, value)

    @abstractmethod
    def count(self, line):
        self.__get__()


class LineCounter(ContentCounter):
    def count(self, line):
        

    # @dataclass
    # class FileCounter:
    #     bytes: int
    #     words: int
    #     lines: int
    #     chars: int
    #     options: InitVar[OptionFlag]

    #     def __post_init__(self, options):
    #         for opt in options:

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

    # class ContentCountData(ABC):
    #     def __init__(self, value):

    #     def reset(self):
    #         self._value = 0

    def inclease(self, line):
        self.value += 1

    # class FileWordCountData:
    #     def reset(self):
    #         self.value = 0

    def inclease(self, line):
        self.value += len(line.split())

    # class FileByteCountData:
    #     def reset(self):
    #         self.value = 0

    def inclease(self, line):
        self.value += len(line.encode())

    # class FileCharCountData:
    #     def reset(self):
    #         self.value = 0

    def inclease(self, line):
        self.value += len(line)


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
