import random

class Card:
    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def displayCard(self):
        print(self.value, end=" ")

class Deck:
    def __init__(self):
        self.cards = [7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.currentIndex = 0

    def drawCard(self):
        if self.currentIndex < len(self.cards):
            card = self.cards[self.currentIndex]
            self.currentIndex += 1
            return Card(card)
        return None

    def resetDeck(self):
        self.currentIndex = 0

class Hand:
    def __init__(self):
        self.cardsInHand = []
        self.totalValue = 0

    def addCard(self, card):
        self.cardsInHand.append(card)
        self.calculateScore()

    def calculateScore(self):
        self.totalValue = 0
        ace_count = 0
        for i in range(len(self.cardsInHand)):
            card_value = self.cardsInHand[i].getValue()
            if card_value == 1:
                ace_count += 1
            self.totalValue += card_value
        while ace_count > 0 and self.totalValue + 11 <= 21:
            self.totalValue += 11
            ace_count -= 1

    def getTotalValue(self):
        return self.totalValue

    def displayHand(self):
        for i in range(len(self.cardsInHand)):
            self.cardsInHand[i].displayCard()
        print()

    def hasBusted(self):
        return self.totalValue > 21

class Player:
    def __init__(self):
        self.hand = Hand()

    def hit(self, deck):
        card = deck.drawCard()
        if card:
            self.hand.addCard(card)

    def getScore(self):
        return self.hand.getTotalValue()

    def hasBusted(self):
        return self.hand.hasBusted()

    def displayHand(self):
        self.hand.displayHand()

class Dealer:
    def __init__(self):
        self.hand = Hand()

    def hit(self, deck):
        card = deck.drawCard()
        if card:
            self.hand.addCard(card)

    def playTurn(self, deck):
        while self.hand.getTotalValue() < 17:
            print("Dealer chooses to hit. (h/s):", end=" ")
            self.hit(deck)
            self.displayHand()
            print("Dealer's total score:", self.getScore())
        print("Dealer's final hand:")
        self.displayHand()
        print("Dealer's total score:", self.getScore())

    def getScore(self):
        return self.hand.getTotalValue()

    def displayHand(self):
        self.hand.displayHand()

    def hasBusted(self):
        return self.hand.hasBusted()

class Game:
    def __init__(self, moves):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.moves = moves

    def startGame(self):
        self.deck.resetDeck()
        self.player.hit(self.deck)
        self.player.hit(self.deck)
        self.dealer.hit(self.deck)
        self.dealer.hit(self.deck)
        print("Game starts:")

    def playerTurn(self):
        move_index = 0
        while move_index < len(self.moves):
            print("Player's turn:")
            self.player.displayHand()
            print("Your total score:", self.player.getScore())
            print("Do you want to hit or stand? (h/s):", end=" ")
            move = self.moves[move_index].lower()
            move_index += 1
            if move == "h":
                self.player.hit(self.deck)
                if self.player.hasBusted():
                    print("You Busted!")
                    break
            elif move == "s":
                break

    def dealerTurn(self):
        print("Dealer's turn:")
        self.dealer.displayHand()
        print("Dealer's total score:", self.dealer.getScore())
        self.dealer.playTurn(self.deck)

    def determineWinner(self):
        print("\nFinal results:")
        self.player.displayHand()
        self.dealer.displayHand()
        player_score = self.player.getScore()
        dealer_score = self.dealer.getScore()

        if self.player.hasBusted():
            print("Dealer wins!")
        elif self.dealer.hasBusted() or player_score > dealer_score:
            print("Player wins!")
        elif player_score < dealer_score:
            print("Dealer wins!")
        else:
            print("It's a tie!")

    def playGame(self):
        self.startGame()
        self.playerTurn()
        if not self.player.hasBusted():
            self.dealerTurn()
        self.determineWinner()

if __name__ == "__main__":
    moves = []
    while True:
        try:
            move = input().strip()
            if move not in ['h', 's']:
                break
            moves.append(move)
        except EOFError:
            break
    game = Game(moves)
    game.playGame()
