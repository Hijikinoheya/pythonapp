import random

# カードのデッキを作成
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# カードクラスの定義
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# デッキクラスの定義
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

# 手札クラスの定義
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# プレイヤークラスの定義
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def __str__(self):
        return f"{self.name}'s hand: {', '.join(map(str, self.hand.cards))}. Value: {self.hand.value}"

# ゲームのメインロジック
def blackjack():
    print("Welcome to Blackjack!")

    deck = Deck()
    deck.shuffle()

    player_name = input("Enter your name: ")
    player = Player(player_name)
    dealer = Player("Dealer")

    # 初期の手札を配る
    for _ in range(2):
        player.hand.add_card(deck.deal())
        dealer.hand.add_card(deck.deal())

    print(player)
    print(dealer)

    # プレイヤーのターン
    while player.hand.value < 21:
        action = input("Do you want to hit or stand? (h/s): ").lower()
        if action == 'h':
            player.hand.add_card(deck.deal())
            print(player)
        elif action == 's':
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.")

    # ディーラーのターン
    while dealer.hand.value < 17:
        dealer.hand.add_card(deck.deal())

    # 結果の表示
    print("\nFinal hands:")
    print(player)
    print(dealer)

    if player.hand.value > 21:
        print("You bust! Dealer wins.")
    elif dealer.hand.value > 21:
        print("Dealer busts! You win.")
    elif player.hand.value > dealer.hand.value:
        print("You win!")
    elif player.hand.value < dealer.hand.value:
        print("Dealer wins.")
    else:
        print("It's a tie!")

# ゲームの実行
if __name__ == "__main__":
    blackjack()
