# lines_counts.py

def intersect(line1, line2):
    # calculate the vectors
    v1 = (line1[1][0] - line1[0][0], line1[1][1] - line1[0][1])
    v2 = (line2[1][0] - line2[0][0], line2[1][1] - line2[0][1])

    # calculate the cross product of the vectors
    cross_product = v1[0] * v2[1] - v1[1] * v2[0]

    # check if the lines are parallel
    if abs(cross_product) < 1e-8:
        return False

    # calculate the intersection point
    s = ((line2[0][0] - line1[0][0]) * v1[1] - (line2[0][1] - line1[0][1]) * v1[0]) / cross_product
    t = ((line2[0][0] - line1[0][0]) * v2[1] - (line2[0][1] - line1[0][1]) * v2[0]) / cross_product

    # check if the intersection point is on both lines
    if s >= 0 and s <= 1 and t >= 0 and t <= 1:
        return True

    return False

class Lines_counts:
    def __init__(self):
        self.centroids = []
        self.direction = None

    def update(self, centroid):
        self.centroids.append(centroid)

    def crossed_line(self, line):
        if len(self.centroids) >= 2:
            # check if the last two centroids crossed the line
            if intersect(line, (self.centroids[-2], self.centroids[-1])):
                # calculate the direction of movement
                dy = self.centroids[-1][1] - self.centroids[-2][1]
                if dy > 0:
                    self.direction = "up"
                else:
                    self.direction = "down"
                return True
        return False
