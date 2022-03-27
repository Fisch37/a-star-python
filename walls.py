from wallless import WalllessAStar
from base import Board, Position
import math
from PIL import Image

class WallAStar(WalllessAStar):
    __slots__ = ("board",)
    def __init__(self, board : Board):
        self.board = board

        super().__init__(self.board.width,self.board.height)
        pass

    @classmethod
    def from_image(cls,path : str, wall_colour):
        im = Image.open(path)
        pixels = im.load()
        
        board = Board(im.width,im.height)
        for x in range(im.width):
            for y in range(im.height):
                board[x,y] = (pixels[x,y] == wall_colour)
                pass
            pass

        return cls(board)
        pass
    
    def g(self, pos : Position):
        if self.board[pos]: return math.inf # If position is a wall, the effort to get to it is infinite (the effort to get out of it too, but inf + inf is still big)
        return super().g(pos)
        pass
    pass

def main():
    original_file = "maze.png"
    path_file = "maze-pathed.png"
    algo = WallAStar.from_image(original_file,(0x0,0x0,0x0))

    path = algo.evaluate(Position(152,0),Position(168,321))
    with Image.open(original_file) as old_im:
        im = old_im.convert("RGB")
        pass
    pixels = im.load()
    for pos in path:
        pixels[pos.x,pos.y] = (0xff,0,0)
        pass

    im.save(path_file)
    pass

if __name__=="__main__": main()