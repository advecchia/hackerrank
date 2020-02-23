from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display():
        pass


class MyBook(Book, metaclass=ABCMeta):
    def __init__(self, book_title, book_author, book_price):
        super().__init__(book_title, book_author)
        self.price = book_price

    def display(self):
        print('Title: %s' % self.title)
        print('Author: %s' % self.author)
        print('Price: %s' % self.price)


title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
