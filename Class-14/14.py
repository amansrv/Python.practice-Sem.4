class Distance:
    __feet=0
    __inches=0.0
    def set(self,feet,inches):
        self.__feet=feet
        self.__inches=inches
        
    def show(self):
        print(self.__feet,"'",self.__inches,'"')
    def input1(self):
        self.__feet=int(input("enter feet: "))
        self.__inches=float(input("enter inches:"))
        
    d1=Distance()
    d1.set(5,7.5)
    d2=distance()
