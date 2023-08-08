# numbers1 = int(input('enter first number : '))
# number2 = int(input('enter second number : '))
# print('the numbers calculation is :' , number2*numbers1)







# def greater_number(a , b):

#   if (a>b):
#      print('a is greater')
#   else:
#      print('b is greater or equal')
# greater_number( 6 , 6)

def calculator(a, b ):
   geometric_mean = (a*b)/(a+b)
   return geometric_mean
res = calculator(6 , 7)
print(res)

