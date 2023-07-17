#functions.py

def cross_product(a, b):
    return a[0] * b[1] - b[0] * a[1]

def line_side(line, point):
    """
    Determines which side of the line a point is on.
    Returns 1 if the point is on one side, -1 if it's on the other side, and 0 if it's on the line.
    """
    # Get the vector that represents the line
    line_vector = (line[1][0] - line[0][0], line[1][1] - line[0][1])

    # Get the vector from a point on the line to the point
    point_vector = (point[0] - line[0][0], point[1] - line[0][1])

    # Calculate the cross product
    cp = cross_product(line_vector, point_vector)

    return 1 if cp > 0 else -1 if cp < 0 else 0