# Meg Ermer
# CPTR 215 A; Lab B
# Lab 6: BaseballCounter
# History:
#	14 October 2022: Wrote some more tests, tried to make it more concise
#	13 October 2022: Did everything 
# Sources:
#	Rules of baseball:
#		https://www.reddit.com/r/explainlikeimfive/comments/vayar/eli5_the_rules_of_baseball/
#	BoundedCounter class from lecture on 7 October 2022

from enum import Enum

class HalfInning(Enum):
    TOP = 0
    BOTTOM = 1
    
class BoundedCounter:
    def __init__(self, lower_bound : int, upper_bound : int, value : int = None, neighbor : 'BoundedCounter' = None):
        """ Creates a BoundedCounter object with parameters lower_bound, upper_bound, optional value, and optional neighbor
        >>> BoundedCounter(0, 2, 1)
        BoundedCounter(0, 2, 1, None)
        >>> BoundedCounter(1, 9, 3, BoundedCounter(0, 2, 1))
        BoundedCounter(1, 9, 3, BoundedCounter(0, 2, 1, None))
        """
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.value = lower_bound if value == None else value
        self.neighbor = neighbor
        
    def __repr__(self):
        """ Returns a more comprehensible epresentation of a BoundedCounter object
        >>> c = BoundedCounter(0, 2, 1)
        >>> repr(c)
        'BoundedCounter(0, 2, 1, None)'
        >>> d = BoundedCounter(1, 9, 3, c)
        >>> repr(d)
        'BoundedCounter(1, 9, 3, BoundedCounter(0, 2, 1, None))'
        """
        return f"BoundedCounter({self.lower_bound}, {self.upper_bound}, {self.value}, {self.neighbor})"
    
    def half_key(self):
        """ Accesses the comprehensive representations of inning half values that could not be handled in the standard way.
        >>> c = BoundedCounter(HalfInning.TOP.value, HalfInning.BOTTOM.value, HalfInning.TOP.value)
        >>> c.half_key()
        'HalfInning.TOP'
        >>> c = BoundedCounter(HalfInning.TOP.value, HalfInning.BOTTOM.value, HalfInning.BOTTOM.value)
        >>> c.half_key()
        'HalfInning.BOTTOM'
        """
        if self.get_value() == 0:
            return "HalfInning.TOP"
        return "HalfInning.BOTTOM"
    
    def increment(self) -> None:
        """ Increments the counter, incrementing the neighbor if the counter value surpasses the upper limit.
        >>> c = BoundedCounter(0, 1, 0)
        >>> c.increment()
        >>> repr(c)
        'BoundedCounter(0, 1, 1, None)'
        >>> c.increment()
        >>> repr(c)
        'BoundedCounter(0, 1, 0, None)'
        >>> d = BoundedCounter(0, 1, 1, c)
        >>> d.increment()
        >>> repr(d)
        'BoundedCounter(0, 1, 0, BoundedCounter(0, 1, 1, None))'
        >>> d.increment()
        >>> repr(d)
        'BoundedCounter(0, 1, 1, BoundedCounter(0, 1, 1, None))'
        >>> d.increment()
        >>> repr(d)
        'BoundedCounter(0, 1, 0, BoundedCounter(0, 1, 0, None))'
        """
        self.value += 1
        if self.value > self.upper_bound:
            self.value = self.lower_bound
            if self.neighbor != None:
                self.neighbor.increment()
                
    def get_value(self) -> int:
        """ Accesses the value of the BoundedCounter object
        >>> c = BoundedCounter(0, 1, 0)
        >>> c.get_value()
        0
        >>> c = BoundedCounter(1, 5, 3)
        >>> c.get_value()
        3
        """
        return self.value

