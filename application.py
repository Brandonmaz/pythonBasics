
# file = "download.jpeg"

# f = open(file, "rb")
# text = f.read()
# x = int(len(text) / 2)

# b = text[:x]
# c = text[x:]
# print(b, c)

# f1 = open("data1.bin", "wb")
# f2 = open("data2.bin", "wb")
# f1.write(b)
# f2.write(c)
# f1.close()
# f2.close()

# f1 = open("data1.bin", "rb")
# text1 = f1.read()
# f2 = open("data2.bin", "rb")
# text2 = f2.read()

# combined = text1 + text2

# print(combined)

# new_file = "new" + file

# f3 = open(new_file, "wb")
# f3.write(combined)
# f3.close()

# -------------------------------------------------------------------------


# my_list = [1, 2, 3, 4, 5]

# my_list.pop()
# my_list[0] = ['Hello']
# my_list.append('Hello')

# my_value = my_list.pop()

# print(my_list)
# print(my_value)

# =============================================================================
# my_list = [1, 5, 3, 4, 2]  # works with strings as well
# my_list.sort()
# my_list.reverse()
# item_count = len(my_list)

# another_list = [0, -1, -2, -3, -4]

# print(my_list)
# print(my_list[2:])
# print(item_count)
# print(my_list[2:] + another_list[2:])

# my_list = ['b', 'd', 'a', 'z', 'x']
# another_list = [1, 2, 3, 4, 5]
# my_list.sort()
# my_list.reverse()
# another_list.reverse()

# new_list = my_list[2:] + another_list[2:]

# print(my_list)
# print(another_list)
# print(new_list)

# =============================================================================
# my_list = ['a', 'b', 'c', 1, 2, 3, [
#     'apple', 'orange', ['jon', 'rob'], 'banana'], 'd']
# fruit_list = my_list[6]
# name_list = fruit_list[2][1]
# name_lists = my_list[6][2][1]
# my_list[6][2][1] = 'joe'
# new_name = my_list[6][2][1]

# print(fruit_list)
# print(name_list)
# print(name_lists)
# print(my_list)
# print(new_name)

# =============================================================================

# my_tuple = ('a', 'b', 'c', [1, 2, 3])

# print(my_tuple[3]) # you can change the lists inisde a tuple, but not the tuple which is a list wrapped in ()

# =============================================================================
# # dictionary reference or value is key(index) and lists are based on position oriented
# people_weight_dictionary = {'john': 134, 'mike': 137,
#                             'rob': 165, 'items': ['orange', {'k3': 190}], 'tuple': (1, 2, 3, 4, 5)}

# people_weight_dictionary['john'] = 143
# people_weight_dictionary.pop('mike')
# # people_weight_dictionary.clear()
# people_weight_dictionary['greg'] = 200
# items_list = people_weight_dictionary['items'][1]['k3']
# tuple_list = people_weight_dictionary['tuple']

# print(people_weight_dictionary)
# print(items_list)
# print(tuple_list)

# =============================================================================
# Comparisons
# print(10 == 10)
# print(5 != 6)
# print(5 > 10)
# print('hello' == 'Hello' or 5 == 5)
# print(('hello' == 'Hello') or (5 == 5) and True)
# print(('hello' == 'Hello') or (5 == 6) and True)
# print((('hello' == 'Hello') or (5 == 5)) and ('8' == '8'))
# print(not (5 == 5))

# condition = not (5 == 5)
# print(type(condition))

# =============================================================================
# functions and creating functions, auto tab when pressing enter (over 4 spaces). Use help() to see what function does
# if you dont pass a name into the function, it will display Buddy, the default value.
# def greet_person(value="Buddy"):
#     print("This is a greeting..." + value + "!")


# greet_person("Brandon")


# def greet_person(value=12):
#     '''
#     CREATING MULTIPLE LINE COMMENT IN FUNCTION with ''' '''
#     this returns a greeting, and you need to change the nunmber into a string
#     command click, or alt click on function names
#     '''
#     print("hey there...")
#     print("This is a greeting..." + str(value) + "!")


# greet_person()

# def remainder(num1, num2):
#     '''
#     creating function that divides num1 and num2 and produces remainder
#     '''
#     print(str(num1) + " divided by " + str(num2) + " =")
#     return num1 % num2


# remainder_value = remainder(10, 3)
# print(remainder_value)

# =============================================================================
# '''
# *args (short for arguments)- if used inside a funtion you can have an unlimited amount values, or arguments. You are required to use the reserved keyword *args, unlike **kwargs.
# **kwargs (short for keyword arguments)- it is just a naming convention, but can be **anything
# '''


# def my_sum(*args):
#     return sum(args)


# result = my_sum(10, 30, 1, 3, 5, 100, 15)

# print(result)


# def key_value(**kwargs):
#     print(kwargs)
#     print(kwargs.keys())
#     print(kwargs.values())
#     print(kwargs.get("weight"))


