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

    def __get__(self, instance, owner=None):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        setattr(instance, self.private_name, self.__get__(instance) + self.count(value))

    @abstractmethod
    def count(self, line: str) -> int:
        pass


class LineCounter(ContentCounter):
    def count(self, line):
        return 1


class WordCounter(ContentCounter):
    def count(self, line):
        return len(line.split())


class ByteCounter(ContentCounter):
    def count(self, line):
        return len(line.encode())


class CharCounter(ContentCounter):
    def count(self, line):
        return len(line)


def make_counter(options: OptionFlag):
    fields = [(str(opt), int) for opt in options]
    namespace = {"reset"}

    def reset(self):
        pass

    make_dataclass(
        "FileCounter",
    )
