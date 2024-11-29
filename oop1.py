class Students():
    name="anonomus"

    nickname="jojo"

    def __init__(self,fullname,id,age):
        self.name=fullname
        self.id=id
        self.age=age

    def info(self):
        print(f"Name: {self.name}")
   

 


s1=Students("koko",80,9)
print(s1.name,s1.nickname)
s2=Students("jakir",60,6)
print(s2.name,s2.nickname)
s3=Students("fukko",6,7)
print(s3.name)
s3.info()
