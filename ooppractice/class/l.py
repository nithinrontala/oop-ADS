class Card:
    def __init__(self, title, author, subject):
        self.title = title
        self.author = author
        self.subject = subject

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Subject: {self.subject}"

class CardCatalog:
    def __init__(self):
        self.cards = []

    def add_card(self, title, author, subject):
        card = Card(title, author, subject)
        self.cards.append(card)

    def get_title(self, title):
        for card in self.cards:
            if card.title == title:
                return card
        return None

    def get_author(self, author):
        return [card for card in self.cards if card.author == author]

    def get_subject(self, subject):
        return [card for card in self.cards if card.subject == subject]

    def remove_title(self, title):
        for card in self.cards:
            if card.title == title:
                self.cards.remove(card)
                return True
        return False

    def print_catalog(self):
        return [str(card) for card in self.cards]

    def run_catalog(self):
        while True:
            try:
                s = input().split()
                if s[0] == "add":
                    self.add_card(s[1], s[2], s[3])
                    print(self.print_catalog())
                elif s[0] == "display":
                    print(self.print_catalog())
                elif s[0] == "gettitle":
                    card = self.get_title(s[1])
                    print(card if card else "Title not found")
                elif s[0] == "getaut":
                    print([str(card) for card in self.get_author(s[1])])
                elif s[0] == "getsub":
                    print([str(card) for card in self.get_subject(s[1])])
                elif s[0] == "remove":
                    removed = self.remove_title(s[1])
                    print("Removed" if removed else "Title not found")
            except:
                break

if __name__ == "__main__":
    c1 = CardCatalog()
    c1.run_catalog()
