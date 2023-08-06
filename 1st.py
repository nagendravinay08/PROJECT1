class student:
    def __init__(self,n,r,m1,m2,m3):
        self.name=n
        self.roll=r
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def dispdetails():
        print(self.name,self.roll,self.m1,self.m2,self.m3)

class takeexam(student):
    def average(self):
        self.avg=(self.m1+self.m2+self.m3)//3

    def takeexam():
        self.takeexam()
        print("")

T=takeexam("ram",1,90,98,76)