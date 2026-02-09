import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


class DisplayBook(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(DisplayBook):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayBook):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class PrintBook(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class ConsolePrint(PrintBook):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...\n"
              f"{book.content}")


class ReversePrint(PrintBook):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...\n"
              f"{book.content[::-1]}")


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({
            "title": book.title,
            "content": book.content
        })


class XMLSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


DISPLAY_STRATEGIES = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}

PRINT_STRATEGIES = {
    "console": ConsolePrint(),
    "reverse": ReversePrint(),
}

SERIALIZERS = {
    "json": JSONSerializer(),
    "xml": XMLSerializer(),
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for command, method_type in commands:
        if command == "display":
            DISPLAY_STRATEGIES[method_type].display(book)

        elif command == "print":
            PRINT_STRATEGIES[method_type].print(book)

        elif command == "serialize":
            return SERIALIZERS[method_type].serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
