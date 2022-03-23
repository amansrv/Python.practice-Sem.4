# que-1
# a and b are the inputs
# display numberws from a to b 
# if a== 10 and b ==20
# output is 10, 11, 112......,20

a=10;
b=20;

# a=input("enter ur lower number")
# b=input("enter the upper number")

if(a<b):
    for i in range (a,b+1):
        print(i, end=" ")
  
else:
    for i in range (b,a-1):
        print (i, end=" ")
    