class BaseballCounter:
    def __init__(self, balls = 0, strikes = 0, outs = 0, half = HalfInning.TOP, inning = 1):
        """ Constructor that initializes the BaseballCounter with balls, strikes, outs, half, and inning
        >>> BaseballCounter()
        BaseballCounter(0, 0, 0, HalfInning.TOP, 1)
        >>> BaseballCounter(2, 2, 1, HalfInning.BOTTOM, 7)
        BaseballCounter(2, 2, 1, HalfInning.BOTTOM, 7)
        """
        self.balls = balls
        self.inning = BoundedCounter(1, 100, inning)
        self.half = BoundedCounter(HalfInning.TOP.value, HalfInning.BOTTOM.value, half.value, self.inning)
        self.outs = BoundedCounter(0, 2, outs, self.half)
        self.strikes = BoundedCounter(0, 2, strikes, self.outs)
    
    def __repr__(self):
        """ Returns a more comprehensive representation of a BaseballCounter object
        >>> repr(BaseballCounter())
        'BaseballCounter(0, 0, 0, HalfInning.TOP, 1)'
        >>> repr(BaseballCounter(2, 2, 1, HalfInning.BOTTOM, 7))
        'BaseballCounter(2, 2, 1, HalfInning.BOTTOM, 7)'
        """
        return f'BaseballCounter({self.balls}, {self.strikes.get_value()}, {self.outs.get_value()}, {self.half.half_key()}, {self.inning.get_value()})'
    
    def __str__(self):
        """ Returns a human readable string representation of a BaseballCounter object
        >>> print(BaseballCounter())
        0 balls, 0 strikes, 0 outs, top of the 1st inning
        >>> print(BaseballCounter(2, 2, 1, HalfInning.BOTTOM, 7))
        2 balls, 2 strikes, 1 out, bottom of the 7th inning
        """
        balls = f"{self.balls} ball, " if self.balls == 1 else f"{self.balls} balls, "
        strikes = f"{self.strikes.get_value()} strike, " if self.strikes.get_value() == 1 else f"{self.strikes.get_value()} strikes, "
        outs = f"{self.outs.get_value()} out, " if self.outs.get_value() == 1 else f"{self.outs.get_value()} outs, "
        half = f"top of the " if self.half.value == HalfInning.TOP.value else f"bottom of the "
        inning = f"{self.inning.get_value()}st inning" if self.inning.get_value() == 1 else f"{self.inning.get_value()}nd inning" if self.inning.get_value() == 2 else f"{self.inning.get_value()}rd inning" if self.inning.get_value() == 3 else f"{self.inning.get_value()}th inning"
        return balls + strikes + outs + half + inning
    
    def new_batter(self):
        """ Resets balls and strikes
        >>> bc = BaseballCounter(2, 2, 1, HalfInning.BOTTOM, 7)
        >>> bc.new_batter()
        >>> repr(bc)
        'BaseballCounter(0, 0, 1, HalfInning.BOTTOM, 7)'
        >>> bc = BaseballCounter(3, 2, 2, HalfInning.TOP, 3)
        >>> bc.new_batter()
        >>> repr(bc)
        'BaseballCounter(0, 0, 2, HalfInning.TOP, 3)'
        """
        self.balls = 0
        self.strikes = BoundedCounter(0, 2, 0, self.outs)
        
    def ball(self):
        """ Counts a ball, and resets when the 4th ball is counted
        >>> bc = BaseballCounter(3, 2, 2, HalfInning.TOP, 3)
        >>> bc.ball()
        >>> repr(bc)
        'BaseballCounter(0, 0, 2, HalfInning.TOP, 3)'
        >>> bc = BaseballCounter()
        >>> bc.ball()
        >>> repr(bc)
        'BaseballCounter(1, 0, 0, HalfInning.TOP, 1)'
        """
        self.balls += 1
        if self.balls > 3:
            self.new_batter()
    
    def strike(self):
        """ Counts a strike. The 3rd strike makes an out.
        >>> bc = BaseballCounter()
        >>> bc.strike()
        >>> repr(bc)
        'BaseballCounter(0, 1, 0, HalfInning.TOP, 1)'
        >>> bc = BaseballCounter(3, 2, 1, HalfInning.BOTTOM, 7)
        >>> bc.strike()
        >>> repr(bc)
        'BaseballCounter(0, 0, 2, HalfInning.BOTTOM, 7)'
        """
        if self.strikes.get_value() < 2:
            self.strikes.increment()
        else:
            self.strikes.increment()
            self.new_batter()            
    
    def out(self):
        """ Counts an out. The 3rd out switches to the other half of the inning.
        >>> bc = BaseballCounter()
        >>> bc.out()
        >>> repr(bc)
        'BaseballCounter(0, 0, 1, HalfInning.TOP, 1)'
        >>> bc = BaseballCounter(1, 2, 2, HalfInning.BOTTOM, 3)
        >>> bc.out()
        >>> repr(bc)
        'BaseballCounter(0, 0, 0, HalfInning.TOP, 4)'
        """
        if self.outs.get_value() < 2:
            self.outs.increment()
        else:
            self.outs.increment()
            self.new_batter()
    
    def new_game(self):
        """ Resets everything for the next game.
        >>> bc = BaseballCounter(1, 2, 2, HalfInning.BOTTOM, 3)
        >>> bc.new_game()
        >>> repr(bc)
        'BaseballCounter(0, 0, 0, HalfInning.TOP, 1)'
        >>> bc = BaseballCounter(3, 1, 2, HalfInning.TOP, 9)
        >>> bc.new_game()
        >>> repr(bc)
        'BaseballCounter(0, 0, 0, HalfInning.TOP, 1)'
        """
        self.balls = 0
        self.inning = BoundedCounter(1, 100, 1)
        self.half = BoundedCounter(HalfInning.TOP.value, HalfInning.BOTTOM.value, HalfInning.TOP.value, self.inning)
        self.outs = BoundedCounter(0, 2, 0, self.half)
        self.strikes = BoundedCounter(0, 2, 0, self.outs)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    
