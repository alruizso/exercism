def validate_triangle(sides):
    if 0 in sides:
        return False
    if sides[0] + sides[1] >= sides[2]         and sides[1] + sides[2] >= sides[0]         and sides[0] + sides[2] >= sides[1]:
        return True
    return False
    
def equilateral(sides):
    if validate_triangle(sides):
        if sides[0] == sides[1] and sides[0] == sides[2] and sides[1] == sides[2]:
            return True
        return False
    return False


def isosceles(sides):
    if validate_triangle(sides):
        if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
            return True
        return False
    return False


def scalene(sides):
    if validate_triangle(sides):
        if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]:
            return True
        return False
    return False
