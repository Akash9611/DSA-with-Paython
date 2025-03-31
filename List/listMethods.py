a = ["Akash","Desai","Python", "Akash"]
b= [10,20,30,40]

a.append("Java")
print("updated list by adding new element: ",a)

b.insert(1, 15)
print("Inserting new element in list at index position: ",b)

print(a.count("Akash"))
print(b.count(20))

print(a.index("Desai"))
print(b.index(40))

a.extend(b)
print(a)

a.pop() # Removes the last element from list, By using pop method we can also remove particular index value [pop(index)] from list EX-pop(1) 
print("POP method: ",a)
 
a.remove(15) # Removes defined element from list
print("Remove Method: ",a)

a.reverse()
print(a)

c=[90,20,10,100,80]
c.sort()
print(c)

