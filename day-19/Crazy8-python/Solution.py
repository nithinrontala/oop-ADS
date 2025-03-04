# Card Class
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        # self.cards = []
    
    def getSuit(self):
        return self.suit
    
    def getRank(self):
        return self.rank
    
    def matches(self,card):
        if self.rank == card.rank or self.suit == card.suit:
            return True
        return False
    

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Deck Class (without using random.shuffle)
class Deck:
    def __init__(self):
        # your code goes here
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        for i in range(len(suits)):
            for j in range(len(ranks)):
                self.cards.append(Card(suits[i], ranks[j]))

        self.manual_shuffle()
    
    def draw_card(self):
        a = self.cards.pop(0)
        return a

    def manual_shuffle(self):
        """Manually shuffle the deck without using random"""
        shuffled = []
        while len(self.cards) > 0:
            mid = len(self.cards) // 2  # Pick a middle point
            shuffled.append(self.cards.pop(mid))  # Move card to shuffled deck
        self.cards = shuffled

# Hand Class
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self,card):
        self.cards.append(card)
        
    def remove_card(self,card):
        for i in self.cards:
            if i.matches(card):
                # print(len(self.cards))
                self.cards.remove(i)
                # print(len(self.cards))
        return self.cards
    
    def has_card(self):
        if len(self.cards) == 0:
            return True
        return False
    
    def play_card(self,card):
        for i in self.cards:
            if i.matches(card):
                self.cards.remove(i)
                return i   

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

# Player Class
class Player:
    def __init__(self,name):
        self.name = name
        self.hand = Hand()
        self.isHuman = False

    def draw_card(self,deck):
        card = deck.draw_card()
        if card:
            self.hand.add_card(card)

    def play_turn(self,top_card,deck):
        card_to_play = self.hand.play_card(top_card)
        if card_to_play:
            # self.hand.remove_card(card_to_play)
            return card_to_play
        else:
            # self.draw_card(deck)  
            return None 
        
    def has_won(self):
        return len(self.hand.cards) == 0

    def __str__(self):
        return f"{self.name}: {self.hand}"

# Game Class
class Game:
    def __init__(self,numplayers):
        self.numPlayers = numplayers
        self.players = []
        self.currentPlayer = 0
        self.deck = Deck()
        self.top_card = self.deck.draw_card()
    
    
    def start_game(self):
        player_1 = Player("Player 1")
        player_2 = Player("Player 2")
        for i in range(6,11):
            player_1.draw_card((self.deck))
        for j in range(0,5):
            player_2.draw_card((self.deck))
        self.players.append(player_1)
        self.players.append(player_2)
        
        
    def play_game(self):
        self.start_game()   
        print()
        while True:
            currentPlayer = self.players[self.currentPlayer]
            
            play = currentPlayer.play_turn(self.top_card,self.deck)
            if play:
                print(f"{currentPlayer.name}'s Turn. Top Card: {self.top_card}")
                print(f"{currentPlayer.name} played: {play}")
                self.top_card = play
                if currentPlayer.has_won():
                    print()
                    print(f"{currentPlayer.name} wins the game!")
                    break
            else:
                print(f"{currentPlayer.name}'s Turn. Top Card: {self.top_card}")
                currentPlayer.draw_card(self.deck)
                print(f"{currentPlayer.name} had to draw a card.")
            self.currentPlayer = (self.currentPlayer + 1) % self.numPlayers
            print()


