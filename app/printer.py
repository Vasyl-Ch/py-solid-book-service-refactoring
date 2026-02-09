from abc import ABC, abstractmethod
from app.models import Book


class PrintBook(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrint(PrintBook):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...\n"
              f"{book.content}")


class ReversePrint(PrintBook):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...\n"
              f"{book.content[::-1]}")
