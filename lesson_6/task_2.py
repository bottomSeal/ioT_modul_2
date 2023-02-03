class Road():
    def __init__(self, length, width):
        self.length = length
        self.width = width


def weight(road, weight, thickness):
    result = road.length * road.width * weight * thickness
    return result

print(weight(Road(2, 1), 3, 5))