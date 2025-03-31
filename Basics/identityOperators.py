a=10
b=a

print("a=",a,"Identity: ",id(a),"------ b=",b,"identity: ",id(b)) 

if(a is b):
    print("a and b have same identity")
else:
    print("a and b do not have same identity")

if(id(a)==id(b)):
    print("a and b have same identity")
else:
    print("a and b do not have same identity")

b=30
print("----------------After updating the value of b ------------------")
print("a=",a,"Identity: ",id(a),"------ b=",b,"identity: ",id(b))

if(a is not b):
    print("a and b do not have same identity")
else:
    print("a and b have same identity")