class Student():
    def __init__(self,name,marks=[]):
        self.name=name
        self.marks=marks


    def info(self):
        return f"Name: {self.name}, Marks: {self.marks}"


    def avarage(self):
        sum=0
        for i in self.marks:
            sum=sum+i

        return sum/len(self.marks)

        


s1=Student("jojo",[100,100,100,90])

print(s1.info())
print(s1.avarage())