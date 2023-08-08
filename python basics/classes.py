# # class Persons :
# #     name = 'aisha'
# #     occupation = 'IOT engineer'
# # def info(self):
# #     print(f'{self.name} is an {self.occupation}')

# # a = Persons()
# # a.name = "Shubham"
# # a.occupation = "Accountant"

# # a.info()


# class Book:
#     def __init__(self, title, quantity, author, price):
#         self.title = title
#         self.quantity = quantity
#         self.author = author
#         self.price = price

# book1 = Book('Book 1', 12, 'Author 1', 120)
# book2 = Book('Book 2', 18, 'Author 2', 220)
# book3 = Book('Book 3', 28, 'Author 3', 320)

# print(book1)
# print(book2)
# print(book3)

# # Object-Orietend Programming
# class Employee():
#   name = "Naim"
#   occ = "Coder"
#   age = 18

#   # create a method.!
#   def info(self):
#     print(f"{self.name} is a {self.occ} and {self.age} years old.!")

# emp1 = Employee()
# emp2 = Employee()
# # # create a emp2 details.
# # emp2.name = "Divya"
# # emp2.occ = "HR"
# # emp2.age = 23
# emp2.info()

# class customers :
#    name = 'rohit'
#    address = 'india'
#    id = 34

# def info(self):
#     print(f"{self.name} lives in  {self.address} and this is his id no. {self.id}")

# cust1 = customers()
# cust1.info()   

class Monster:
    health = 90
    energy = 40

    def attack(monster , amount , category):
      print('monster has attacked')
      print(f'this amount is {amount} ')
      print(f'and each has differ cateogry like {category}')
   

    def move( something , speed):
       print(f'the speed is {speed} , which is very high')
monster = Monster()
monster.move(20)
monster.attack(48 ,  5)

# monster.attack(45 , 2)
# print(monster.health)



