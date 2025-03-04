
from Solution import Card, CardCatalog


def test_add_a_card():
    print("==================== Testing add_a_card() ====================")
    # Test Case 1: Add to an empty catalog.
    catalog1 = CardCatalog()
    catalog1.add_a_card(Card("Animal Farm", "George Orwell", "Dystopia"))
    print("Test Case 1: Expected catalog order:")
    print("  Title: Animal Farm | Author: George Orwell | Subject: Dystopia")
    print("Actual catalog:")
    catalog1.print_the_catalog()
    print()

    # Test Case 2: Add a card that should appear at the beginning.
    catalog2 = CardCatalog()
    catalog2.add_a_card(Card("Moby Dick", "Herman Melville", "Adventure"))
    catalog2.add_a_card(Card("A Tale of Two Cities", "Charles Dickens", "Historical"))
    print("Test Case 2: Expected catalog order:")
    print("  Title: A Tale of Two Cities | Author: Charles Dickens | Subject: Historical")
    print("  Title: Moby Dick | Author: Herman Melville | Subject: Adventure")
    print("Actual catalog:")
    catalog2.print_the_catalog()
    print()

    # Test Case 3: Add a card that should appear in the middle.
    catalog3 = CardCatalog()
    catalog3.add_a_card(Card("A Farewell to Arms", "Ernest Hemingway", "War"))
    catalog3.add_a_card(Card("The Great Gatsby", "F. Scott Fitzgerald", "Drama"))
    catalog3.add_a_card(Card("Brave New World", "Aldous Huxley", "Dystopia"))
    print("Test Case 3: Expected catalog order:")
    print("  Title: A Farewell to Arms | Author: Ernest Hemingway | Subject: War")
    print("  Title: Brave New World | Author: Aldous Huxley | Subject: Dystopia")
    print("  Title: The Great Gatsby | Author: F. Scott Fitzgerald | Subject: Drama")
    print("Actual catalog:")
    catalog3.print_the_catalog()
    print()

    # Test Case 4: Add a card with a title that matches (case-insensitive).
    catalog4 = CardCatalog()
    catalog4.add_a_card(Card("Hamlet", "William Shakespeare", "Tragedy"))
    catalog4.add_a_card(Card("hamlet", "Someone Else", "Drama"))
    print("Test Case 4: Expected catalog (both entries, order may vary but adjacent):")
    print("  Title: Hamlet | Author: William Shakespeare | Subject: Tragedy")
    print("  Title: hamlet | Author: Someone Else | Subject: Drama")
    print("Actual catalog:")
    catalog4.print_the_catalog()


def test_get_a_title():
    print("\n==================== Testing get_a_title() ====================")
    # Test Case 1: Card exists with exact title.
    catalog1 = CardCatalog()
    catalog1.add_a_card(Card("1984", "George Orwell", "Dystopia"))
    print('Test Case 1: Searching for title "1984"')
    found = catalog1.get_a_title("1984")
    print("Expected: Title: 1984 | Author: George Orwell | Subject: Dystopia")
    print("Actual: " + (str(found) if found else "Not Found"))

    # Test Case 2: Card does not exist.
    catalog2 = CardCatalog()
    catalog2.add_a_card(Card("To Kill a Mockingbird", "Harper Lee", "Drama"))
    print('\nTest Case 2: Searching for title "The Catcher in the Rye"')
    found = catalog2.get_a_title("The Catcher in the Rye")
    print("Expected: Not Found")
    print("Actual: " + (str(found) if found else "Not Found"))

    # Test Case 3: Case-insensitive matching.
    catalog3 = CardCatalog()
    catalog3.add_a_card(Card("The Hobbit", "J.R.R. Tolkien", "Fantasy"))
    print('\nTest Case 3: Searching for title "the hobbit" (lowercase)')
    found = catalog3.get_a_title("the hobbit")
    print("Expected: Title: The Hobbit | Author: J.R.R. Tolkien | Subject: Fantasy")
    print("Actual: " + (str(found) if found else "Not Found"))

    # Test Case 4: Multiple cards with the same title.
    catalog4 = CardCatalog()
    catalog4.add_a_card(Card("Dune", "Frank Herbert", "Science Fiction"))
    catalog4.add_a_card(Card("Dune", "Another Author", "Different Subject"))
    print('\nTest Case 4: Searching for title "Dune" with multiple entries (should return first)')
    found = catalog4.get_a_title("Dune")
    print("Expected: First inserted Dune card (Frank Herbert)")
    print("Actual: " + (str(found) if found else "Not Found"))


