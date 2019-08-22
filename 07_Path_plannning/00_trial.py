a = [[0, 'a'], [0, 'b'], [3, 0], [2, '5']]

a.sort()

print(a)


class Point():
    def __init__(self, g_value=0, x=0, y=0, prev_movement=0):
        self.g_value = g_value
        self.x = x
        self.y = y
        self.prev_movement = prev_movement
g = [Point, Point]
print(g)