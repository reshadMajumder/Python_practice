name="jojo"

def printName():
    print("my name is "+name)

# printName()

# ======================

x=int(10)
y=str("string")

def printType(x):
        print(type(x))
# try:
#     printType()
   

# except:
#     print("error")



import random
def randomNumber(st,lt):
      return random.randrange(st,lt)

# print(randomNumber(1,10))



class Charrecter:
    def __init__ (self,name,age,speed):
        self.name=name
        self.age=age
        self.speed=speed

    
    def DoubleSpeed(self):
        self.speed=self.speed*2
  

    def info(self):
        print(f"my name is {self.name} and my age is {self.age} and my speed is {self.speed}")



# warriror=Charrecter("jojo",20,10)
# warriror.DoubleSpeed()
# print(warriror.info())

num=[6,7,8,9,10]

for i in range(len(num)):
    print(i)
    
