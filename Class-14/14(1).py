class Distance:
    __feet=0
    __inches=0.0
    def __init__(self,*args):
        pass
    def set(self,feet,inches):
        self.__feet=feet
        self.__inches=inches
    def show(self):
        print(self.__feet,"'",self.__inches,'"')
    def input1(self):
        self.__feet=int(input("enter feet: "))
        self.__inches=float(input("enter inches:"))
    def add(x):
        pass
    def add1(x,y):
        pass
        
    d1=Distance(5,7.5)
    d2=distance()
    d2.input1()
    d3=Distance(6.78)
