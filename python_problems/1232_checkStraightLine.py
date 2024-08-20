def checkStraightLine(coordinates):

    x0, y0, x1, y1 = *coordinates[0], *coordinates[1]
    dx = x1 - x0
    dy = y1 - y0

    return all((x - x0) * dy == (y - y0) * dx for x, y in coordinates)


print(checkStraightLine([[0,0],[0,1],[0,-1]]))