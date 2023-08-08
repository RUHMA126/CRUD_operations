sports = ["basket ball"  , "cricket"]
list_of_items = [1 , "food" ,2]
all_attendees = [True , False]

print("cricket" in sports)
print(3 in list_of_items)

print(list_of_items[2])

list_of_items[1] = "no food"
print(list_of_items)
all_attendees[1] = "some are present"
print(all_attendees)

print(list_of_items[-2])

list1 = ["food" , "grocery" , "fruits" , "vegetables"]
print(list1[:2]) 

list2 = ["rock" , "paper" , "scissors"]
list2[0] = "paper"
print(list2)

list1 = ["food" , "grocery" , "fruits" , "vegetables"]
list1[1 : 3] = ["rocky" , "shocky" , "tocky" , "mocky" , "crocky"]
print(list1)

list2 = ["apple" , "mango" , "banana"]
list2.append("water" , "water")
print(list2)

list2 = ["apple" , "mango" , "banana"]
list2.insert(0 , "water")
print(list2)

list2 = ["apple" , "mango" , "banana"]
list1 = ["food" , "grocery" , "fruits" , "vegetables"]
list2.extend(list1)
list1.extend(list2)
print(list1)

list1 = ["food" , "grocery" , "fruits" , "vegetables"]
list1.remove("grocery")
print(list1)

list1 = ["food" , "grocery" , "fruits" , "vegetables"]
list1.pop(0)
print(list1)

list1 = ["food" , "grocery" , "fruits" , "vegetables"]
list1.pop()
print(list1)

list1 = ["food" , "grocery" , "fruits" , "vegetables"]
del list1[1]
print(list1)


list1 = ["food" , "grocery" , "fruits" , "vegetables"]
del list1

list1 = ["food" , "grocery" , "fruits" , "vegetables"]
list1.clear()