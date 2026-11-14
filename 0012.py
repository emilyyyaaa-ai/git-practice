class Car:
    def __init__(self,brand,speed = 0):
        self.brand = brand
        self.speed = speed


    def speed_up(self,n):
        self.speed += n
    def show(self):
        print("当前品牌：",self.brand,"当前速度",self.speed)
c = Car("BMBV")
c.speed_up(30)
c.show()
c.speed_up(20)
c.show()
