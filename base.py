from typing import Any, Optional
import math

class Position:
    __slots__ = ("_x","_y")

    def __init__(self,x : int, y : int):
        self._x = x
        self._y = y
        pass


    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __getitem__(self, index) -> int:
        if index == 0: return self._x
        elif index == 1: return self._y
        else: raise IndexError("Index out of range")
        pass

    def __add__(self, other):
        return self.__class__(self._x + other._x, self._y + other._y)
        pass

    def __sub__(self, other):
        return self.__class__(self._x - other._x, self._y - other._y)
        pass

    def __abs__(self):
        return math.sqrt(self._x**2 + self._y**2)
        pass

    def __eq__(self,other):
        return self._x == other._x and self._y == other._y
    def __neq__(self,other):
        return self._x != other._x or self._y != other._y

    def __str__(self) -> str:
        return f"({self._x},{self._y})"
        pass
    def __repr__(self) -> str:
        return f"<Position ({self._x},{self._y})>"
        pass

    def __hash__(self) -> int:
        return hash((self._x,self._y)) # This is a bad hash function, but I can't figure out a better way
        pass
    pass

class Board:
    __slots__ = ("board","_width","_height")

    def __init__(self, width : int, height : int):
        self.board : list[list[Any]] = [[None for y in range(height)] for x in range(width)]
        self._width = width
        self._height = height
        pass

    @classmethod
    def from_list(cls, raw_board : list[list[Any]]):
        self = cls(len(raw_board),len(raw_board[0]))
        self.board = raw_board

        return self
        pass

    @property
    def width(self): return self._width
    @property
    def height(self): return self._height

    def __getitem__(self, index) -> Any:
        return self.board[index[0]][index[1]]
        pass

    def __setitem__(self, index, value):
        self.board[index[0]][index[1]] = value
        pass
    pass

class AStar:
    __slots__ = ("start","goal")

    def g(self, pos) -> float:
        raise NotImplementedError("method g never implemented. Override this method when inheriting from AStar")
        pass

    def h(self, pos) -> float:
        raise NotImplementedError("method h never implemented. Override this method when inheriting from AStar")
        pass

    def get_neighbors(self, pos) -> tuple[Any]:
        raise NotImplementedError("method get_neighbors never implemented. Override this method when inheriting from AStar")
        pass

    def __init__(self):
        self.start : Optional[int] = None
        self.goal  : Optional[int] = None
        pass

    def evaluate(self, start, goal) -> tuple:
        f = lambda node: self.g(node) + self.h(node)

        self.start, self.goal = start, goal

        OPEN = set()
        CLOSE= set()
        PARENTS = dict()

        OPEN.add((self.start,f(self.start)))
        PARENTS[start] = start
        while True:
            active_node, cost = min(OPEN,key=lambda data: data[1]) # Find open node with smallest f
            if active_node == goal: # If node is goal, finish
                del cost
                break

            OPEN.remove((active_node,cost)) # Remove node from OPEN
            if active_node in CLOSE: continue # Don't retread paths
            del cost
            neighbors = self.get_neighbors(active_node) # Find neighbors of active_node
            for pos in neighbors: # Add all neighbors to OPEN and calculate their f-value
                if pos in CLOSE: continue # DO NOT RETREAD!
                OPEN.add((pos,f(pos)))
                if pos not in PARENTS.keys() or self.h(PARENTS[pos]) > self.h(active_node): # Only replace a parent if this new parent has a better g (i.e. )
                    PARENTS[pos] = active_node
                pass
            del pos, neighbors
            CLOSE.add(active_node)

            del active_node
            pass

        
        path = []
        # Descend parent ladder
        while PARENTS[active_node] != active_node:
            path.append(active_node)
            active_node = PARENTS[active_node]
            pass
        path.append(start)
        path.reverse()
        return path
        pass
    pass