def test_get_an_author():
    print("\n==================== Testing get_an_author() ====================")
    # Test Case 1: Single card by author.
    catalog1 = CardCatalog()
    catalog1.add_a_card(Card("Pride and Prejudice", "Jane Austen", "Romance"))
    print('Test Case 1: Searching for author "Jane Austen"')
    author_cards = catalog1.get_an_author("Jane Austen")
    print("Expected: 1 card - Pride and Prejudice")
    print("Actual:")
    for card in author_cards:
        print(card)

    # Test Case 2: Multiple cards by same author.
    catalog2 = CardCatalog()
    catalog2.add_a_card(Card("Emma", "Jane Austen", "Romance"))
    catalog2.add_a_card(Card("Sense and Sensibility", "Jane Austen", "Romance"))
    print('\nTest Case 2: Searching for author "Jane Austen" (multiple entries)')
    author_cards = catalog2.get_an_author("Jane Austen")
    print("Expected: 2 cards - Emma and Sense and Sensibility")
    print("Actual:")
    for card in author_cards:
        print(card)

    # Test Case 3: No cards by the given author.
    catalog3 = CardCatalog()
    catalog3.add_a_card(Card("The Odyssey", "Homer", "Epic"))
    print('\nTest Case 3: Searching for author "Jane Austen" when none exist')
    author_cards = catalog3.get_an_author("Jane Austen")
    print("Expected: Empty list")
    print("Actual: " + ("Empty list" if not author_cards else str(author_cards)))

    # Test Case 4: Case-insensitive author matching.
    catalog4 = CardCatalog()
    catalog4.add_a_card(Card("Great Expectations", "Charles Dickens", "Fiction"))
    print('\nTest Case 4: Searching for author "charles dickens" (lowercase)')
    author_cards = catalog4.get_an_author("charles dickens")
    print("Expected: 1 card - Great Expectations")
    print("Actual:")
    for card in author_cards:
        print(card)


def test_get_subject():
    print("\n==================== Testing get_subject() ====================")
    # Test Case 1: Single card by subject.
    catalog1 = CardCatalog()
    catalog1.add_a_card(Card("The Shining", "Stephen King", "Horror"))
    print('Test Case 1: Searching for subject "Horror"')
    subject_cards = catalog1.get_subject("Horror")
    print("Expected: 1 card - The Shining")
    print("Actual:")
    for card in subject_cards:
        print(card)

    # Test Case 2: Multiple cards on the same subject.
    catalog2 = CardCatalog()
    catalog2.add_a_card(Card("It", "Stephen King", "Horror"))
    catalog2.add_a_card(Card("Carrie", "Stephen King", "Horror"))
    print('\nTest Case 2: Searching for subject "Horror" (multiple entries)')
    subject_cards = catalog2.get_subject("Horror")
    print("Expected: 2 cards - It and Carrie")
    print("Actual:")
    for card in subject_cards:
        print(card)

    # Test Case 3: No cards for a given subject.
    catalog3 = CardCatalog()
    catalog3.add_a_card(Card("The Great Gatsby", "F. Scott Fitzgerald", "Drama"))
    print('\nTest Case 3: Searching for subject "Science Fiction" when none exist')
    subject_cards = catalog3.get_subject("Science Fiction")
    print("Expected: Empty list")
    print("Actual: " + ("Empty list" if not subject_cards else str(subject_cards)))

    # Test Case 4: Case-insensitive subject matching.
    catalog4 = CardCatalog()
    catalog4.add_a_card(Card("Foundation", "Isaac Asimov", "Science Fiction"))
    print('\nTest Case 4: Searching for subject "science fiction" (lowercase)')
    subject_cards = catalog4.get_subject("science fiction")
    print("Expected: 1 card - Foundation")
    print("Actual:")
    for card in subject_cards:
        print(card)


