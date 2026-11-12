class Ball:
    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

myBall = Ball()
myBall.direction = "down"
myBall.color = "red"
myBall.size = "small"

print("I've just created a ball.")
print("My ball is",myBall.color)
print("My ball is",myBall.size)
print("My ball's direction is",myBall.direction)
print("Now I'm going to bounce the ball.")
print()
myBall.bounce()
print("Now my ball's direction is",myBall.direction)