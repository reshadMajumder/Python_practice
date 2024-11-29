class Solution:
    numbers=[]
    output=[]
    def __init__(self,numbers,target):
        self.numbers=numbers
        self.target=target


    def sum(self):
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers)):
                if self.numbers[i] + self.numbers[j] == self.target:
                    self.output.append(i)
                    self.output.append(j)
        self.output = list(set(self.output))
        return self.output

test1=Solution([3,2,4],6)
print(test1.sum())