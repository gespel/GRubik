from core.Cube import Cube, CubeColor, CubeDirection

if __name__ == '__main__':
    c = Cube()
    #c.turn(CubeColor.WHITE, CubeDirection.LEFT)

    print(c.cube[CubeColor.RED].southWest)
