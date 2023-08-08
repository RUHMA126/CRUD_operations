# COUNT

list1 = ["food" , "grocery" , "fruits" , "vegetables" , "fruits" , "vegetables" , "fruits" , "vegetables"]
list1[1]="NoteBOOks"
print(list1)
# check ="Hellooo"
# check[1]="l"
# print(check[1])

lists_count = list1.count("fruits")

print(lists_count)

# SORTING

list2 = ["apple" , "mango" , "banana"]
list2.sort(reverse=False)
print(list2)

list2 = ["apple" , "mango" , "banana"]
list2.sort(reverse=True)
print(list2)

list2 = ["apple" , "mango" , "banana"]
list2.sort()
print(list2)

# COPY METHOD

list2 = ["apple" , "mango" , "banana"]
list2.copy()
print(list2)

# INDEX METHOD

list2 = ["apple" , "mango" , "banana"]
indexes = list2.index("apple")
print(indexes)

list1 = ["food" , "grocery" , "fruits" , "vegetables" , "fruits" , "vegetables" , "fruits" , "vegetables"]
index1 = list1.index("fruits")
print(index1)

# REVERSE METHOD

list1 = ["food" , "grocery" , "fruits" , "vegetables" , "fruits" , "vegetables" , "fruits" , "vegetables"]
list1.reverse
print(list1)

#APPEND

list1 = ["food" , "grocery" , "fruits" , "vegetables" , "fruits" , "vegetables" , "fruits" , "vegetables"]
list1.append('orange')
print(list1)

# EXTEND

list2 = ["apple" , "mango" , "banana"]
list1 = ["food" , "grocery" , "fruits" , "vegetables"]
list2.extend(list1)
list1.extend(list2)
print(list1)

# REMOVE

list1 = ["food" , "grocery" , "fruits" , "vegetables"]
list1.remove("grocery")
print(list1)

# POP_METHOD

list1 = ["food" , "grocery" , "fruits" , "vegetables"]
list1.pop(0)
print(list1)

list1 = ["food" , "grocery" , "fruits" , "vegetables"]
list1.pop()
print(list1)

# DELETE

list1 = ["food" , "grocery" , "fruits" , "vegetables"]
del list1[1]
print(list1)

# CLEAR

list1 = ["food" , "grocery" , "fruits" , "vegetables"]
list1.clear()
