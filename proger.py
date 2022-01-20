import random

class DeckOfCards:
    deck = [None] * 36
    def __init__(self):
        x = 0;
        for i in range(1, 4 + 1):
            for j in range(6, 14 + 1):
                self.deck[x] = Card(i, j)
                x += 1;
    def shuffle(self):
        random.shuffle(self.deck)
    def get(self, i):
        try:
            answer = {
                11: "Валет",
                12: "Дама",
                13: "Король",
                14: "Туз",
            }[self.deck[i].Num]
        except:
            answer = str(self.deck[i].Num)
        answer += " "
        answer += {
            1: "червей",
            2: "бубей",
            3: "крестей",
            4: "пик",
        }[self.deck[i].Mastb]
        return answer
class Card():
    def __init__(self, i, j):
        self.Mastb = i
        self.Num   = j

if __name__ == '__main__':
    deck = DeckOfCards()
    deck.shuffle()
    print(deck.get(-1))
















# import random 
 
# class Card:
    
#     def __init__(self, suit, rank):
#         self.suit = suit 
#         self.rank = rank
        
#     def info_rank(self):
#          return self.rank
 
#     def __str__(self):
#         return f'{self.rank} {self.suit}'
 
 
# class Deck:
    
#     def __init__(self, cards):
#         self.cards = cards
 
#     def deck_info(self):
#         for card in self.cards:
#             print(card)
 
#     def mix_card(self):
#         random.shuffle(self.cards)
 
#     def one_card(self):
#         if not self.cards:
#             return 'no card'
#         return random.choice(self.cards)
    
#     def six_card(self):
#         return [self.one_card() for _ in range(6)]
 
 
# rank = ['Туз', 'Король','Дама','Валет','10','9','8','7','6',]
# suit = ["червей","бубей","крестей","пик" ]
# cards = [Card(s,r) for s in suit for r in rank] # возможно это в классе Deck нужно выполнить
 
 
# deck = Deck(cards)
# print('колода')
# deck.deck_info()
# deck.mix_card()
# print()
# print('перемешанная колода')
# deck.deck_info()
# print()
# print('выдача одной карты')
# print(deck.one_card())
# print()
# print('выдача 6 карт')
# for card in deck.six_card():
#     print(card)








# import random

# class card_deck:
#     def __init__(self, rank, suite, card):


#         self.rank= rank
#         self.suite = suite
#     def ranks(self):
#         return self.rank
#     def suites(self):
#         return self.suite
#     def cards(self,card):
#         suit_name= ['The suit of Spades','The suit of Hearts', 'The suit of Diamonds','Clubs']
#         rank_name=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']


#     def value(self):
#         if self.rank == 'Ace':
#             return 1
#         elif self.rank == 'Jack':
#             return 11
#         elif self.rank == 'Queen':
#             return 12
#         elif self.rank == 'King':
#             return 13
#     def shffule(self):
#         random.shuffle(self.cards)
#     def remove(self,card):
#         self.cards.remove(card)


#     def cardremaining(self):
#         self.suite-self.rank


# def main():
#     try:
#         deck=[]
#         for i in ['Spades','Hearts', ' Diamonds','Clubs']:
#             for c in ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']:
#                 deck.append((c, i))
#         deck.shffule

#         hand = []
#         user =eval(input('Enter a number of cards: 1-7 '))
#         print()
#         while user <1 or user >7:
#             print ("Only a number between 1-7:")
#             return main()

#         for i in range(user):
#             hand.append(deck[i]) 
#         print (hand)
#     except ValueError:
#         print("Only numbers")
#         main()

# trial = card_deck(4,2,1)
# print(trial.ranks)



















# from collections import namedtuple

# Card = namedtuple('Card', 'sign, value')  #  no need to write class to represent card
# SIGNS = ['Hearts', 'Diamonds', 'Spades', 'Clubs']


# class Deck:
#     def __init__(self):
#         self.cards = [Card(sign, value) for sign in SIGNS for value in range(2,
#                                                                              11) +
#                       'J Q K A'.split()]

#     def __repr__(self):
#         return str([str(card) for card in self.cards])

#     def __len__(self):
#         return len(self.cards)

#     def __getitem__(self, item):
#         return self.cards[item]

#     def __setitem__(self, key, value):
#         self.cards[key] = value


# deck = Deck()

# print(deck[11])  # indexing works, prints Card(sign='Hearts', value='K')

# print(len(deck))  # prints 52

# print(deck[13:16])  # slicing works

# import random

# random.shuffle(deck)  # shuffle works using no extra code