def test_remove_a_title():
    print("\n==================== Testing remove_a_title() ====================")
    # Test Case 1: Remove an existing card.
    catalog1 = CardCatalog()
    catalog1.add_a_card(Card("The Catcher in the Rye", "J.D. Salinger", "Fiction"))
    print('Test Case 1: Removing title "The Catcher in the Rye"')
    removed = catalog1.remove_a_title("The Catcher in the Rye")
    print("Expected: True; catalog should now be empty.")
    print("Actual:", removed)
    print("Catalog after removal:")
    catalog1.print_the_catalog()

    # Test Case 2: Remove when title does not exist.
    catalog2 = CardCatalog()
    catalog2.add_a_card(Card("Lord of the Flies", "William Golding", "Allegory"))
    print('\nTest Case 2: Removing title "Animal Farm" (does not exist)')
    removed = catalog2.remove_a_title("Animal Farm")
    print("Expected: False; catalog should remain unchanged.")
    print("Actual:", removed)
    print("Catalog after attempted removal:")
    catalog2.print_the_catalog()

    # Test Case 3: Case-insensitive removal.
    catalog3 = CardCatalog()
    catalog3.add_a_card(Card("Frankenstein", "Mary Shelley", "Horror"))
    print('\nTest Case 3: Removing title "frankenstein" (lowercase)')
    removed = catalog3.remove_a_title("frankenstein")
    print("Expected: True; catalog should now be empty.")
    print("Actual:", removed)
    print("Catalog after removal:")
    catalog3.print_the_catalog()

    # Test Case 4: Remove when multiple cards have the same title.
    catalog4 = CardCatalog()
    catalog4.add_a_card(Card("Dune", "Frank Herbert", "Science Fiction"))
    catalog4.add_a_card(Card("Dune", "Another Author", "Different Genre"))
    print('\nTest Case 4: Removing title "Dune" when multiple exist')
    removed = catalog4.remove_a_title("Dune")
    print("Expected: True; one Dune should be removed, leaving one remaining.")
    print("Actual:", removed)
    print("Catalog after removal:")
    catalog4.print_the_catalog()


def test_print_the_catalog():
    print("\n==================== Testing print_the_catalog() ====================")
    # Test Case 1: Print an empty catalog.
    catalog1 = CardCatalog()
    print('Test Case 1: Printing an empty catalog')
    print("Expected: \"The catalog is empty.\"")
    print("Actual:")
    catalog1.print_the_catalog()

    # Test Case 2: Print a catalog with a single card.
    catalog2 = CardCatalog()
    catalog2.add_a_card(Card("Fahrenheit 451", "Ray Bradbury", "Dystopia"))
    print('\nTest Case 2: Printing a catalog with one card')
    print("Expected: One card printed - Fahrenheit 451")
    print("Actual:")
    catalog2.print_the_catalog()

    # Test Case 3: Print a catalog with multiple cards in sorted order.
    catalog3 = CardCatalog()
    catalog3.add_a_card(Card("Brave New World", "Aldous Huxley", "Dystopia"))
    catalog3.add_a_card(Card("1984", "George Orwell", "Dystopia"))
    catalog3.add_a_card(Card("Animal Farm", "George Orwell", "Political Satire"))
    print('\nTest Case 3: Printing a catalog with multiple cards (sorted order)')
    print("Expected order (alphabetical by title):")
    print("  Title: 1984 ...")
    print("  Title: Animal Farm ...")
    print("  Title: Brave New World ...")
    print("Actual:")
    catalog3.print_the_catalog()

    # Test Case 4: Print after removing a card.
    catalog4 = CardCatalog()
    catalog4.add_a_card(Card("The Hobbit", "J.R.R. Tolkien", "Fantasy"))
    catalog4.add_a_card(Card("The Lord of the Rings", "J.R.R. Tolkien", "Fantasy"))
    print('\nTest Case 4: Removing "The Hobbit" then printing catalog')
    removed = catalog4.remove_a_title("The Hobbit")
    print("Removal expected: True. Actual:", removed)
    print("Expected catalog:")
    print("  Title: The Lord of the Rings | Author: J.R.R. Tolkien | Subject: Fantasy")
    print("Actual catalog:")
    catalog4.print_the_catalog()


def main():
    test_add_a_card()
    test_get_a_title()
    test_get_an_author()
    test_get_subject()
    test_remove_a_title()
    test_print_the_catalog()


if __name__ == "__main__":
    main()
