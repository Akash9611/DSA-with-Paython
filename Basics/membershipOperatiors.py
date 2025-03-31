# There two operators 1. in 2. not in

a=10
b=12

list = [1,2,3,4,5,6]

if(a in list):
    print(a, "value is in the list")
else:
    print(a, "value is not in the list")
    
if(b not in list):
    print(b, "value is not in the list")
else:
    print(b, "values is in the list")

c=4
if(c in list):
    print(c, "value is in the list")
else:
    print(c, "value is not in the list")