
import random

class MS:
    def __init__(self, N:int):
        self.n = N
        # self.array = [i for i in range(N)]
        # random.shuffle(self.array)
        self.array = [N-i for i in range(N)]

    def printMS(self):
        print(self.array)
        return None
    
    def devide(self) -> list:
        temp = []
        i = 0
        if self.n % 2 == 0:
            while i < (self.n):
                temp1,temp2 = self.array[i:i+2]
                if temp1 < temp2:
                    pass
                else:
                    temp1, temp2 = temp2, temp1
                temp.append([temp1,temp2])
                i += 2
            self.n //= 2
        else:
            while i < (self.n-1):
                temp1,temp2 = self.array[i:i+2]
                if temp1 < temp2:
                    pass
                else:
                    temp1, temp2 = temp2, temp1
                temp.append([temp1,temp2])
                i += 2
            temp.append(self.array[i:])
            self.n = self.n//2 + 1
        self.array = temp

    def merge(self):
        self.devide()
        if len(self.array) < 3:
            return False
        else:
            i = 0
            ans = []
            while i < (self.n-1):
                A = self.array[i]
                B = self.array[i+1]
                index1 = 0
                index2 = 0
                temp = []
                while index1 < len(A) and index2 < len(B):
                    if A[index1] < B[index2]:
                        temp.append(A[index1])
                        index1 += 1
                    else:
                        temp.append(B[index2])
                        index2 += 1
                temp += A[index1:] + B[index2:]
                ans.append(temp)
                i += 2
            if i < len(self.array):
                ans.append(self.array[i])
            self.array = ans
            self.n = len(self.array)
            return True
                    


#test                
A = MS(100)
while A.n > 3:
    A.merge()
A.printMS()



#Problem: リスト内包表記になる