# key_value(name="brandon", weight=175, age=38)

# =============================================================================
# scope/nested methods (a function associated with a class) or functions (not associated with a class)
# age = 27


# def increase_age():
#     age = 30
#     # defining a nested function

#     def add_four(age):
#         age = age + 4
#         print("Nested Method: " + str(age))
#         # calling the nested function
#     add_four(age)
#     print(age)


# increase_age()

# print(age)

# =============================================================================
# if & else statements... Elif

# elephant = 800
# hippo = 600
# if elephant < hippo:
#     print('yes')
# else:
#     print("no")

# # when the first if is false it will skip all the nested if/else statements and go to the last else
# if (elephant > hippo):
#     print("yes")
#     if 5 > 7:
#         print("yes, yes")
#     else:
#         print("no, no")
# else:
#     print("no")

# animal = 'ape'

# if animal == "cow":
#     print("eat grass")
# elif animal == "bird":
#     print("eat seeds")
# elif animal == "monkey" or animal == "ape":
#     print("eat banana")
# else:
#     print("no animal")

# ==========================================================================================
# for loop

# farm_animals = ['goat', 'cow', 'chicken', 'horse']
# greeting = 'hello my name is brandon'

# counter = 0

# for animal in farm_animals:
#     if animal == "chicken":
#         continue
#     counter += 1
#     sentence = str(counter) + '. ' + animal + " is safe in our farm"
#     print(sentence)

# for char in greeting:
#     if char == "n":
#         break  # will stop loop just before the "n" in name
#         continue  # will skip the letter "n" and continue loop at "a"
#     print(char)

# my_list = ['computer', 'car', 'game', 'bottle']

# for item in my_list:
# comment to coder: work on this next week
# pass ## this is used when code will be applied later on, doesn't interfere with code

# ==========================================================================================
# while loop, while something is true do something. Be careful with while loops because they will create an infinite loop. You need to have a condition that can be met.

# x = 0
# while x < 10:
#     # do something
#     x += 1
#     if(x == 6):
#         continue
#     print(x)
# else:
#     print("x is not less than 10")

# ==========================================================================================
# Looping and Unpacking with Dictionaries and Tuples

# # Dictionary
# employees_salary = {
#     'mike': 27000,
#     'john': 65000,
#     'steve': 30000,
#     'tom': 100000
# }

# for name in employees_salary:
#     print(name)
# for employee in employees_salary.items():
#     print(employee)
# for salary in employees_salary.values():
#     print(salary)
# for names in employees_salary.keys():
#     print(names)
# for (key, value) in employees_salary.items():
#     print(key)
#     print(value)
#     print(key + "'s salary is " + str(value))

# # Tuple
# employees_age = [
#     ('mike', 27, "Manager"),
#     ('john', 65, "Salesman"),
#     ('steve', 30, "HR"),
#     ('tom', 100, "CEO")
# ]
# for name, age, position in employees_age:
#     print(name, age, position)
#     print()  # creates space between each employee

# =============================================================================
# Range, Enumerate, Zip Functions, unpack zip lists

# word = 'hello'
# my_num = [1, 2, 3, 4, 5]
# words = ['hello', 'my', 'name', 'is', 'brandon']

# for letter in list(word):
#     print(letter)
# # the third number is the step. in this example it will go by every two, even.
# for num in range(2, 11, 2):
#     print(num)
# combined_items = zip(my_num, words)
# # print(combined_items)

# for item in combined_items:
#     print(item)  # combined items converted into tuples. Each number is matched with the other list item and is called Enumeration

# for item in enumerate(words, 1): # the number is the starting point of the list, otherwise default would be 0
#     print(item)

# unpack zip files
# list_a = ['a', 'b', 'c', 'd', 'e', 'f']
# list_b = [1, 2, 3, 4, 5, 6]
# list_c = [99, 98, 97, 96, 95, 94]

# zipped_list = list(zip(list_a, list_b, list_c))

# for (a, b, c) in zipped_list:
#     print(a)
#     print(b)
#     print(c)

# # this is a boolean and will return true/false if the object is in the list, also min and max in list
# print('z' in list_a)
# print('john' in {'john': 140})
# print(140 in {'john': 140}.values())
# answer_num = max(list_b), min(list_b)
# answer_letter = max(list_a), min(list_a)
# print(answer_letter)

# import functions from python library using: from ___ import ____
# from random import shuffle
# from random import randint

# random_number = randint(0, 1000)
# print(random_number)


# my_list = [1, 2, 3, 4, 5]
# shuffle(my_list)
# print(my_list)

# my_numbers = list(range(101))
# shuffle(my_numbers)
# print(my_numbers) # if printed again, the code will be the same shuffle list

# =============================================================================
# prompt user, accept user input
# name = input('Enter your name: ')
# print("Hello there " + name.strip()) # strip gets rid of any extra white space if person enters too many spaces in answer

