class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pagers={self.pages!r})"

    @property
    def pages(self):
        return self._pages

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pagers={self.duration!r})"

    @property
    def duration(self):
        return self._duration

if __name__ == '__main__':
    paperbook = PaperBook("Муму", "Достоевский", 120)
    audiobook = AudioBook("Война и мир", "Толстой", 300)
    print(paperbook)
    print(audiobook)
