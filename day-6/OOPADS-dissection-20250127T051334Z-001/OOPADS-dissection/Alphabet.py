class Alphabet:
    """
    A class to represent an alphabet for use in string-processing tasks.
    Converts between characters of the alphabet and their respective indices.
    """

    # Predefined alphabets
    BINARY = None
    OCTAL = None
    DECIMAL = None
    HEXADECIMAL = None
    DNA = None
    LOWERCASE = None
    UPPERCASE = None
    PROTEIN = None
    BASE64 = None
    ASCII = None
    EXTENDED_ASCII = None
    UNICODE16 = None

    def __init__(self, alpha):
        """
        Initialize the Alphabet instance.

        :param alpha: A string containing the characters of the alphabet.
        """
        self.alphabet = list(alpha)
        self.R = len(alpha)  # The radix or size of the alphabet
        self.inverse = {char: idx for idx, char in enumerate(self.alphabet)}

        # Check for duplicate characters in the alphabet
        if len(set(self.alphabet)) != len(self.alphabet):
            raise ValueError("Illegal alphabet: contains duplicate characters.")

    @classmethod
    def initialize_predefined_alphabets(cls):
        """Initialize predefined alphabets as class-level attributes."""
        cls.BINARY = Alphabet("01")
        cls.OCTAL = Alphabet("01234567")
        cls.DECIMAL = Alphabet("0123456789")
        cls.HEXADECIMAL = Alphabet("0123456789ABCDEF")
        cls.DNA = Alphabet("ACGT")
        cls.LOWERCASE = Alphabet("abcdefghijklmnopqrstuvwxyz")
        cls.UPPERCASE = Alphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        cls.PROTEIN = Alphabet("ACDEFGHIKLMNPQRSTVWY")
        cls.BASE64 = Alphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
        cls.ASCII = Alphabet(''.join(chr(i) for i in range(128)))
        cls.EXTENDED_ASCII = Alphabet(''.join(chr(i) for i in range(256)))
        cls.UNICODE16 = Alphabet(''.join(chr(i) for i in range(65536)))

    def contains(self, char):
        """
        Check if the character is in the alphabet.

        :param char: Character to check.
        :return: True if the character exists in the alphabet, else False.
        """
        return char in self.inverse

    def radix(self):
        """Return the size of the alphabet."""
        return self.R

    def to_index(self, char):
        """
        Convert a character to its index in the alphabet.

        :param char: Character to convert.
        :return: Index of the character.
        """
        if char not in self.inverse:
            raise ValueError(f"Character '{char}' not in alphabet.")
        return self.inverse[char]

    def to_indices(self, string):
        """
        Convert a string to a list of indices.

        :param string: Input string.
        :return: List of indices.
        """
        return [self.to_index(char) for char in string]

    def to_char(self, index):
        """
        Convert an index to its corresponding character in the alphabet.

        :param index: Index to convert.
        :return: Corresponding character.
        """
        if index < 0 or index >= self.R:
            raise ValueError(f"Index {index} out of range (0 to {self.R - 1}).")
        return self.alphabet[index]

    def to_chars(self, indices):
        """
        Convert a list of indices to a string of characters.

        :param indices: List of indices.
        :return: String of corresponding characters.
        """
        return ''.join(self.to_char(index) for index in indices)

# Initialize predefined alphabets
Alphabet.initialize_predefined_alphabets()

# Example usage
if __name__ == "__main__":
    encoded1 = Alphabet.BASE64.to_indices("NowIsTheTimeForAllGoodMen")
    decoded1 = Alphabet.BASE64.to_chars(encoded1)
    print(decoded1)

    encoded2 = Alphabet.DNA.to_indices("AACGA ACGGTTTACCCCG")
    decoded2 = Alphabet.DNA.to_chars(encoded2)
    print(decoded2)

    encoded3 = Alphabet.DECIMAL.to_indices("01234567890123456789")
    decoded3 = Alphabet.DECIMAL.to_chars(encoded3)
    print(decoded3)
