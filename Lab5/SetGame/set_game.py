# Meg Ermer
# CPTR 215 A
# History:
#	5 October: Wrote doctests, condensed loops into list comprehensions, made it cute
#	3 October: Wrote the code, got it to work, it does not look cute but it gets the job done
# Sources:
#	https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/
#		-Used for learning about list comprehensions

from enum import Enum
from queue import Empty
import random

class Fill(Enum):
    EMPTY = 0
    SHADED = 1
    FILLED = 2
    
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Shape(Enum):
    QUAD = 5
    OVAL = 17
    PYRAMID = 234

class SetCard:
    def __init__(self, number, fill, color, shape):
        '''int in [1,3], Fill, Color, Shape -> SetCard
        >>> SetCard(2, Fill.EMPTY, Color.BLUE, Shape.OVAL)
        SetCard(2, Fill.EMPTY, Color.BLUE, Shape.OVAL)
        >>> SetCard(3, Fill.SHADED, Color.RED, Shape.PYRAMID)
        SetCard(3, Fill.SHADED, Color.RED, Shape.PYRAMID)
        '''
        self.number = number
        self.fill = fill
        self.color = color
        self.shape = shape
    def __str__(self):
        '''Human-readable representation of this card.
        >>> str(SetCard(1, Fill.SHADED, Color.BLUE, Shape.OVAL))
        '1SBO'
        >>> str(SetCard(2, Fill.EMPTY, Color.RED, Shape.QUAD))
        '2ERQ'
        '''
        return f"{self.number}{self.fill.name[0]}{self.color.name[0]}{self.shape.name[0]}"
        
    def __repr__(self):
        '''Python code to recreate this card.
        >>> SetCard(1, Fill.SHADED, Color.BLUE, Shape.OVAL)
        SetCard(1, Fill.SHADED, Color.BLUE, Shape.OVAL)
        >>> repr(SetCard(2,Fill.EMPTY,Color.RED,Shape.QUAD))
        'SetCard(2, Fill.EMPTY, Color.RED, Shape.QUAD)'
        '''
        return f"SetCard({self.number}, {self.fill}, {self.color}, {self.shape})"

    def third_card(self, other):
        '''Returns the third card that makes a set with self and other.
        >>> card1 = SetCard(2, Fill.EMPTY, Color.RED, Shape.QUAD)
        >>> card2 = SetCard(1, Fill.SHADED, Color.BLUE, Shape.OVAL)
        >>> print(card1.third_card(card2))
        3FGP
        >>> print(card2.third_card(card1))
        3FGP
        >>> card1 = SetCard(1, Fill.EMPTY, Color.GREEN, Shape.QUAD)
        >>> card2 = SetCard(1, Fill.EMPTY, Color.RED, Shape.OVAL)
        >>> print(card1.third_card(card2))
        1EBP
        >>> card1 = SetCard(2, Fill.SHADED, Color.GREEN, Shape.QUAD)
        >>> card2 = SetCard(1, Fill.EMPTY, Color.GREEN, Shape.QUAD)
        >>> print(card1.third_card(card2))
        3FGQ
        '''
        card1 = self
        card2 = other
        card3 = SetCard(1, Fill.EMPTY, Color.GREEN, Shape.QUAD)
        if card1.number == card2.number:
            card3.number = card1.number
        else:
            numberSet = {1, 2, 3}
            card3.number = list(numberSet - {card1.number} - {card2.number})[0]
        if card1.fill == card2.fill:
            card3.fill = card1.fill
        else:
            card3.fill = list(set(Fill) - {card1.fill} - {card2.fill})[0]
        if card1.color == card2.color:
            card3.color = card1.color
        else:
            card3.color = list(set(Color) - {card1.color} - {card2.color})[0]
        if card1.shape == card2.shape:
            card3.shape = card1.shape
        else: card3.shape = list(set(Shape) - {card1.shape} - {card2.shape})[0]
        return card3

def make_deck():
    '''Returns a list containing a complete Set deck with 81 unique cards.
    >>> len(make_deck())
    81
    >>> print(type(make_deck()))
    <class 'list'>
    >>> len([card for card in make_deck() if card.fill == Fill.EMPTY])
    27
    >>> len([card for card in make_deck() if card.color == Color.GREEN])
    27
    '''    
    numberList = [1, 2, 3]
    fillList = list(Fill)
    colorList = list(Color)
    shapeList = list(Shape)
    deck = []
    [[[[deck.append(SetCard(num, fill, color, shape)) for shape in shapeList] for color in colorList] for fill in fillList] for num in numberList]
    random.shuffle(deck)
    return deck

def is_set(card1, card2, card3):
    '''Determines whether the 3 cards make a set.
    (For each of the 4 traits, all 3 cards are either the same, or all 3 are different.)
    >>> card1 = SetCard(3, Fill.FILLED, Color.GREEN, Shape.QUAD)
    >>> card2 = SetCard(2, Fill.FILLED, Color.GREEN, Shape.QUAD)
    >>> card3 = SetCard(2, Fill.EMPTY, Color.GREEN, Shape.QUAD)
    >>> is_set(card1, card2, card3)
    False
    >>> card1 = SetCard(2, Fill.FILLED, Color.BLUE, Shape.QUAD)
    >>> card2 = SetCard(1, Fill.FILLED, Color.BLUE, Shape.OVAL)
    >>> card3 = SetCard(3, Fill.FILLED, Color.BLUE, Shape.PYRAMID)
    >>> is_set(card1, card2, card3)
    True
    '''
    return str(card1.third_card(card2)) == str(card3)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()