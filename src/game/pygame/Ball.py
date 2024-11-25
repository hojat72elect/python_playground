class Ball:
    def __init__(self, x, y, speed_x, speed_y, radius):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = radius

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def bounce_y(self):
        self.speed_y *= -1

    def bounce_x(self):
        self.speed_x *= -1

    def reset(self, x, y):
        self.x = x
        self.y = y
