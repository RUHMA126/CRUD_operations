# creating a tuple
basic_tuple = ('room' , 'apartment' , 'flat')
print(basic_tuple)

# COUNT
basic_tuple = ('room' , 'apartment' , 'flat' , 'room' , 'apartment' , 'flat')
this_tuple = basic_tuple.count('room') #one argument at a time
print(this_tuple)

#INDEX (first occurrence of the value which is passed and return its position)
no_tuple = (1 ,2 , 3 ,4 , 5, 6 ,7, 8 , 9)
this_tuple = no_tuple.index(5)
print(this_tuple)

#check index from the limited range

no_tuple = (1 ,2 , 3 ,4 , 5, 6 ,7, 8 , 9)
this_tuple = no_tuple.index(5 , 0 ,8)
print(this_tuple)
