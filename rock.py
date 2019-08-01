class Rock():

    def __init__(self, x, y, xSpeed, ySpeed, size):
        self.x = x
        self.y = y
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.size = size

    def move(self):
        self.x += self.xSpeed
        self.y += self.ySpeed

    def bounce(self):
        if self.x + self.size > 800 or self.x < 0:
            self.xSpeed *= -1
        if self.y + self.size > 500 or self.y < 0:
            self.ySpeed *= -1
