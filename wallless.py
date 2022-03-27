from base import AStar, Position

class WalllessAStar(AStar):
    __slots__ = ("width", "height")

    def __init__(self, width : int, height : int):
        self.width = width
        self.height = height
        pass

    def g(self, pos : Position) -> float:
        return abs(pos - self.start)

    def h(self, pos : Position) -> float:
        return abs(self.goal - pos)

    def get_neighbors(self, pos : Position) -> tuple[Position]:
        neighbors = []
        for offset in [Position(x,y) for y in range(-1,2) for x in range(-1,2) if not(x==y==0)]:
            new_pos = pos + offset
            if new_pos.x < 0 or new_pos.y < 0 or new_pos.x >= self.width or new_pos.y >= self.height: continue
            neighbors.append(new_pos)
            pass

        return tuple(neighbors)
        pass
    pass

if __name__ == "__main__":
    algorithm = WalllessAStar()
    start, stop = Position(0,0),Position(4,5)
    print(algorithm.evaluate(start,stop))
    pass