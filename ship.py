class Ship():

    size = 30
    speed = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xVelocity = 0
        self.yVelocity = 0

    def move(self):
        self.x += self.xVelocity
        self.y += self.yVelocity