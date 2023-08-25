# Meg Ermer
# CPTR 215 A
# History:
#	5 October: Wrote doctests, condensed loops into list comprehensions, made it cute
#	2 October: Wrote code, got all functions passing
# Sources:
#	https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/
#		-Used for learning about list comprehensions
import random

class UnoCard:
    def __init__(self, color, rank):
        """
        >>> UnoCard('G', '7')
        UnoCard('G', '7')
        >>> UnoCard('K', 'F')
        UnoCard('K', 'F')
        """
        self.color = color
        self.rank = rank
        
    def __str__(self):
        """
        >>> print(UnoCard('R', '3'))
        R3
        >>> print(UnoCard('K', 'W'))
        KW
        """
        return f"{self.color}{self.rank}"
    
    def __repr__(self):
        """
        >>> repr(UnoCard('R', '9'))
        "UnoCard('R', '9')"
        >>> repr(UnoCard('G', '7'))
        "UnoCard('G', '7')"
        """
        return f"UnoCard('{self.color}', '{self.rank}')"
    
    def can_be_played_on(self, other):
        """
        >>> card1 = UnoCard('G', '8')
        >>> card2 = UnoCard('G', '7')
        >>> card1.can_be_played_on(card2)
        True
        >>> card3 = UnoCard('B', '7')
        >>> card2.can_be_played_on(card3)
        True
        >>> card4 = UnoCard('K', 'W')
        >>> card4.can_be_played_on(card1)
        True
        >>> card1.can_be_played_on(card3)
        False
        """
        if (self.color == other.color) or (self.rank == other.rank) or (self.rank == 'W') or (self.rank == 'F'): # anything can be played on black and 
            return True
        return False
  
    def score_value(self):
        """
        >>> card1 = UnoCard('B', '7')
        >>> card1.score_value()
        7
        >>> card2 = UnoCard('K', 'F')
        >>> card2.score_value()
        50
        """
        card_vals = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'S': 20,
            'D': 20,
            'R': 20,
            'W': 50,
            'F': 50
        }
        return (card_vals[self.rank])
    
def create_deck():
    """
    >>> deck = create_deck()
    >>> print(len(deck))
    108
    >>> type(create_deck())
    <class 'list'>
    >>> len([card for card in deck if card.color == "G"])
    25
    >>> all([len([card for card in deck if card.rank == rank])== 8 for rank in "123456789SDR"])
    True
    """
    normal_color_list = ['R', 'G', 'B', 'Y']
    color_card_rank_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'S', 'D', 'R']
    black_card_rank_list = ['W', 'F']
    deck = []
    [[[deck.append(UnoCard(color, rank)) for i in range(2)] for rank in color_card_rank_list] for color in normal_color_list]
    [[deck.append(UnoCard('K', rank)) for i in range(4)] for rank in black_card_rank_list]
    [deck.append(UnoCard(color, '0')) for color in normal_color_list]
    random.shuffle(deck)
    return deck

def deal_hands(deck, num_hands):
    """
    >>> game = deal_hands(create_deck(), 3)
    >>> print(len(game))
    3
    >>> print(len(game[0]))
    7
    >>> print(type(game))
    <class 'tuple'>
    """
    hands = []
    [hands.append([]) for i in range(num_hands)]
    [[(hands[k].append(deck.pop(0))) for k in range(num_hands)] for j in range(7)]
    return tuple(hands)

def hand_score(hand):
    """
    >>> hand = [UnoCard('Y', '6'), UnoCard('G', '7'), UnoCard('R', '9'), UnoCard('B', '2'), UnoCard('B', 'R'), UnoCard('R', '4'), UnoCard('G', 'R')]
    >>> print(hand_score(hand))
    68
    >>> hand2 = [UnoCard('R', '3'), UnoCard('K', 'F'), UnoCard('Y', '9'), UnoCard('Y', 'R'), UnoCard('B', '6'), UnoCard('B', '4'), UnoCard('R', '8')]
    >>> print(hand_score(hand2))
    100
    """
    return sum([card.score_value() for card in hand])
            
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    
    
    
    