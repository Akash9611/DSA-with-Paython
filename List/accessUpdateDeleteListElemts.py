list1 = [1, 2, 3, 4, 5]

print("======Accessing List Elements========")
print("2nd index value: ", list1[1])
print("print values of list from 2nd index to 3rd index: ", list1[1:4])

print("\n======Updating List Elements========")
list1[2]=10
print("Updated List: ",list1)

print("\n======Deleting List Elements========")
list2=["name", "Data", "values"]

del list1[3]
print("Updated List after deleting 3rd index value: ",list1,"\n")

del list2
# print("\n Deleting whole list object(will throw an error if we will try to print it):",list2)

list1.pop(1)
print("deleting 1st index value using pop method", list1)

list1.remove(10)
print("Removing specific element by using remove method", list1)

print("\n======Appending/Concatenating other List Elements========")
list3=[1.1, 1.2, 1.3, 11.5]
list1.append(list3)
print("\nAppended List: ",list1)

print("\n======Inserting new Element in List========")
list1.insert(1, 11)
print("List after inserting new value: ", list1)

