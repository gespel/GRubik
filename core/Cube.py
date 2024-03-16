from enum import Enum


class CubeColor(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    WHITE = 4
    ORANGE = 5
    YELLOW = 6

class CubeDirection(Enum):
    LEFT = 1
    RIGHT = 2


class Cube:
    def __init__(self):
        self.cube = {
            CubeColor.RED: Side(CubeColor.RED),
            CubeColor.GREEN: Side(CubeColor.GREEN),
            CubeColor.BLUE: Side(CubeColor.BLUE),
            CubeColor.WHITE: Side(CubeColor.WHITE),
            CubeColor.ORANGE: Side(CubeColor.ORANGE),
            CubeColor.YELLOW: Side(CubeColor.YELLOW)
        }

    def turn(self, colorSide: CubeColor, direction: CubeDirection):
        if colorSide in self.cube:
            red = self.cube[CubeColor.RED]
            green = self.cube[CubeColor.GREEN]
            blue = self.cube[CubeColor.BLUE]
            white = self.cube[CubeColor.WHITE]
            orange = self.cube[CubeColor.ORANGE]
            yellow = self.cube[CubeColor.YELLOW]
            if colorSide == CubeColor.WHITE:
                if direction == CubeDirection.LEFT:
                    tmp1 = orange.northEast
                    tmp2 = orange.east
                    tmp3 = orange.southEast

                    orange.northEast = blue.southEast
                    orange.east = blue.south
                    orange.southEast = blue.southWest

                    blue.southWest = red.northWest
                    blue.south = red.west
                    blue.southEast = red.southWest

                    red.nortWest = green.northWest
                    red.west = green.north
                    red.southWest = green.northEast

                    green.northEast = tmp1
                    green.north = tmp2
                    green.northEast = tmp3
        else:
            print(f"Cube has no side {colorSide}")


class Side:
    def __init__(self, color: CubeColor):
        self.main = color
        self.north = color
        self.south = color
        self.east = color
        self.west = color
        self.northEast = color
        self.northWest = color
        self.southEast = color
        self.southWest = color
