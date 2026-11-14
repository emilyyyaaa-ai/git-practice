#BankAccount

class BankAccout:
    #构造函数
    def __init__(self,name,money = 0):#初始money = 0
        self.name = name
        self.money = money

#存款
    def deposit(self,amount):
        self.money += amount

#取款
    def withdraw(self,amount):
        if self.money >+ amount:
            self.money -= amount
        else:
            print("余额不足")
    def show(self):
        print(self.name,self.money)


a = BankAccout("zhangsan",1000)  
a.deposit(200)
a.withdraw(500)
a.show
a.withdraw(1000)             
         
        
