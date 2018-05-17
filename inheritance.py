# Inheritance example using phone

class Phone:
  def __init__(self, phone_number):
    self.number = phone_number

  def call(self, other_number):
    print("Calling {} from {}.".format(self.number, other_number))

  def text(self, other_number, msg):
    print("Sending text from {} to {}:".format(self.number, other_number))
    print(msg);


class IPhone(Phone):
  def __init__(self, phone_number):
    super().__init__(phone_number)

  def record_screen(self, screen):
    self.screen = screen
    self.screen.record()

class Android(Phone):
  def __init__(self, phone_number):
    super().__init__(phone_number)
    self.layout = "Default"

  def customize_layout(self, new_layout):
    self.layout = new_layout


# Basic python program that says hello and asks for my age
# print('what up G?')
# print('What is your first name?')
# my_name = input()
# print('You got a funny name! ' + my_name)
# how_long = len(my_name)
# print('Your first name has ' + str(how_long) + ' characters. How old are you')
# my_age = input()
# print('So ' + my_name + ', you are ' + str(my_age) + ' years old')


# Learn about python classes
# class Employee:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.initials = first[:1] + last[:1]
#         self.pay = pay
#         self.bonus = pay * .15
#
#
# emp_1 = Employee('Reynaldo', 'Espinosa', 40000)
# emp_2 = Employee('Oliver', 'Espinosa', 35000)
# print('{} {}, your email is: {}, your initials are {}, starting salary ${} and yearly bonus is ${}'.format(emp_1.first, emp_1.last, emp_1.email, emp_1.initials, emp_1.pay, emp_1.bonus))
# print('{} {}, your email is: {}, your initials are {}, starting salary ${} and yearly bonus is ${}'.format(emp_2.first, emp_2.last, emp_2.email, emp_2.initials, emp_2.pay, emp_2.bonus))

# More Learning About Python classes
# class CoffeeCup():
#   def __init__(self, capacity):
#     self.capacity = capacity
#     self.amount = 0
#
#   def fill(self):
#     self.amount = self.capacity
#
#   def empty(self):
#     self.amount = 0
#
#   def drink(self, amount):
#     self.amount -= amount
#     if (self.amount == 0):
#       self.amount = 0
#
# steves_cup = CoffeeCup(12)  # a fancy latte.
# seans_cup = CoffeeCup(16)    # gas station drip.
# brandis_cup = CoffeeCup(2)  # a quick espresso.
#
# steves_cup.fill()
# seans_cup.fill()
# brandis_cup.fill()
#
# steves_cup.drink(1)
# seans_cup.drink(1)
# brandis_cup.drink(1)
#
# print(steves_cup.amount, "ounces left")
# print(seans_cup.amount, "ounces left")
# print(brandis_cup.amount, "ounces left")
