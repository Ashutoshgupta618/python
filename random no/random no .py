import random
a= random.randint(1,100)
b=int(input("enter a no b/W 1-100"))

if( a== b):
    print("no. match by computer")
else:
    print("no. not match: no. given by computer is ",a," and no. given by you is " ,b)