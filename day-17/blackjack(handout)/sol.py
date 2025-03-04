class Card:
    def __init__(self, card):
        self.card = card

    def get_value(self):
        return self.card

    def display_card(self):
        print(self.card, end=" ")

class Deck:
    def __init__(self, cards):
        self.cards = cards
        self.current_index = 0

    def draw_card(self):
        if self.current_index < len(self.cards):
            card = self.cards[self.current_index]
            self.current_index += 1
            return card
        return None

    def reset_deck(self):
        self.current_index = 0

class Hand:
    def __init__(self, cards_in_hand):
        self.cards_in_hand = cards_in_hand
        self.total_value = 0

    def add_card(self, card):
        self.cards_in_hand.append(card)

    def calculate_score(self):
        self.total_value = 0
        ace_count = 0
        for card in self.cards_in_hand:
            if card.get_value() == 1:
                ace_count += 1
                self.total_value += 11
            else:
                self.total_value += card.get_value()

        while self.total_value > 21 and ace_count > 0:
            self.total_value -= 10
            ace_count -= 1

    def get_total_value(self):
        return self.total_value

    def display_hand(self):
        for card in self.cards_in_hand:
            card.display_card()
        print()

    def is_blackjack(self):
        if self.total_value == 21 and len(self.cards_in_hand) == 2:
            return True
        else:
            return False

    def is_busted(self):
        
        if self.total_value > 21:
            return True
        else:
            return False

class Player:
    def __init__(self, hand):
        self.hand = hand
        self.varstand = False

    def hit(self, deck):
        self.hand.add_card(deck.draw_card())
        self.hand.calculate_score()

    def stand(self):
        self.varstand = True

    def get_score(self):
        return self.hand.get_total_value()

    def has_blackjack(self):
        return self.hand.is_blackjack()

    def has_busted(self):
        return self.hand.is_busted()

    def display_hand(self):
        self.hand.display_hand()

class Dealer:
    def __init__(self, hand):
        self.hand = hand

    def hit(self, deck):
        self.hand.add_card(deck.draw_card())
        self.hand.calculate_score()

    def play_turn(self, s, deck):
        l = s

        if l == "h":
            self.hit(deck)
            print("Dealer chooses to hit. (h/s): ", end="")
            self.display_hand()
            print(f"Dealer's total score: {self.get_score()}")
            return

    def get_score(self):
        return self.hand.get_total_value()

    def has_blackjack(self):
        return self.hand.is_blackjack()

    def has_busted(self):
        return self.hand.is_busted()

    def display_hand(self):
        self.hand.display_hand()

class Game:
    def __init__(self):
        cards = [Card(7)]
        for i in range(1, 7):
            cards.append(Card(i))
        self.deck = Deck(cards)
        self.player = Player(Hand([]))
        self.dealer = Dealer(Hand([]))

    def start_game(self):
        print("Game starts:")
        print("Player's turn:")
        self.player.hit(self.deck)
        self.player.hit(self.deck)
        self.dealer.hit(self.deck)
        self.dealer.hit(self.deck)
        self.player.display_hand()
        print(f"Your total score: {self.player.get_score()}")

    def player_turn(self, s):
        if not self.player.varstand:
            l = s
            if l == "s":
                self.player.stand()
                print("Do you want to hit or stand? (h/s): Dealer's turn:")
                self.dealer.display_hand()
                print(f"Dealer's total score: {self.dealer.get_score()}")
                return

            self.player.hit(self.deck)
            if self.player.get_score() > 21:
                return
            print("Do you want to hit or stand? (h/s): Player's turn:")
            self.player.display_hand()
            print(f"Your total score: {self.player.get_score()}")

    def dealer_turn(self, s):
        self.dealer.play_turn(s, self.deck)

    def determine_winner(self):
        if self.player.has_busted():
            print("Do you want to hit or stand? (h/s): Player busts!")
            print("Player's hand: ")
            self.player.display_hand()
            print("Player has busted!")
            return

        if self.dealer.has_busted():
            print("Final results:")
            self.player.display_hand()
            self.dealer.display_hand()
            print("Dealer has busted!")
            return

        if self.player.get_score() > self.dealer.get_score():
            print("Dealer chooses to hit. (h/s): Dealer's final hand: ")
            self.dealer.display_hand()
            print(f"Dealer's total score: {self.dealer.get_score()}")
            print()
            print("Final results:")
            self.player.display_hand()
            self.dealer.display_hand()
            print("Player wins!")
            return

        if self.player.get_score() < self.dealer.get_score():
            print()
            print("Final results:")
            self.player.display_hand()
            self.dealer.display_hand()
            print("Dealer wins!")
            return 

    def play_game(self):
        self.start_game()

        while True:
            try:
                s = input()
                self.player_turn(s)
                if(self.player.varstand):
                    self.dealer_turn(s)
                if(self.player.has_busted()):
                    self.determine_winner()
                    return
            except:
                self.determine_winner()
                break





def main():
    game = Game()
    
    game.play_game()

if __name__ == "__main__":
    main()
