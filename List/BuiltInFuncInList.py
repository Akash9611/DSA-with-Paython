a=["Data", "Capacity", "Python"]
b=[100, 500, 200]

print(len(a)) # Print the length of list

#Crete new list with range function
c=list(range(5))    # This will create list from 0 t0 4 = [0, 1, 2, 3, 4]
print("new list with range function",c) 

print("Maximum value of list a: ", max(a)) # Take the value from first character/ ASCII value
print("Maximum value of list b: ", max(b)) 

print("Min value of list a", min(a)) # Find min value by first characters ASCII value
print("Min value of list a", min(b))

aTuple = ("akash","addy", "roy", 11, 44 ) 
d=list(aTuple) # Convert Tuple into List
print(d)

strVal = "Hello World" # Converts String into List
e=list(strVal)
print(e) 