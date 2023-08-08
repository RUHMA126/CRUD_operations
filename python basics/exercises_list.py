# list1 = [100, 200, 300, 400, 500]
# list1.sort(reverse = True)
# print(list1)

# PROBLEM 2

# Write Python 3 code in this online editor and run it.
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# Ans = [j + k for j , k in zip(list1  , list2)]
# print(Ans)

# l1=["m","na","i","pra"]
# l2=["y","me","s","veen"]
# l3=[]
# for ANS in range(len(l1)):
#     l3.append(l1[ANS]+l2[ANS])
# print(l3)

# PROBLEM 3

# numbers = [1, 2, 3, 4, 5, 6, 7]
# square = []
# for  i in numbers :
#     square.append(i*i)
# print(square)

# PROBLEM 4

# l1 = ["Hello ", "take "]
# l2 = ["Dear", "Sir"]
# l3=[]
# l3 = [j + k for j in l1 for k in l2 ]
# print(l3)

# l1 = ["Hello ", "take "]
# l2 = ["Dear", "Sir"]
# Ans=[]
# Ans = [j + k for j in l1 for  k in l2]
# print(Ans)

# PROBLEM 5

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]

# for l1 , l2 in zip(list1 , list2):
#  print(l1 , l2)

# problem 6
# my_list = ["hello", "", "world", "", ""]

# new_list = [x for x in my_list if x !='']

# print(new_list)

# my_list = ["", "hello", "", "world", "", ""]

# new_list = list(filter(None, my_list))

# print(new_list)

# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# remove None from list1 and convert result into list
# res = list(filter(None, list1))
# print(res)

# MyList = []
# # Iterate over a sequence of numbers from 0 to 3
# for i in range(4):
#     # In each iteration, add an empty list to the main list
#     MyList.append([])
# print(MyList)

# # output: [[], [], [], []
# problem 6
# list1 = [10, 20, [300, 400, [5000, 6000 , [ 8000 , 500 ,[23409, 39485 , 96544]], 30, 40]]]
# print(list1[2][2][2][1])
# print(list1)

# # problem 7
# list2 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# print(list2[2][1][2].extend(['h' , 'i' , 'j']))
# print(list2)

# ['zero', 'one', 'two', 'three']

# myList = []
# for i in range(3):
#     tempList = []
#     for j in range(3):
#         element = i + j
#         tempList.append(element)
#     myList.append(tempList)
# print("The list of lists is:")
# print(myList)

# myList = [[i+j for i in range(3)] for j in range(3)]
# print("The list of lists is:")
# print(myList)

# myList = [[1, 2, 3, 4, 5], [12, 13, 23], [10, 20, 30], [11, 22, 33], [12, 24, 36]]
# print("The list of lists is:")
# print(myList)
# print("The first item of the nested list is:")
# print(myList[0])

# myList = [[1, 2, 3, 4, 5], [12, 13, 23], [10, 20, 30], [11, 22, 33], [12, 24, 36]]
# print("The list of lists is:")
# print(myList)
# print("The third element of the second inner list is:")
# print(myList[1][2])

# # problem 9

# list3 = [5, 10, 15, 20, 25, 50, 20]
# list3[3] = 200
# print(list3)

# problem 10

#USING FOR LOOP
# list1 = [5, 20, 15, 20, 25, 50, 20]
# remove_item = 20
# for item in list1:
#     if(remove_item==item):
#         list1.remove(remove_item)
# print(list1)

 #USING WHILE LOOP

# list1 = [5, 20, 15, 20, 25, 50, 20]
# while 20 in list1:
#     list1.remove(20)
# print(list1)


#comparing two lists in python


rare = (["word1","word2","word3",4,8])
freq = (["word1","word2","word3",4,8])
assert rare==freq
#   print('it is equal')
# else:
#   print('it is not equal')



# rare = (["word1"])
# freq = (["word1"])
# if rare==freq:
#   print('it is equal')
# else:
#   print('it is not equal')



# reverse of a list
rare = (["word1","word4","word5"])
rare.reverse()
print(rare)


#comparing two dictionaries


# dict1 = {'Name': 'asif', 'Age': 5}
# dict2 = {'Name': 'asif', 'Age': 5}
# if dict1 == dict2:
#    print('it is equal')
# else:
#    print('it is not equal')
