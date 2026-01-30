"""
Example 1-1 is a class to represent a deck of playing cards.
"""

import collections

Card = collections.namedtuple("Card", ["rank", "suit"])

class FrenchDeck:
  ranks = [str(n) for n in range(2, 11)] + list('JQKA')
  suits = 'spades diamonds clubs hearts'.split()

  def __init__(self):
    self._cards = [Card(rank, suit) for suit in self.suits
                                    for rank in self.ranks]

  def __len__(self):
    return len(self._cards)

  def __getitem__(self, position):
    return self._cards[position]

def main():
  beer_card = Card("7", "diamonds")
  print(f"Highlighting collections.namedtuple: {beer_card}")

  deck = FrenchDeck()
  print(f"len(deck): {len(deck)}")

  print(f"First item in the deck: {deck[0]}, last item in the deck: {deck[-1]}.")
  print("\n")

  from random import choice
  print(f"Randomly selected card: {choice(deck)}")
  print("\n")

  print("Slicing")
  print(f"Top 3 cards: {deck[:3]}")
  print(f"Top 5 cards: {deck[:5]}")
  print("\n")
  print(f"Pick the aces by starting on index 12 and skipping 13 cards at a time:\n {deck[12::13]}")
  print("\n")

  print("Iterating over our deck:")
  for card in deck:
    print(f"  {card}")

  print("\n")
  print("Iterating over our deck in reverse:")
  for card in reversed(deck):
    print(f"  {card}")
  print("\n")

  print("Iterating over our FrenchDeck")
  print(f"Card('Q', 'hearts') in deck: {Card('Q', 'hearts') in deck}")
  print(f"Card('8', 'eats) in deck: {Card('8', 'eats') in deck}")

if __name__ == '__main__':
  main()
