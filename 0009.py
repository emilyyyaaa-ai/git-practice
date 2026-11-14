class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score


    def show_info(self):
        print("姓名：",self.name,"分数：",self.score)
    def add_bonus(self,n):
        self.score += n      



s = Student("Li",85)
s.add_bonus(6)
s.show_info()
s.add_bonus(10)
s.show_info()        