# age = input('Enter your age: ')
# print(5 + int(age))

# ============================================================================
# Object Oriented programming - make resusability of code easier, organizing code - key word for bundling

# class Vehicle:
#     # these variables should not be changed outside of the class specification
#     # this is a class attribute
#     color = ['red', 'blue']
#     vehicle_counter = 0

#     def __init__(self, body_type, make):
#         self.vehicle_body = body_type
#         self.vehicle_make = make
#         Vehicle.vehicle_counter += 1

#     def get_vehicle_count(self): # must have self before any arguments
#         return Vehicle.vehicle_counter

# # how to change the class color, but not a good practice
# Vehicle.color = ["green", "black"]

# car1 = Vehicle("sedan", "toyota")
# # the following 2 lines of code are not following a class specification, which leads to poor design
# car1.color = ["pink"]
# car1.engine = 'v6'


# car2 = Vehicle("sport", "porsche")
# car3 = Vehicle("wagon", "dodge")
# car4 = Vehicle("hatch", "subaru")
# print(car1.vehicle_body, car1.vehicle_make)
# print(car2.vehicle_body, car2.vehicle_make)
# print(type(car1))
# print(car1.color[0])
# print(car2.color[1])
# print(car1.get_vehicle_count())
# print(car2.get_vehicle_count())


# # learning how to access the Vehicle class file
# # inheritance
# from machines.vehicle_stuff import Vehicle, Truck, Motorcycle


# truck1 = Truck("lonbed", "chevy")
# car1 = Vehicle("hatchback", "subaru")
# motorcycle1 = Motorcycle("r1", "Yamaha")


# for veh in [truck1, car1, motorcycle1]:
#     veh.drive()


# def perform_tasks(vehicle_object):
#     vehicle_object.drive()


# perform_tasks(truck1)

# ================================================================
# # practical OOP from utilities file
# from utils.utility_stuff import ListAndCarShortener, DictionaryShortener

# myDictShortener = DictionaryShortener(
#     {1: 'mike', 2: 'tom', 3: 'mark', 4: 'paul', 5: 'steve'})
# myDictShortener.print_shortened_items()

# ===============================
# dunder method, geeksforgeeks.org/dunder
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # need dunder method to incorporate a string
        return self.name + " age is " + str(self.age)

    def __len__(self):  # needed dunder method to check len
        return self.age


tom = Employee("Tom Man", 47)
print(tom)

my_list = [2, 3, 4, 5]
print(len(my_list))
print(len(tom))
# =============================Extra equations from CodeSignal Interview====================================================

# # 1 -
# # Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.
# # using the integer division ( // ), the number rounds to the whole number... ie, 20.99 = 20.

# def centuryFromYear(year):
#     return (year + 99) // 100
# print(centuryFromYear(2000))

# # 2 -
# # Given the string, check if it is a palindrome.

# def checkPalindrome(inputString):
#     if inputString == inputString[::-1]:
#         return True
#     else:
#         return False


# print(checkPalindrome("aabaa"))

# # 3 -
# # Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

# def adjacentElementsProduct(inputArray):
#     max = inputArray[0] * inputArray[1]
#     # print(max)
#     for i in range(len(inputArray) - 1):
#         numbers = inputArray[i] * inputArray[i + 1]
#         # print(numbers)
#         if numbers > max:
#             max = numbers
#     return max
#         # list_of_numbers = range(numbers)
#         # print(list_of_numbers)


# arr = [3, 6, -2, -5, 7, 3]

# print(adjacentElementsProduct(arr))

# # 4 -
# # Finding the area of an interesting polygon - starts with one square in width, which equals 1 square in total. Then 2 squares in width, which equals 5 squares in total. So on and so forth.

# def shapeArea(n):
#     if n < 0:
#         return False
#     else:
#         return (n * n) + ((n-1)*(n-1))
# print(shapeArea(2))

# # 5 -
# # Create a numerical array in order from the lowest number to the highest number. Add any missing numbers to complete array and print out the total of numbers needed to fill the array up.

# # This equation gives me the missing numbers in the array and the amount of numbers needed to fill the array
# def makeArrayConsecutive2(statues):
#     start = statues[0]
#     end = statues[-1]
#     return sorted(set(range(start, end + 1)).difference(statues))


# statues = [6, 2, 3, 8]
# statues.sort()
# length = len(makeArrayConsecutive2(statues))
# print(length)

# # This equation gives me the missing numbers in the array
# def makeArrayConsecutive2(statues):
#     return [i for i in range(statues[0], statues[-1] + 1) if i not in statues]


# statues = [6, 2, 3, 8]
# statues.sort()
# print(makeArrayConsecutive2(statues))

# # This equation gives me the amount needed to fill the array
# def makeArrayConsecutive2(statues):
#     return (max(statues)-min(statues)+1)-len(statues)


# statues = [6, 2, 3, 8]
# print(makeArrayConsecutive2(statues))

# # 6 -
# # Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.
