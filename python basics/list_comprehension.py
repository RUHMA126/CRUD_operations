my_list = []
for num in range(5):
    my_list.append(num)
print(my_list)


#using list comprehension
new_list = [num for num in range(5)]

print(new_list)



numbers = [1,2,3,4,5,6]
square_numbers = []

for num in numbers: 
    square_numbers.append(num * num)

print(square_numbers)

#using list comprehension
numbers = [1,2,3,4,5,6]

square_numbers = [num * num for num in numbers]

print(square_numbers)

numbers = [0 , 2 , 4 , 6 , 8 , 10]
even_numbers = [num for num in range(20)]
print(even_numbers)

