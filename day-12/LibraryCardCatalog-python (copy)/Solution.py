class Card:
    def __init__(self, title, author, subject):
        self.title = title
        self.author = author
        self.subject = subject

    def __str__(self):
        return f"Title: {self.title} | Author: {self.author} | Subject: {self.subject}"

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_subject(self):
        return self.subject


class CardCatalog:
    def __init__(self):
        self.catalog = []

    def add_a_card(self, card):
        self.catalog.append(card)
        self.catalog.sort(key=lambda c: c.get_title())

    def get_a_title(self, title):
        for card in self.catalog:
            if card.get_title().lower() == title.lower():
                return card
        return "Not Found"

    def get_an_author(self, author):
        books_by_author = []
        for card in self.catalog:
            if card.get_author().lower() == author.lower():
                books_by_author.append(card)
        return books_by_author

    def get_subject(self, subject):
        books_by_subject = []
        for card in self.catalog:
            if card.get_subject().lower() == subject.lower():
                books_by_subject.append(card)
        return books_by_subject

    def remove_a_title(self, title):
        self.catalog = [card for card in self.catalog if card.get_title().lower() != title.lower()]
        return True

    def print_the_catalog(self):
        if not self.catalog:
            print("The catalog is empty.")
        else:
            for card in self.catalog:
                print(card)
