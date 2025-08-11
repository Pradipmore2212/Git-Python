# 1.Write a Python program to print the following string in a specific format (see the output).
#Sample String : 
# "Twinkle, twinkle, little star, 
# How I wonder what you are! 
# Up above the world so high, 
# Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# How I wonder what you are"

# print("Twinkle, twinkle, little star,")
# print("\tHow I wonder what you are!")
# print("\t\tUp above the world so high,")
# print("\t\tLike a diamond in the sky.")
# print("Twinkle, twinkle, little star,")
# print("\tHow I wonder what you are")



# 2.Write a Python program to find out what version of Python you are using.

# import sys 

# print("python version")
# print(sys.version)
# print("version info:")
# print(sys.version_info)


# 3.Write a Python program to display the current date and time.
#Sample Output :
#Current date and time :
#2020-07-25 11:39:14

# import datetime
# now = datetime.datetime.now()

# print("current date and time :")
# print(now.strftime("%Y-%m-%d %H:%M:%S"))


# 4.Write a Python program that calculates the area of a circle based on the radius entered by the user.
#Sample Output :
#r = 1.1
#Area = 3.8013271108436504
# import math

# radius = float(input("enter the radius of the circle: "))
# area = math.pi * radius ** 2
# print("Area =", area)


# 5.Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

# first_name = input("enter your first name: ")
# last_name = input("enter your last name: ")

# print("reversed name:", last_name, first_name)



# 6.Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list 
#and a tuple of those numbers.
#Sample data : 3, 5, 7, 23
#Output :
#List : ['3', ' 5', ' 7', ' 23']
#Tuple : ('3', ' 5', ' 7', ' 23')

# data = input("enter comma separated numbers")
# number_list = data.split(",")
# number_tuple = tuple(number_list)
# print("List:", number_list)
# print("tuple:", number_tuple)


# 7.Write a Python program that accepts a filename from the user and prints the extension of the file.
#Sample filename : abc.java
#Output : java

# filename = input("Enter the filename: ")
# if '.' in filename:
#     extension = filename.split(".")[-1]
#     print("the extension of the file is:", extension)
# else:
#     print("no extensions found in the filename.")


#8.Write a Python program to display the first and last colors from the following list.
#color_list = ["Red","Green","White" ,"Black"]        



# color_list = ["Red", "Green", "white", "black"]

# first_color = "Red"
# last_color = "black"

# print(f"first color is: {first_color} \nlast color is: {last_color} ")


# 9.Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014


# exam_st_date = (11, 12, 2014)
# print(f"the examination will start from :{exam_st_date[0]} / {exam_st_date[1]} / {exam_st_date[2]}")


#10.Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
#Sample value of n is 5
#Expected Result : 615

# n = input("enter a number: ")
# result = int(n) + int(n*2) + int(n*3)
# print("result:", result)



#11.Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
#Sample function : abs()
#Expected Result :
#abs(number) -> number
#Return the absolute value of the argument.

# func_name = input("Enter the built-in function name (e.g., abs, len, max):")

# print(f"\nDocumentation for {func_name}():\n")
# help(eval(func_name))


#12.Write a Python program that prints the calendar for a given month and year.
#Note : Use 'calendar' module.


# year = int(input("enter a year:"))
# month = int(input("enter a month"))

# print(year,month)



#13.Write a Python program to print the following 'here document'.
#Sample string :
#a string that you "don't" have to escape
#This
#is a ....... multi-line
#heredoc string --------> example


# print("""a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example""")


#14. Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
# from datetime import date

# date1 = date(2014, 7, 2)
# date2 = date(2014, 7, 11)

# result = (date2 - date1).days
# print(result, "days")


#15. Write a Python program to get the volume of a sphere with radius six.

# import math

# radius = 6
# volume = (4/3 * math.pi*radius**3)
# print("volume of the sphere is:", volume)

#16. Write a Python program to calculate the difference between a given number and 17. 
# If the number is greater than 17, return twice the absolute difference.

# num = int(input("enter a number:"))

# if num > 17:
#     result = 2 * abs(num - 17)

# else:
#     result = 17-num
#     print("result:", result)


#17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

# num = int(input("enter a number: "))

# if (900 <= num <= 1100) or (1900 <= num <= 2100):
#     print("number is within 100 of 1000 or 2000")
# else:
#     print("number is not within 100 of 1000 or 2000")


#18. Write a Python program to calculate the sum of three given numbers.
# If the values are equal, return three times their sum.


# num1 = int(input("enter a first number: "))
# num2 = int(input("enter a second number: "))
# num3 = int(input("enter a third number: "))

# if num1 == num2 == num3 :
#     result = 3 * (num1 + num2 + num3)
# else:
#     result = num1 + num2 + num3

# print("result:", result)




#19. Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front.
# Return the string unchanged if the given string already begins with "Is".


# text = input("enter a string: ")
# if text.startswith ("Is"): 
#    print("result:", text)
# else:
#    print("result:", "Is" + text)




#20. Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

# text = input("enter a string: ")
# n = int(input("enter a non-negative number:"))

# if n>=0:
#     result = text * n
#     print("result:", result)
# else:
#     print("please enter a non-negative number.")



#21. Write a Python program that determines whether a given number (accepted from the user) is even or odd, and 
# prints an appropriate message to the user.


# number = int(input("enter a number:"))

# if number % 2 == 0:
#     print("the number is even")
# else:
#     print("the number is odd")    



#22. Write a Python program to count the number 4 in a given list.

# input_str = input("enter numbers seperated by commas:")
# numbers = list(map(int, input_str.split(",")))

# count = numbers.count(4)

# print("number 4 appears", count, "times in the list")



#23. Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. 
# Return n copies of the whole string if the length is less than 2.

# text = input("enter a string: ")
# n = int(input("enter a non-negative integer: "))
 
# if len(text) <=2:
#     result = text * n
# else:
#     result = text[:2] * n
#     print(result)    


#24. Write a Python program to test whether a passed letter is a vowel or not.

# letter = input("enter a vowel: ")

# if letter.lower() in 'aeiou':
#     print(f"letter is a vowel") 
# else:
#     print(f"letter is not a vowel")


#25.Write a Python program that checks whether a specified value is contained within a group of values.

# value = int(input("Enter a number to check: "))
# group = [1, 5, 8, 3]
# result = value in group
# print(f"{value} -> {group} : {result}")



#26. Write a Python program to create a histogram from a given list of integers.

# numbers = [4, 7, 1, 3, 5]
# for num in numbers:
#     print('*' * num)



#27. Write a Python program that concatenates all elements in a list into a string and returns it.

# def concatenate_list_data(lst):
#     result = ''  
    
#     for element in lst:
#         result += str(element)  

#     return result  

# print(concatenate_list_data([1, 5, 12, 2]))

#28. Write a Python program to print all even numbers from a given list of numbers in the same order and
# stop printing any after 237 in the sequence.
# Sample numbers list :

# numbers = [ 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,  958,743, 527 ]

# for num in numbers:
#     if num == 237:
#         break     
#     if num % 2 == 0:
#         print(num)


#29. Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
# Test Data :

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

# result = color_list_1 - color_list_2
# print(result)




#30. Write a Python program that will accept the base and height of a triangle and compute its area

# base = float(input("enter the base of the triangle: "))
# height = float(input("enter the height of the triangle: "))

# area = 0.5 * base * height
# print("the area of triangle is: ", area)




#31. Write a Python program that computes the greatest common divisor (GCD) of two positive integers.

# def gcd(x, y):
#     gcd = 1
#     if x % y == 0:
#         return y
#     for k in range(int(y / 2), 0, -1):
#         if x % k == 0 and y % k == 0:
#             gcd = k
#             break
#     return gcd

# print("GCD of 12 & 17 =", gcd(12, 17))
# print("GCD of 4 & 6 =", gcd(4, 6))
# print("GCD of 336 & 360 =", gcd(336, 360))




#32. Write a Python program to find the least common multiple (LCM) of two positive integers.

# num1 = int(input("Enter first positive number: "))
# num2 = int(input("Enter second positive number: "))

# import math
# gcd = math.gcd(num1, num2)

# print("the gcd of", num1, "and", num2, "is:", gcd )




#33. Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.

# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# c = int(input("enter third number: "))

# if a == b or b == c or a == c:
#     result = 0
# else:
#     result = a + b + c

# print("result: ", result)



#34. Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.

# a = int(input("enter first number: "))
# b = int(input("enter second number: "))

# sum_result = a + b
# if 15 <= sum_result <= 20:
#     print("result: 20")
# else:
#     print("result:", sum_result)



#35. Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5

# a = int(input("enter first number: "))
# b = int(input("enter second number: "))

# if a == b or (a + b ==5 or (a-b) ==5):
#     print("true")
# else:
#     print("false")



#36. Write a Python program to add two objects if both objects are integers.

# a = input("enter first object: ")
# b = input("enter second object: ")

# if a.isdigit() and b.isdigit():
#     sum_result = int(a) + int(b)
#     print("sum:", sum_result)
# else:
#     print("object must be integer. ")    




#37. Write a Python program that displays your name, age, and address on three different lines.

# name = "pradip"
# age = "25"
# adress = "latur"

# print("name:", name)
# print("age:", age)
# print("adress:", adress)



#38. Write a Python program to solve (x + y) * (x + y).
# Test Data : x = 4, y = 3

# x = 4
# y = 3

# result = (x + y) * (x + y)
# print("result:", result)


#39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
# Test Data : amt = 10000, int = 3.5, years = 7

# amt = 10000
# interest = 3.5
# years = 7

# future_value = amt * (1 + (interest / 100)) ** years
# print(round(future_value, 2))




#40. Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).

# import math 
# x1 = float(input("enter x1:"))
# y1 = float(input("enter y1:"))
# x2 = float(input("enter x2:"))
# y2 = float(input("enter y2:"))


# distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
# print("distance:", round(distance, 2))



#41. Write a Python program to check whether a file exists.

# import os
# file_path = input("Enter the file path: ")

# if os.path.exists(file_path):
#     print("File exists.")
# else:
#     print("File does not exist.")



#42.Write a program to create a new string made of an input string’s first, middle, and last character.
#Given:str1 = "James"

# str1 = "james"
# result = str1[0::2] 
# print(result)



#43. Write a program to create a new string made of the middle three characters of an input string.
# Given:
# Case 1
# str1 = "JhonDipPeta"
# Case 2
# str2 = "JaSonAy"

# str1 = "JhonDipPeta"
# str2 = "JaSonAy"

# slice_Dip = str1[4:7]
# print(slice_Dip)
# slice_Son = str2[2:5]
# print(slice_Son)



#44. Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
# s1 = "Ault"
# s2 = "Kelly"  

# s1 = "Ault"
# s2 = "Kelly" 

# s3 = s1[:len(s1)//2] + s2 + s1[len(s1)//2]
# print(s3)



#45. Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

# s1 = "America"
# s2 = "Japan"
# s3 = s1[0] + s2[0] + s1[len(s1)//2] + s2[len(s2)//2] + s1[-1] + s2[-1]

# print(s3)




#46. Given string contains a combination of the lower and upper case letters. 
# Write a program to arrange the characters of a string so that all lowercase letters should come first.

# str1 = "PyNaTive"
# lower = []
# upper = []
# for char in str1:
#     if char.islower():
#         lower.append(char)
#     else:
#         upper.append(char)
# sorted_str = ''.join(lower + upper)
# print('Result:', sorted_str)



#47. Count all letters, digits, and special symbols from a given string.

# str1 = "P@#yn26at^&i5ve"
# letters = 0
# digits = 0
# special = 0
# for char in str1:
#  if char.isalpha():
#   letters += 1
#  elif char.isdigit():
#   digits += 1
#  else:
#   special += 1
# print("letters:", letters)
# print("digits:", digits)



#48. Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, 
# then the last char of s2, Next,the second char of s1 and second last char of s2, and so on.
# Any leftover chars go at the end of the result.

# s1 = "Abc"
# s2 = "Xyz"

# s3 = ""
# len1, len2 = len(s1), len(s2)

# for i in range(max(len1, len2)):
#     if i < len1:
#         s3 += s1[i]
#     if i < len2:
#         s3 += s2[-(i + 1)]

# print("New string:", s3)





#49. Write a program to check if two strings are balanced. 
# For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. 
# The character’s position doesn’t matter

# s1 = "Yn"
# s2 = "PYnative"

# all_present = True

# for char in s1:
#     if char not in s2:
#         all_present = False
#         break

# if all_present:
#     print(True)
# else:
#     print(False)



#50. Write a program to find all occurrences of “USA” in a given string ignoring the case.

# import re

# text = "Welcome to usa. usa is awesome. I love the USA!"

# matches = re.findall(r"usa", text, re.IGNORECASE)
# print("USA found", len(matches), "times")



#51. Write a program to count occurrences of all characters within a string

# from collections import Counter
# input_str = "apple"
# print(Counter(input_str)) 



#52. Reverse a given string

# str1 = "PYnative"
# reversed_str = str1[::-1]
# print(reversed_str)



#53. Write a program to find the last position of a substring “Emma” in a given string.


# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# last_pos = str1.rfind("Emma")
# print("last position of Emma start at index: ", last_pos)




#54. Write a program to split a given string on hyphens and display each substring.

# str1 = "Emma-is-a-data-scientist"

# split = str1.split("-")
# for split in split:
#  print(split)



#55. Remove empty strings from a list of strings 

# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# cleaned_list = [s for s in str_list if s]
# print(cleaned_list)




#56. Write a program to accept two integer numbers from the user and calculate their product.

# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))

# product = num1 * num2
# print("the product of num1 and num 2 is:", product)




#57. Write a program to display four string “My, “Name“, “Is“, “James” as “My**Name**Is**James“.'

# str1 = 'My'
# str2 = 'Name'
# str3 = 'Is'
# str4 = 'James'

# print(str1, str2, str3, str4, sep='**')



#58. Display Decimal Number to Octal using print() function

# decimal_number = 8
# print("Octal representation:", oct(decimal_number))



#59.  Display Float Number with 2 Decimal Places.

# num = 458.541315
# print("Formatted number: {:.2f}".format(num))



#60. Accept a list of 5 float numbers as an input from the user.

# numbers = []

# for i in range(5):
#     num = float(input(f"Enter float number {i+1}: "))
#     numbers.append(num)
# print("The list of float numbers is:", numbers)



#61. Accept three strings in one input
# str1, str2, str3 = input("Enter three strings separated by spaces: ").split()

# print("First string:", str1)
# print("Second string:", str2)
# print("Third string:", str3)



#62. Format variables using string.format() method.

# totalMoney = 1000
# quantity = 3
# price = 450

# print("I have ${}, I want to buy {} items for ${} each.".format(totalMoney, quantity, price))



#63. Check File is Empty or Not

# import os

# file_path = "example.txt"

# if os.path.exists(file_path) and os.stat(file_path).st_size == 0:
#     print("The file is empty.")
# else:
#     print("The file is not empty.")



#64. Ask the user for a numerator and a denominator. 
# Calculate the percentage and display it with two decimal places followed by a percent sign (e.g., 75.50%).


# numerator = float(input("Enter the numerator: "))
# denominator = float(input("Enter the denominator: "))

# if denominator != 0:
#     percentage = (numerator / denominator) * 100
#     print("Percentage: {:.2f}%".format(percentage))
# else:
#     print("Denominator cannot be zero.")



#65. Create a simple interactive menu with options like “1. Say Hello”, “2. Calculate Square”, “3. Exit”. 
# Based on the user’s input, perform the corresponding action

# while True:

#     print("\nMenu:")
#     print("1. Say Hello")
#     print("2. Calculate Square")
#     print("3. Exit")

#     choice = input("Enter your choice (1/2/3): ")

#     if choice == '1':
#         print("Hello!")
#     elif choice == '2':
#         number = float(input("Enter a number to square: "))
#         print("Square of", number, "is", number ** 2)
#     elif choice == '3':
#         print("Exiting the program. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please select 1, 2, or 3.")




#66. Write a program to accept two integer numbers from the user and calculate their product.

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# product = num1 * num2

# print("The product of", num1, "and", num2, "is:", product)



#67. Print first 10 natural numbers using while loop
# num = 1

# while num <= 10:
#     print(num)
#     num += 1  



#68. Write a Python code to print the following number pattern using a loop.

# def display_info(name, age):
#     print("Name:", name)
#     print("Age:", age)

# display_info("Pradip", 25)



#69. Write a program to create a function func1() that accepts a variable number of arguments and prints each of their values.

# def func1(*args):
#     for value in args:
#         print(value)
# func1(20, 40, 60)
# print("---")
# func1(80, 100)




#70. Write a program to create a recursive function that calculates the sum of numbers from 0 to 10.
# A recursive function is a function that calls itself repeatedly.

# def recursive_sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + recursive_sum(n - 1)

# result = recursive_sum(10)
# print("Sum from 0 to 10 is:", result)



#71. Generate a Python list of all the even numbers between 4 to 30

# even_numbers = list(range(4, 31, 2))

# print("Even numbers from 4 to 30:", even_numbers)



#72. Find the largest item from list.
# x = [4, 6, 8, 24, 12, 2]
# largest = max(x)
# print("The largest item in the list is:", largest)




#73. A lambda function in Python is a small anonymous function defined using the lambda keyword. 
# The syntax is lambda arguments: expression. 
# The expression is evaluated and returned.

# square = lambda x: x**2
# number = 5
# squared_number = square(number)
# print(f"The square of {number} is {squared_number}")



#74. Use a lambda with the filter() function to get all even numbers from a list.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_nums = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_nums)



#75. Perform Basic List Operations
# Access Elements: Print the third element.
# List Length: Print the number of elements in the list
# Check if Empty: Write a code to check is list empty.
 
# my_list = [10, 20, 30, 40, 50]

# print("Third element:", my_list[2])

# print("Length of list:", len(my_list))

# if not my_list:
#     print("The list is empty")
# else:
#     print("The list is not empty")



#76. Calculate and print the sum and average of all numbers in a list.

# my_list = [10, 20, 30, 40, 50]
# total = sum(my_list)
# average = total / len(my_list)
# print("Sum:", total)
# print("Average:", average)



# 77.Write a Python program to parse a string to float or integer.
# s = "123.45"

# float_num = float(s)
# print("Float:", float_num)
# int_num = int(float(s))
# print("Integer:", int_num)



# 78.Write a Python program to list all files in a directory.
# import os

# files = os.listdir(".")
# for file in files:
#     print(file)




# 79.Write a Python program to print without a newline or space.
# print("Hello", end="") 
# print("World", end="")  




# 80.Write a Python program to determine the profiling of Python programs.
# import cProfile

# def test():
#     total = 0
#     for i in range(1000):
#         total += i
#     return total

# cProfile.run('test()')



# 81.Write a Python program to print to STDERR.
# import sys

# print("This is an error message", file=sys.stderr)



# 82.Write a Python program to sum the first n positive integers.
# n = int(input("Enter a number: "))
# total = sum(range(1, n + 1))
# print("Sum of first", n, "positive integers is:", total)



# 83.Write a Python program to convert height (in feet and inches) to centimeters.
# feet = int(input("Enter feet: "))
# inches = int(input("Enter inches: "))

# cm = feet * 30.48 + inches * 2.54
# print("Height in centimeters:", cm)



#84. Write a Python program to calculate the hypotenuse of a right angled triangle.
# import math

# a = float(input("Enter side a: "))
# b = float(input("Enter side b: "))

# hypotenuse = math.hypot(a, b)
# print("Hypotenuse:", hypotenuse)




#85. Write a Python program to convert the distance (in feet) to inches, yards, and miles.
# feet = float(input("Enter distance in feet: "))

# inches = feet * 12
# yards = feet / 3
# miles = feet / 5280

# print("Inches:", inches)
# print("Yards:", yards)
# print("Miles:", miles)



#86. Write a Python program to convert all units of time into seconds.
# days = int(input("Days: "))
# hours = int(input("Hours: "))
# minutes = int(input("Minutes: "))
# seconds = int(input("Seconds: "))

# total_seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds
# print("Total seconds:", total_seconds)



#87. Write a Python program to calculate the body mass index.
# weight = float(input("Enter weight in kg: "))
# height = float(input("Enter height in meters: "))

# bmi = weight / (height ** 2)
# print("BMI:", round(bmi, 2))



#88. Write a Python program to calculate sum of digits of a number.
# num = input("Enter a number: ")
# digit_sum = sum(int(d) for d in num if d.isdigit())
# print("Sum of digits:", digit_sum)


#89. Write a Python program to sort three integers without using conditional statements and loops.
# nums = [int(input("Enter a number: ")) for _ in range(3)]
# print("Sorted:", sorted(nums))



#90. Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary).
# container = [1, 2, 3, 4]
# print("Sum:", sum(container))



#91. Write a Python program to count the number of occurrences of a specific character in a string.
# text = "hello world"
# char = 'l'

# count = text.count(char)
# print(f"'{char}' appears {count} times.")



#92. Given variables x=30 and y=20, write a Python program to print "30+20=50".
# x = 30
# y = 20
# print(f"{x}+{y}={x+y}")



#93. Write a Python program to perform an action if a condition is true.
# Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.
# n = float(input("Input a number: "))
# if (n == 1):
#    print("First day of a Month!")
# else:
#    print("empty")




#94. Write a Python program to swap two variables.
# a = 5
# b = 10
# a, b = b, a
# print("a:", a, "b:", b)



#95. Write a Python program to get the Identity, Type, and Value of an object.
# x = 42
# print("ID:", id(x))
# print("Type:", type(x))
# print("Value:", x)



#96. Write a Python program to check whether multiple variables have the same value.
# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# c = int(input("enter third number:"))

# if a == b == c:
#     print("All variables have the same value")
# else:
#     print("Variables have different values")




#97. Write a Python program to sum all counts in a collection.
# from collections import Counter

# data = Counter(a=3, b=5, c=2)
# print("Total count:", sum(data.values()))




#98. Write a Python program that uses double quotes to display strings.
# s = "She said, \"Hello, how are you?\""
# print(s)



#99. Write a Python program to split a variable length string into variables.

# data = "Pradip,25,Male"
# name, age, gender = data.split(',')

# print("Name:", name)
# print("Age:", age)
# print("Gender:", gender)



#100. Write a Python program to print a variable without spaces between values.

# x = 30
# print('Value of x is "' + str(x) + '"')



# 101.Write a Python program to check whether a variable is an integer or string.
# var1 = 100
# var2 = "hello"

# print(isinstance(var1, int))  
# print(isinstance(var2, str))   



# 102.Write a Python program to test if a variable is a list, tuple, or set.
# data = [1, 2, 3]

# if isinstance(data, list):
#     print("It is a list.")
# elif isinstance(data, tuple):
#     print("It is a tuple.")
# elif isinstance(data, set):
#     print("It is a set.")



# 103.Python program to calculate the area of a circle
# from math import pi

# r = float(input("Enter the radius of the circle: "))
# area = pi * r**2
# print("Area of the circle is:", area)


# 104.Write a Python program to accept a filename from the user and print the extension of that.
# filename = input("Enter the filename: ")
# ext = filename.split(".")[-1]
# print("The extension of the file is:", ext)



# 105.Write a Python program to display the first and last colors from the following list.
# color_list = ["Red", "Green", "White", "Black"]
# print("First color:", color_list[0])
# print("Last color:", color_list[-1])



#106. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

# n = input("Enter a number: ")
# result = int(n) + int(n*2) + int(n*3)
# print("Result is:", result)




# 107.Write a Python program to print the calendar of a given month and year.
# import calendar
# year = int(input("enter year: "))
# month = int(input("enter month: "))



# 108.Write a Python program to calculate the number of days between two dates.
# from datetime import date
# date1 = date(2025, 7, 30) 
# date2 = date(2025, 12, 25)

# result = date2 - date1
# print(result)

 

#109. Write a Python program to get the difference between a given number and 17.
# n = int(input("enter a number: "))

# if n > 17:
#    print(2 * (n-17))
# else:
#    print(17 -n)   



# 108.Write a Python program to test whether a number is within 100 of 1000 or 2000.

# n = int(input("enter a number: "))
# if (1000 - n) <=100 or (2000 - n) <=100:
#     print("number is within 100 ")
# else:    
#     print("number is without 100")



# 109. Write a Python program to calculate the sum of three given numbers. If the values are equal, return triple their sum.

# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# c = int(input("enter third number: "))

# if a==b==c:
#     print(3 * (a + b + c))
# else:
#     print(a + b + c)



# 110.Write a Python program to get a newly-generated string from a given string where “Is” has been added to the front.

# def new_string(text):
#     if text.startswith("Is"):
#         return text
#     else:
#         return "Is" + text

# # Example usage:
# user_input = input("Enter a string: ")
# print("Result:", new_string(user_input))



#111. Write a Python program to concatenate all elements in a list into a string and return it.

# def list_to_string (lst):
#     return ''.join(lst)

# sample_list = ['P', 'Y', 'T', 'H', 'O', 'N']
# print(list_to_string(sample_list))



# 112.What will be the output of the following code?

# a = "10"
# b = 10
# print(a == str(b))



# 113.Write a Python program to calculate the sum of all numbers from 1 to a given number.

# num = 10
# total = 0
# for i in range(1, num + 1):
#     total += i
# print("sum is:", total)



# 114.Write a Python program to find the maximum and minimum values in a list.
# nums = [4, 2, 9, 1, 7]
# print('Maximum:', max(nums))
# print('Minimum:', min(nums))



# 115.What will the following code output?
# x = 5
# y = 2.5
# print(type(x + y))



# 116.Write a Python program to check if a number is even or odd.
# num = 13
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")



# 117.Write a Python program to get the ASCII value of a character.
# char = 'A'
# ascii_value = ord(char)
# print(ascii_value)



# 118.Write a Python program to print the sum of two numbers entered by the user.
# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))
# value = num1 + num2
# print(value)



# 119.Write a Python program to check if a number is even or odd.
# num = int(input("enter a number: "))
# if num % 2 == 0:
#     print("even number")
# else:
#     print("odd number")



# 120.What will be the output of the following code?
# x = [1, 2, 3]
# print(x * 2)



# 121.Write a Python program to print the Fibonacci series up to n terms.
# n = int(input("enter number of terms: "))
# a, b = 0, 1
# count = 0

# while count < n:
#     print(a, end="")
#     a, b = b, a + b
#     count += 1



# 122.Write a program to print all numbers from 0 to 6 except 3 and 6.
# for i in range(7):
#     if i == 3 or i == 6:
#         continue
#     print(i, end="")



# 123.Write a Python program to convert a string to a list of words.
# text = "Python is fun to learn"
# word_list = text.split()
# print(word_list)



# 124.Write a program to count the total number of digits in a number.

# num = 75869
# count = 0
# while num != 0:
#     num //= 10
#     count += 1
# print("total digits:", count)



# 125.Write a program to check if the given number is a palindrome number.
# num = 121
# temp = num
# rev = 0

# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10

# if temp == rev:
#     print("Palindrome number")
# else:
#     print("Not a palindrome")



# 126.Write a Python program to check if the first and last number of a list is the same.
# def check_first_last(nums):
#     return nums[0] == nums[-1]

# print(check_first_last([10, 20, 30, 10]))
# print(check_first_last([1, 2, 3]))




# 127.Write a Python program to determine the largest and smallest integers, longs, and floats.
# import sys

# print("Max integer:", sys.maxsize)
# print("Min integer:", -sys.maxsize - 1)

# print("Max float:", sys.float_info.max)
# print("Min float:", sys.float_info.min)



# 128.Write a Python program to check whether multiple variables have the same value.
# x = 10
# y = 10
# z = 10

# if x == y == z:
#     print("All variables have the same value.")
# else:
#     print("Variables have different values.")



# 129.Write a Python program to sum all counts in a collection.
# from collections import Counter

# colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
# color_counter = Counter(colors)

# total = sum(color_counter.values())

# print("Total count of all items:", total)



# 130.Write a Python program to check whether an integer fits in 64 bits.
# def fits_in_64_bits(n):
#     return -(2**63) <= n <= 2**63 - 1

# # Example usage:
# num = int(input("Enter an integer: "))
# if fits_in_64_bits(num):
#     print("The number fits in 64 bits.")
# else:
#     print("The number does NOT fit in 64 bits.")




# 131.Write a Python program to check whether lowercase letters exist in a string.
# def contains_lowercase(s):
#     return any(char.islower() for char in s)

# # Example usage:
# text = input("Enter a string: ")
# if contains_lowercase(text):
#     print("The string contains lowercase letters.")
# else:
#     print("The string does NOT contain any lowercase letters.")



# 132.Write a Python program that uses double quotes to display strings.
# text = "He said, \"Python is fun!\""
# print(text)



# 133.Write a Python program to split a variable length string into variables.
# data = "Pradip More 25"
# first_name, last_name, age = data.split()
# print("First Name:", first_name)
# print("Last Name:", last_name)
# print("Age:", age)



# 134.Write a Python program to calculate the time the program runs
# import time

# start_time = time.time()

# for i in range(1000000):
#     pass

# end_time = time.time()

# print("Program runtime:", end_time - start_time, "seconds")



# 135.Write a Python program to input two integers on a single line.
# x, y = map(int, input("Enter two integers separated by space: ").split())
# print("First number:", x)
# print("Second number:", y)



# 136.Write a Python program to print a variable without spaces between values.

# x = 30
# print('Value of x is "' + str(x) + '"')



# 137.Write a Python program to find the maximum of three numbers.
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# print("Max:", max(a, b, c))



# 138.Write a Python program to check if a string is a palindrome.
# s = input("Enter string: ")
# print("Palindrome?" , s == s[::-1])



# 139.Write a Python program to sum all the items in a list.
# numbers = [1, 2, 3, 4, 5]
# print("Sum:", sum(numbers))



# 140. Check if a number is positive, negative, or zero
# num = int(input("Enter a number: "))
# if num > 0:
#     print("Positive")
# elif num == 0:
#     print("Zero")
# else:
#     print("Negative")



# 141. Count vowels in a given string
# text = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# count = sum(1 for char in text if char in vowels)
# print("Number of vowels:", count)



# 142. Swap two variables without using a third variable
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# a, b = b, a
# print("After swapping: a =", a, ", b =", b)



# 143. Write a Python program to find the second smallest number in a list.
# def second_smallest(numbers):
#     unique_nums = list(set(numbers))
#     unique_nums.sort()
#     return unique_nums[1]

# print(second_smallest([3, 1, 4, 1, 5, 2]))



# 144. Write a Python program to calculate the length of a string without using len()
# s = "Python"
# count = 0
# for char in s:
#     count += 1
# print("Length:", count)



# 145. Write a Python program to check if a dictionary is empty.
# d = {}

# if not d:
#     print("Dictionary is empty")
# else:
#     print("Dictionary is not empty")



# 146. Write a Python program to concatenate dictionaries.
# d1 = {'a': 1}
# d2 = {'b': 2}
# d3 = {'c': 3}

# result = {**d1, **d2, **d3}
# print(result)



# 147. Write a Python program to remove duplicates from a dictionary.
# d = {'a': 1, 'b': 2, 'c': 1}
# result = {}
# for key, value in d.items():
#     if value not in result.values():
#         result[key] = value
# print(result)




# 148. Write a Python program to convert a list of tuples into a dictionary.
# t = [('a', 1), ('b', 2)]
# d = dict(t)
# print(d)



# 149. Write a Python program to create a dictionary from two lists.
# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# d = dict(zip(keys, values))
# print(d)



# 150. Write a Python program to check if a key exists in a dictionary.
# d = {'a': 1, 'b': 2}
# key = 'b'
# print(key in d)



# 151. How do you remove an item from a list by value?
# my_list = [1, 2, 3, 4]
# my_list.remove(3)
# print(my_list)



# 152. Write a Python program to remove all whitespace from a string.
# s = " P y t h o n "
# s = s.replace(" ", "")
# print(s)



# 153. Write a Python program to find the largest number in a list.
# nums = [3, 6, 2, 8, 4]
# print("Max:", max(nums))



# 154. Write a Python program to print even numbers from a list.
# nums = [1, 2, 3, 4, 5, 6]
# evens = [n for n in nums if n % 2 == 0]
# print(evens)



# 155. Write a Python program to merge two lists into a set.
# l1 = [1, 2, 3]
# l2 = [3, 4, 5]
# merged = set(l1 + l2)
# print(merged)



# 156. Write a Python program to check if a number is even or odd.
# n = int(input("Enter a number: "))
# print("Even" if n % 2 == 0 else "Odd")



# 157. Write a Python program to convert a list of strings to uppercase.
# words = ["hello", "world"]
# upper = [word.upper() for word in words]
# print(upper)



# 158. Write a Python program to convert a string to a list of characters.
# s = "python"
# char_list = list(s)
# print(char_list)



# 159. Write a Python program to count the number of digits in an integer.
# num = 12345
# count = len(str(abs(num)))
# print("Number of digits:", count)



# 160. Write a Python program to print the numbers from 1 to 100, skipping 3 and 7.
# for i in range(1, 101):
#     if i in (3, 7):
#         continue
#     print(i, end=" ")



# 161. Write a Python program to count uppercase and lowercase letters in a string.
# text = "PyThOn"
# upper = sum(1 for c in text if c.isupper())
# lower = sum(1 for c in text if c.islower())
# print("Uppercase:", upper)
# print("Lowercase:", lower)



# 162. Write a Python program to convert a list into a comma-separated string.
# lst = ['apple', 'banana', 'cherry']
# result = ', '.join(lst)
# print(result)



# 163. Write a Python program to print the Fibonacci sequence up to n terms.
# n = 7
# a, b = 0, 1
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b



# 164. How do you create a list with numbers from 1 to 5

# lst = list(range(1, 6))
# print(lst)



# 164. Write a Python program to find common elements between two lists
# a = [1, 2, 3]
# b = [2, 3, 4]
# common = list(set(a) & set(b))
# print(common)



# 165. Write a Python program to check if a number is positive, negative or zero.
# num = int(input("Enter number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")



# 166. Write a Python program to convert a list of integers to a single integer.
# nums = [1, 2, 3]
# result = int("".join(map(str, nums)))
# print(result)  



# 167. Write a Python program to get the smallest number from a list.
# nums = [4, 1, 8, 3]
# print(min(nums))



# 168. Write a Python program to find the sum of even numbers in a list.
# nums = [1, 2, 3, 4, 5, 6]
# even_sum = sum(n for n in nums if n % 2 == 0)
# print(even_sum)



# 169. Write a Python program to count words in a sentence.

# sentence = "Python is fun to learn"
# words = sentence.split()
# print("Word count:", len(words))



# 170. Write a Python program to reverse the words in a sentence.
# sentence = "Python is awesome"
# reversed_sentence = ' '.join(sentence.split()[::-1])
# print(reversed_sentence)



# 171. Write a Python program to count the occurrence of each word in a sentence.
# sentence = "hello world hello"
# words = sentence.split()
# counts = {word: words.count(word) for word in set(words)}
# print(counts)



# 172. Write a Python program to check if a string ends with a given suffix.
# s = "python programming"
# print(s.endswith("ing"))  



# 173. What does the strip() method do?
# s = "  hello  "
# print(s.strip()) 



# 174. What is the output of this code?
# a = 10
# b = 5
# print(a > b and b < a)



# 175. Write a Python program to get the difference between two sets.
# a = {1, 2, 3, 4}
# b = {3, 4, 5}
# diff = a - b
# print(diff)  



# 176. Write a Python program to check if a string contains only alphabets.
# s = "Python"
# print(s.isalpha()) 



# 177. Write a Python program to sort a list of strings alphabetically.
# words = ['banana', 'apple', 'cherry']
# words.sort()
# print(words)



# 178. Write a Python program to check whether an element exists in a list.
# nums = [1, 2, 3]
# print(2 in nums) 



# 179. Write a Python program to calculate the average of a list.
# nums = [10, 20, 30]
# average = sum(nums) / len(nums)
# print(average)



# 180. Write a Python program to convert all lowercase letters to uppercase in a string.
# text = "hello"
# print(text.upper())



# 181. Write a Python program to find the last element of a list.
# lst = [1, 2, 3]
# print(lst[-1])



# 182. Write a Python program to print a pattern like a triangle with stars.
# n = 5
# for i in range(1, n + 1):
#     print('*' * i)



# 183. Write a Python program to convert a tuple to a string.
# t = ('P', 'y', 't', 'h', 'o', 'n')
# s = ''.join(t)
# print(s)


# 184.Write a Python program to convert a list of tuples into a dictionary where the first element is the key.
# data = [(1, 'one'), (2, 'two'), (3, 'three')]
# d = dict(data)
# print(d)



# 185. Write a Python program to get the frequency of elements in a list using a dictionary.
# lst = [1, 2, 2, 3, 3, 3]
# freq = {}
# for item in lst:
#     freq[item] = freq.get(item, 0) + 1
# print(freq)



# 186. Write a Python program to remove all non-alphabetic characters from a string.
# import re

# s = "P@#y!t1h$%o^n"
# cleaned = re.sub(r'[^A-Za-z]', '', s)
# print(cleaned)



# 187. Write a Python program to find the length of the longest word in a list.
# words = ["Python", "is", "awesome"]
# longest = max(words, key=len)
# print("Length:", len(longest))



# 188. Write a Python program to iterate over a list and print its index and value.
# items = ['a', 'b', 'c']
# for index, value in enumerate(items):
#     print(index, value)



# 189. Write a Python program to remove the nth index character from a non-empty string.
# def remove_char(s, n):
#     return s[:n] + s[n+1:]

# print(remove_char("Python", 3))  



# 190. Write a Python program to print even numbers between 1 and 50.
# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i, end=" ")



# 191. Write a Python program to print a multiplication table for a number.
# num = 5
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")



# 192. Write a Python program to check if a year is a leap year.
# year = 2024
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")



# 193. Write a Python program to count the number of even and odd numbers in a list.
# nums = [1, 2, 3, 4, 5]
# even = len([n for n in nums if n % 2 == 0])
# odd = len(nums) - even
# print(f"Even: {even}, Odd: {odd}")



# 194. Write a Python program to print a right-angled triangle pattern using numbers.
# n = 5
# for i in range(1, n + 1):
#     print(' '.join(str(j) for j in range(1, i + 1)))



# 195. Write a Python program to get the first and last element of a list.
# lst = [10, 20, 30, 40]
# print("First:", lst[0], "Last:", lst[-1])



# 196. Write a Python program to print all prime numbers between 10 and 50.
# for num in range(10, 51):
#     if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5)+1)):
#         print(num, end=" ")



# 197. Write a Python program to count occurrences of a substring in a string.
# s = "hello world hello"
# print(s.count("hello"))  



# 198. Write a Python program to print only the vowels from a string.
# text = "PyNative Exercises"
# vowels = "aeiouAEIOU"
# result = ''.join([ch for ch in text if ch in vowels])
# print(result)



# 199. Write a Python program to print numbers divisible by 5 from a list.
# nums = [10, 22, 35, 40, 55]
# div5 = [n for n in nums if n % 5 == 0]
# print(div5)



# 200. Write a Python program to count uppercase and lowercase letters in a string.
# s = "Hello World"
# upper = sum(1 for c in s if c.isupper())
# lower = sum(1 for c in s if c.islower())
# print(f"Uppercase: {upper}, Lowercase: {lower}")



# 201. Write a Python program to remove duplicates from a list.
# lst = [1, 2, 2, 3, 4, 4]
# unique = list(set(lst))
# print(unique)



# 202. Write a Python program to convert a list into a comma-separated string.
# lst = ['apple', 'banana', 'cherry']
# s = ', '.join(lst)
# print(s)



# 203. Write a Python program to flatten a nested list.
# nested = [[1, 2], [3, 4], [5]]
# flat = [item for sublist in nested for item in sublist]
# print(flat)



# 204. Write a Python program to reverse the order of items in a dictionary.
# d = {'one': 1, 'two': 2, 'three': 3}
# reversed_d = dict(reversed(list(d.items())))
# print(reversed_d)



# 205. Write a Python program to sort a list of dictionaries by a value.
# data = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 22}]
# sorted_data = sorted(data, key=lambda x: x['age'])
# print(sorted_data)



# 206. Write a Python program to check if all items in a list are of the same type.
# lst = [1, 2, 3]
# print(all(type(x) == type(lst[0]) for x in lst)) 



# 207. Write a Python program to find the common elements between two lists.
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]
# common = list(set(a) & set(b))
# print(common)



# 208. Write a Python program to calculate the sum of digits of a number.
# num = 1234
# total = sum(int(digit) for digit in str(num))
# print(total)



# 209. Write a Python program to print a square pattern using stars.
# n = 4
# for i in range(n):
#     print('* ' * n)



# 210. Write a Python program to create a new list from two lists by selecting odd numbers.
# a = [1, 2, 3]
# b = [4, 5, 6]
# result = [x for x in a + b if x % 2 != 0]
# print(result)



# 211. Write a Python program to find the factorial of a number using a loop.
# n = 5
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print(fact)



# 212. Write a Python program to find the second largest number in a list.
# lst = [5, 2, 8, 1, 9]
# lst.sort()
# print(lst[-2])  



# 213. Write a Python program to remove special characters from a string.
# import re
# s = "Hello@#World!!"
# clean = re.sub(r'[^A-Za-z0-9]', '', s)
# print(clean)



# 214. Write a Python program to convert Celsius to Fahrenheit.
# c = 25
# f = (c * 9/5) + 32
# print(f)



# 215. Write a Python program to reverse the words in a sentence.
# s = "Python is fun"
# reversed_sentence = ' '.join(s.split()[::-1])
# print(reversed_sentence)



# 216. Write a Python program to check if a number is palindrome.
# num = 121
# print(str(num) == str(num)[::-1]) 



# 217. Write a Python program to find the ASCII value of a character.
# char = 'A'
# print(ord(char))  



# 218. Write a Python program to count the occurrences of each word in a given sentence.
# sentence = "this is a test this is only a test"
# words = sentence.split()
# count = {w: words.count(w) for w in words}
# print(count)



# 219. Write a Python program to print the following floating numbers up to 2 decimal places.
# x = 3.1415926
# print("{:.2f}".format(x))



# 220. Write a Python program to calculate body mass index (BMI).
# weight = 70  
# height = 1.75  
# bmi = weight / (height ** 2)
# print("BMI:", round(bmi, 2))



# 221. Write a Python program to get the last element of a list.
# lst = [1, 2, 3, 4]
# print(lst[-1])



# 222. Write a Python program to print numbers from 1 to 10 except 5 and 7.
# for i in range(1, 11):
#     if i in (5, 7):
#         continue
#     print(i)



# 223. Write a Python program to reverse the order of items in a tuple.
# t = (1, 2, 3)
# print(t[::-1])



# 224. Write a Python program to check if a dictionary is empty.
# d = {}
# print(not bool(d))  



# 225. Write a Python program to get the number of vowels in a string.
# s = "PyNative"
# vowels = 'aeiouAEIOU'
# count = sum(1 for c in s if c in vowels)
# print(count)



# 226. Write a Python program to find the square of all even numbers from 1 to 10.
# print([x**2 for x in range(1, 11) if x % 2 == 0])



# 227. Write a Python program to find if a given list has a sublist.
# main = [1, 2, 3, 4, 5]
# sub = [3, 4]
# print(str(sub)[1:-1] in str(main)[1:-1])



# 228. Write a Python program to generate a list of all prime numbers between 1 and 50.
# primes = []
# for num in range(2, 51):
#     if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
#         primes.append(num)
# print(primes)



# 229. Write a Python program to remove a newline in Python. 
# text = "Hello World\n"
# print(text.rstrip())



# 230.Write a Python program to check whether a string contains all letters of the alphabet.
# import string

# def is_pangram(s):
#     return set(string.ascii_lowercase) <= set(s.lower())

# print(is_pangram("the quick brown fox jumps over the lazy dog"))



# 231. Write a Python program to print yesterday, today, and tomorrow.
# import datetime
# today = datetime.date.today()
# yesterday = today - datetime.timedelta(days=1)
# tomorrow = today - datetime.timedelta(days=1)

# print("yesterday:", yesterday)
# print("today:", today)
# print("tomorrow:", tomorrow)



# 232. Write a Python program to get the name of the operating system.
# import os
# print(os.name)



# 233. Write a Python program to count occurrences of a substring in a string.
# text = "hello world, hello python"
# print(text.count("hello"))



# 234. Write a Python program to get the current username.
# import getpass
# print(getpass.getuser())



# 235. Write a Python program to extract the file extension from a filename.
# filename = "example.txt"
# print("extension:", filename.split(".")[-1])



# 236.Which of these will raise an error?
# mylist = [1, 2, 3]
# print(mylist[3])


# 237.Which operator is used to check identity?
# a = b = [1, 2]
# print(a is b)



# 238. Convert a string to a list of characters.
# s = "hello"
# char_list = list(s)
# print(char_list)



# 239. Replace all occurrences of a specific word in a string.
# text = "one one was a race horse"
# new_text = text.replace("one", "two")
# print(new_text)



# 240. Reverse each word in a string.
# sentence = "Hello World"
# reversed_words = ' '.join(word[::-1] for word in sentence.split())
# print(reversed_words)



# 241. Count vowels in a string.
# vowels = "aeiouAEIOU"
# text = "PyNative is a great resource"
# count = sum(1 for ch in text if ch in vowels)
# print("Vowel count:", count)



# 242. Write a function to return even numbers from a list.
# def get_even(nums):
    # return [n for n in nums if n % 2 == 0]

# print(get_even([1, 2, 3, 4, 5, 6]))



# 243. Swap first and last elements of a list.
# lst = [10, 20, 30, 40]
# lst[0], lst[-1] = lst[-1], lst[0]
# print(lst)



# 241. Write a function to return the largest of three numbers.
# def largest(a, b, c):
#     return max(a, b, c)

# print(largest(10, 25, 15))



# 242. Remove duplicate characters from a string.
# s = "pynative"
# result = ""
# for char in s:
#     if char not in result:
#         result += char
# print(result)



# 243. Calculate factorial using a loop.
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)



# 244. Write a Python program to count digits in a number.
# num = 123456
# count = 0
# while num:
#     num //= 10
#     count += 1
# print("Digits:", count)



# 245. Create a list of the first letters of every word in a string.
# text = "Python is powerful"
# first_letters = [word[0] for word in text.split()]
# print(first_letters)



# 246. Find the second smallest number in a list.
# nums = [5, 1, 3, 2, 4]
# nums.sort()
# print(nums[1])



# 247. Convert a list of multiple integers into a single integer.
# nums = [1, 2, 3]
# result = int("".join(map(str, nums)))
# print(result)



# 248. Count the number of occurrence of a specific character in a string.
# s = "hello world"
# print(s.count('l'))



# 249. Write a Python program to get the ASCII value of a character.
# char = 'A'
# print("ASCII value of", char, "is", ord(char))



# 250. What will this return?
# x = "Python"
# print(x[-1])



# 251. What is the result of this slice?
# text = "PyNative"
# print(text[2:5])



# 252. Count the number of occurrences of a specific character in a string.
# s = "PyNative"
# print(s.count('a'))



# 253. Reverse a list using slicing.
# my_list = [1, 2, 3, 4]
# print(my_list[::-1])



# 254. How to convert a string into a list of words?
# s = "Python is fun"
# print(s.split())



# 255. How to check if all characters in a string are digits?
# num = "12345"
# print(num.isdigit())



# 256. What is the output?
# s = "Pynative"
# print(s.upper())



# 257. What is the output of:
# x =[1, 2]
# y = [3, 4]
# print(x + y)



# 258. Swap two variables without a third variable.
# a = 5
# b = 10
# a, b = b, a
# print(a, b)



# 259. Write a Python program to check if a number is positive, negative or zero.
# num = float(input("Enter a number: "))
# if num > 0:
#     print("number is positive")
# elif num == 0:
#     print("zero")
# else:
#     print("number is negative") 



# 260. How do you create a list of even numbers from 0 to 10 in Python?
# evens = [i for i in range(11) if i % 2 == 0]
# print(evens)



# 261. Write a Python program to convert a list of integers to a single integer.
# nums = [1, 2, 3]
# result = int("".join(map(str, nums)))
# print(result)



# 262. Replace all spaces in a string with underscores.
# text = "hello world python"
# print(text.replace(" ", "_"))



# 263. Merge two dictionaries.
# a = {'x': 1}
# b = {'y': 2}
# merged = {**a, **b}
# print(merged)



# 264. Get the square root of a number using math module.
# import math 
# print(math.sqrt(49))



# 265. Write a program to get the ASCII value of a character.
# char = 'A'
# print("the ASCII value of", char, "is", ord(char))



# 266. What will the following slice do?
# x = [1, 2, 3, 4, 5]
# print(x[1:-1])



# 267. Write a Python program to print the square and cube of a number.
# num = 4
# print("Square:", num ** 2)
# print("Cube:", num ** 3)



# 268. Write a Python program to print all even numbers from 1 to 10.
# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i, end=' ')



# 269. Write a Python program to count the number of vowels in a string.
# text = "PyNative"
# vowels = "aeiouAEIOU"
# count = 0
# for char in text:
#     if char in vowels:
#         count += 1
# print("vowel count:", count)        



# 270. Create a dictionary from two lists.
# keys = ['name', 'age']
# values = ['Pradip', 25]
# my_dict = dict(zip(keys, values))
# print(my_dict)



# 271. Check if a list is empty.
# my_list = []
# if not my_list:
#     print("Empty List")



# 272. Remove all spaces from a string.
# text = "Hello World"
# print(text.replace(" ", ""))



# 273. Write a Python program to reverse a list.
# my_list = [1, 2, 3, 4]
# my_list.reverse()
# print(my_list)



# 274. Write a Python program to get the file extension from a filename.
# filename = "example.txt"
# extension = filename.split('.')[-1]
# print("Extension:", extension)



# 275. Write a Python program to find the maximum and minimum values in a list.
# nums = [10, 20, 5, 8, 35]
# print("Max:", max(nums))
# print("Min:", min(nums))



# 276.Write a Python program to check if a given key exists in a dictionary.
# sample_dict = {'a': 1, 'b': 2}
# key = 'b'
# print(key in sample_dict)



# 277. Write a Python program to count the number of characters in a string.
# text = "hello world"
# print("Character count:", len(text))



# 278. How to convert a list of strings to a single string?
# words = ['Python', 'is', 'awesome']
# result = ' '.join(words)
# print(result)



# 279. Write a Python program to check if a string starts with a given prefix.
# text = "GeeksforGeeks"
# print(text.startswith("Geeks"))



# 280. What does the following list slicing return?
# x = [10, 20, 30, 40, 50]
# print(x[1:4])



# 281. Write a Python program to convert a string to lowercase.
# text = "GFG IS COOL"
# print(text.lower())



# 282. How to copy a list in Python?
# a = [1, 2, 3]
# b = a.copy()
# print(b)



# 283. Write a Python program to repeat a string 3 times.
# s = "Hi"
# print(s * 3)



# 284. Write a Python program to remove duplicate elements from a list.
# nums = [1, 2, 2, 3, 4, 4]
# unique = list(set(nums))
# print(unique)



# 285. Write a Python program to check if a number is a multiple of 3 or 5.
# num = 15
# if num % 3 == 0 or num % 5 == 0:
#     print("Yes")
# else:
#     print("No")



# 286. Write a Python program to check if a list is empty or not.
# a = []
# if not a:
#     print("List is empty")
# else:
#     print("List is not empty")



# 287. Write a Python program to find the common elements between two lists.
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]
# common = list(set(a) & set(b))
# print(common)



# 288. Write a Python program to remove all whitespaces from a string.
# s = " G e e k s "
# clean = s.replace(" ", "")
# print(clean)



# 289. Write a Python program to find the sum of the first n natural numbers.
# n = 5
# total = n * (n + 1) // 2
# print("Sum of first", n, "natural numbers is:", total)



# 290. Write a Python program to find the second largest number in a list.
# nums = [10, 20, 30, 40]
# nums.sort()
# print("Second largest:", nums[-2])



# 291. Write a Python program to print all even numbers from a list.
# num = [1, 4, 5, 6, 7, 8]
# for n in num:
#     if n % 2 == 0:
#      print("number is even")
#     else:
#        print("number is odd",)



# 292. Write a Python program to print only the first 3 characters of a string.
# s = "PyNative"
# first_three = s[slice(0, 3)]
# print("First 3 characters:", first_three)



# 293. Write a Python program to convert a string to title case.
# text = "python programming is fun"
# print(text.title())



# 294. Write a Python program to convert a string to a list of characters.
# s = "Hello"
# char_list = list(s)
# print(char_list)



# 295. Write a Python program to convert a list of characters into a string.
# chars = ['P', 'y', 't', 'h', 'o', 'n']
# s = ''.join(chars)
# print(s)



# 296. Write a Python program to check if a number is a multiple of 3 or 5.
# n = 15
# if n % 3 == 0 or n % 5 == 0:
#     print("Yes")
# else:
#     print("No")



# 297. Write a Python program to reverse a string using slicing.
# s = "geeksforgeeks"
# slice_str = s[::-1]
# print(slice_str)



# 298. Write a Python program to remove all whitespaces from a string.
# s = " G e e k s  f o r  G e e k s "
# no_space = s.replace(" ", "")
# print(no_space)



# 299. Write a Python program to print numbers from 1 to 10 using a while loop.
# i = 1
# while i <= 10:
#     print(i)
#     i += 1



# 300. Write a Python program to count the number of vowels in a string.
# s = "geeksforgeeks"
# vowels = "aeiouAEIOU"
# count = sum(1 for ch in s if ch in vowels)
# print("Vowel count:", count)



# 301. Write a Python program to swap two variables without using a third variable.
# a = 5
# b = 10
# a, b = b, a
# print("a:", a, "b:", b)



# 302. Write a Python program to find the second largest number in a list.
# numbers = [10, 20, 4, 45, 99]
# numbers.sort()
# second_largest = numbers[-2]
# print("Second largest number is:", second_largest)



# 303. Write a Python program to check if a number is a Harshad number.
# num = 18
# digit_sum = sum(int(digit) for digit in str(num))
# if num % digit_sum == 0:
#     print(num, "is a harshad number")
# else:
#     print(num, "is not a harshad number")



# 304. Write a Python program to find the sum of squares of the first n natural numbers.
# n = 5
# total = sum(i**2 for i in range(1, n+1))
# print("sum of squares:", total)



# 305.Write a Python program to check if two strings are anagrams.
# str1 = "listen"
# str2 = "silent"
# if sorted(str1) == sorted(str2):
#     print("anagrams")
# else:
#     print("not anagrams")



# 306. Write a Python program to reverse a number.
# num = 12345
# reverse = int(str(num)[::-1])
# print("Reversed number:", reverse)



# 307. Find the largest of three numbers without using built-in max()
# a, b, c = 12, 25, 18
# largest = a 
# if b > largest:
#     largest = b
# if c > largest:
#     largest = c
# print("Largest number:", largest)    



# 308. Find the largest number in a list without using max()
# numbers = [12, 45, 78, 34, 89, 23]
# largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
# print("Largest number is :", largest)



# 309. Count how many times a digit appears in a number
# num = 1223334444
# digit_to_count = 4
# count = str(num).count(str(digit_to_count))

# print(f"Digit {digit_to_count} appears {count} times.")



# 310. Find the largest number in a list without using max()
# numbers = [12, 45, 78, 34, 89, 23]
# largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
# print("Largest number is:", largest)



# 311. Reverse a number without using slicing
# num = 4567
# rev_num = 0
# while num > 0:
#     digit = num % 10
#     rev_num = rev_num * 10 + digit
#     num //= 10
# print("Reversed number:", rev_num)



# 312. Calculate the sum of digits of a number
# num = 9875
# sum_digits = 0
# for digit in str(num):
#     sum_digits += int(digit)
# print("Sum of digits:", sum_digits)



# 313. Find the factorial of a number using recursion
# def factorial(n):
#     if n == 0 or n ==1:
#         return 1
#     return n * factorial(n-1)
# print("Factorial of 5:", factorial(5))



# 314. Calculate the square root of a number without using math.sqrt()
# num = 16
# sqrt_num = num ** 0.5
# print("square root of", num, "is", sqrt_num)


# 315. Check if a number is prime
# num = 29
# if num %2 == 0 :
#     print("num is not prime")
# else:
#     print("num is prime")



# 316. Count the total number of digits in a number
# num = 75869
# count = 0
# while num > 0:
#     count +=1
#     num //= 10
# print("Total digits:", count)



# 317. Calculate the sum of the first n natural numbers
# n = 10
# total = n * (n + 1) // 2
# print("sum of first", n, "natural numbers is:", total)



# 318. Check if a number is palindrome
# num = 121
# if str(num) == str(num)[::-1]:
#     print(num, "is a palindrome")
# else:
#     print(num, "is not a paqlindrome")



# 319. Calculate the cube of each number in a list
# numbers = [2, 3, 4, 5]
# cubes = [n**3 for n in numbers]
# print(cubes)



# 320. Find the largest among three numbers
# a, b, c = 12, 25, 7
# largest = max(a, b, c)
# print(largest)



# 321. Calculate the area of a circle
# radius = 7 
# area = 3.14159 * radius * radius
# print(area)



# 322. Count the number of vowels in a string
# text = "Hello World"
# vowels = "aeiouAEIOU"
# count = sum(1 for ch in text if ch in vowels)
# print("Number of vowels:", count)



# 323. Merge two dictionaries
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# merged = {**dict1, **dict2}
# print("Merged dictionary:", merged)



# 324. Reverse a list without using slicing
# numbers = [1, 2, 3, 4, 5]
# numbers.reverse()
# print("Reversed list:", numbers)



# 325. Check if a number is even or odd
# num = 7
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")



# 326. Calculate the sum of digits of a number
# num = 1234
# digit_sum = sum(int(d) for d in str(num))
# print("Sum of digits:", digit_sum)



# 327. Convert a string to lowercase
# text = "HELLO WORLD"
# lower_text = text.lower()
# print(lower_text)



# 328. Check if a year is a leap year
# year = 2024
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")



# 329. Remove duplicates from a list
# numbers = [1, 2, 2, 3, 4, 4, 5]
# unique = list(set(numbers))
# print(unique)



# 330. Convert a list of integers to a single concatenated string
# numbers = [1, 2, 3, 4]
# result = ''.join(map(str, numbers))
# print(result)



# 331. Count how many times a word appears in a sentence
# sentence = "the quick brown fox jumps over the lazy dog the the"
# word = "the"
# count = sentence.split().count(word)
# print(count)



# 332. Calculate the area of a triangle
# base = 5
# height = 8
# area = 0.5 * base * height
# print(area)



# 333. Reverse a given string
# text = "Python"
# reversed_text = text[::-1]
# print("Reversed string:", reversed_text)



# 334. Check if a number is positive, negative, or zero
# num = int(input("Enter a number:"))
# if num > 0:
#     print("positive")
# elif num < 0:
#     print("negative")
# else:
#     print("zero")



# 335. Get the length of a list without using len()
# numbers = [1, 2, 3, 4]
# count = 0
# for _ in numbers:
#     count += 1
# print("Length of list:", count)



# 336. Find the smallest element in a list
# numbers = [5, 2, 9, 1, 7]
# smallest = min(numbers)
# print("Smallest element:", smallest)



# 337. Print numbers from 1 to 10 using a while loop
# i = 1
# while i <= 10:
#     print(i, end=" ")
#     i += 1



# 338. Check if a number is even or odd
# num = int(input("enter a number:"))
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")



# 339. Calculate the sum of elements in a list using a loop
# numbers = [1, 2, 3, 4, 5]
# total = 0
# for n in numbers:
#     total += n
# print("Sum of list elements:", total)



# 340. Multiply all numbers in a list
# numbers = [2, 3, 4]
# product = 1
# for n in numbers:
#     product *= n
# print("Product:", product)



# 341. Reverse a list without using built-in functions
# numbers = [1, 2, 3, 4, 5]
# reversed_list = []
# for i in range(len(numbers)-1, -1, -1):
#     reversed_list.append(numbers[i])
# print(reversed_list)



# 342. Find the largest among three numbers
# a, b, c = 12, 7, 15
# largest = a if (a > b and a > c) else (b if b > c else c)
# print("Largest number:", largest)



# 343. Remove all whitespace from a string
# text = "  Hello   World  "
# cleaned = text.replace(" ", "")
# print("Without spaces:", cleaned)



# 344. Convert a decimal number to binary
# num = 13
# binary = bin(num)[2:]
# print("Binary:", binary)



# 345. Remove duplicates from a list while preserving order
# items = [1, 2, 2, 3, 4, 4, 5]
# unique_items = []
# for i in items:
#     if i not in unique_items:
#         unique_items.append(i)
# print("Without duplicates:", unique_items)



# 346.Convert a list of tuples into a dictionary
# pairs = [("a", 1), ("b", 2), ("c", 3)]
# result = dict(pairs)
# print("Dictionary:", result)


# 347.Find the second smallest number in a list
# numbers = [10, 3, 5, 7, 2, 8]
# sorted_nums = sorted(set(numbers))
# second_smallest = sorted_nums[1]
# print("Second smallest:", second_smallest)


# 348.Flatten a list of lists
# nested = [[1, 2], [3, 4], [5, 6]]
# flat = [item for sublist in nested for item in sublist]
# print("Flattened list:", flat)


# 349.Check if a string is a pangram
# import string
# text = "The quick brown fox jumps over the lazy dog"
# alphabet = set(string.ascii_lowercase)
# if alphabet <= set(text.lower()):
#     print("Pangram")
# else:
#     print("Not a pangram")


# 350. Find the intersection of two lists
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# intersection = list(set(list1) & set(list2))
# print("Intersection:", intersection)


# 351.Sort a dictionary by its values (descending)
# data = {"apple": 5, "banana": 2, "cherry": 7}
# sorted_data = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
# print("Sorted dictionary:", sorted_data)



# 352.Remove all occurrences of a given element from a list
# nums = [1, 2, 3, 2, 4, 2, 5]
# element_to_remove = 2
# filtered = [n for n in nums if n != element_to_remove]
# print("After removal:", filtered)



# 353. Generate a list of even numbers between two numbers
# start, end = 4, 14
# evens = [n for n in range(start, end+1) if n % 2 == 0]
# print("Even numbers:", evens)



# 354.Count the frequency of each character in a string
# text = "programming"
# frequency = {}
# for char in text:
#     frequency[char] = frequency.get(char, 0) + 1
# print("Character frequency:", frequency)



# 355.Get the unique elements from a list while preserving order
# items = [1, 2, 2, 3, 1, 4, 3]
# unique_items = []
# for item in items:
#     if item not in unique_items:
#         unique_items.append(item)
# print("Unique elements:", unique_items)



# 356.Check if a key exists in a dictionary
# data = {"name": "Alice", "age": 25}
# key_to_check = "age"
# if key_to_check in data:
#     print(f"Key '{key_to_check}' exists.")
# else:
#     print(f"Key '{key_to_check}' does not exist.")



# 357.Find the factorial of a number using recursion
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)

# print("Factorial of 5:", factorial(5))



# 358.Remove duplicates from a string
# text = "programming"
# result = ""
# for ch in text:
#     if ch not in result:
#         result += ch
# print(result)



# 359.Find the sum of digits of a number
# num = 987
# sum_digits = sum(int(d) for d in str(num))
# print("Sum of digits:", sum_digits)



# 360.Check if a number is prime
# num = 29
# if num > 1:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print(f"{num} is not prime")
#             break
#     else:
#         print(f"{num} is prime")
# else:
#     print(f"{num} is not prime")



# 361. Find the largest element in a list
# nums = [10, 25, 7, 98, 3]
# largest = max(nums)
# print("Largest number:", largest)



# 362.Convert a list of tuples into a dictionary
# pairs = [("a", 1), ("b", 2), ("c", 3)]
# result = dict(pairs)
# print("Dictionary:", result)



# 363.Find the common elements between two lists
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7]
# common = [x for x in list1 if x in list2]
# print("Common elements:", common)



# 364.Find the length of the longest word in a list
# words = ["apple", "banana", "cherry", "watermelon"]
# longest_length = max(len(word) for word in words)
# print("Longest word length:", longest_length)



# 365.Flatten a nested list
# nested = [[1, 2], [3, 4], [5]]
# flat = [item for sublist in nested for item in sublist]
# print("Flattened list:", flat)



# 366.Check if a string is a palindrome ignoring case
# text = "Racecar"
# if text.lower() == text.lower()[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")



# 367.Find the square of each number in a list using map
# nums = [1, 2, 3, 4, 5]
# squares = list(map(lambda x: x**2, nums))
# print("Squares:", squares)



# 368.Find the common prefix among a list of strings
# words = ["interspecies", "interstellar", "interstate"]
# prefix = ""
# for chars in zip(*words):
#     if len(set(chars)) == 1:
#         prefix += chars[0]
#     else:
#         break
# print("Longest common prefix:", prefix)



# 369. Find all substrings of a given string
# text = "abc"
# substrings = [text[i:j] for i in range(len(text)) for j in range(i+1, len(text)+1)]
# print("Substrings:", substrings)



# 370.Convert a list of integers to a single concatenated number
# nums = [4, 5, 6]
# result = int("".join(map(str, nums)))
# print("Concatenated number:", result)



# 371.Check if a number is an Armstrong number
# num = 9474
# power = len(str(num))
# if sum(int(digit) ** power for digit in str(num)) == num:
#     print(f"{num} is an Armstrong number")
# else:
#     print(f"{num} is not an Armstrong number")



# 372.Rotate a list by k positions to the right
# nums = [1, 2, 3, 4, 5]
# k = 2
# rotated = nums[-k:] + nums[:-k]
# print("Rotated list:", rotated)



# 373.Flatten a nested list
# nested = [[1, 2], [3, 4], [5]]
# flat = [item for sublist in nested for item in sublist]
# print("Flattened list:", flat)



# 374.Find all even numbers between two given numbers
# start, end = 4, 15
# evens = [n for n in range(start, end+1) if n % 2 == 0]
# print("Even numbers:", evens)



# 375. Find the second smallest element in a list
# nums = [12, 5, 7, 3, 9]
# unique_nums = sorted(set(nums))
# if len(unique_nums) >= 2:
#     print("Second smallest:", unique_nums[1])
# else:
#     print("List does not have a second smallest element")



# 376.Find the sum of digits of a number
# num = 9875
# digit_sum = sum(int(d) for d in str(num))
# print("Sum of digits:", digit_sum)



# 377.Find the frequency of each element in a list
# nums = [1, 2, 2, 3, 1, 4, 2]
# frequency = {n: nums.count(n) for n in set(nums)}
# print("Frequencies:", frequency)



# 378.Check if all elements in a list are unique
# nums = [1, 2, 3, 4]
# if len(nums) == len(set(nums)):
#     print("All elements are unique")
# else:
#     print("Duplicates found")



# 379.Get the largest and smallest number from a list
# nums = [4, 7, 1, 9, 12, -3]
# print("Largest:", max(nums))
# print("Smallest:", min(nums))



# 380.Multiply all numbers in a list
# nums = [2, 3, 4]
# result = 1
# for n in nums:
#     result *= n
# print("Product of list elements:", result)



# 381.Remove duplicate characters from a string
# text = "programming"
# result = "".join(sorted(set(text), key=text.index))
# print("Without duplicates:", result)



# 382.Flatten a nested list
# nested = [[1, 2], [3, 4], [5, 6]]
# flat = [item for sublist in nested for item in sublist]
# print("Flattened list:", flat)



# 383.Replace all spaces in a string with underscores
# text = "Hello World from Python"
# modified = text.replace(" ", "_")
# print("Modified string:", modified)



# 384.Count frequency of each element in a list
# nums = [1, 2, 2, 3, 3, 3]
# freq = {n: nums.count(n) for n in set(nums)}
# print("Frequencies:", freq)



# 385.Remove all punctuation from a string
# import string

# text = "Hello!!! Are you there?"
# cleaned = "".join(ch for ch in text if ch not in string.punctuation)
# print("Without punctuation:", cleaned)



# 386.Count the number of uppercase letters in a string
# text = "Hello World!"
# uppercase_count = sum(1 for ch in text if ch.isupper())
# print("Uppercase letters:", uppercase_count)



# 387.Find numbers divisible by 7 in a range
# divisible_by_7 = [n for n in range(1, 51) if n % 7 == 0]
# print("Numbers divisible by 7:", divisible_by_7)



# 388.Remove all occurrences of a specific element from a list
# nums = [1, 2, 3, 2, 4, 2, 5]
# element_to_remove = 2
# result = [n for n in nums if n != element_to_remove]
# print("List after removal:", result)



# 389. Convert a list of tuples into a dictionary
# pairs = [("a", 1), ("b", 2), ("c", 3)]
# result = dict(pairs)
# print("Dictionary:", result)



# 390.Find the maximum key in a dictionary
# data = {5: "apple", 8: "banana", 2: "cherry"}
# max_key = max(data)
# print("Maximum key:", max_key)



# 391.Remove all None values from a list
# data = [1, None, 2, None, 3, 4, None]
# filtered = [x for x in data if x is not None]
# print("List without None:", filtered)



# 392.Find the largest element in a list
# nums = [10, 20, 30, 5]
# print(max(nums))



# 393.Remove duplicates from a list while preserving order
# nums = [1,2,2,3,4,3]
# unique = []
# for n in nums:
#     if n not in unique:
#         unique.append(n)
# print(unique)



# 394.Count occurrences of each element in a list
# nums = [1, 2, 2, 3, 3, 3]
# count_dict = {}
# for n in nums:
#     count_dict[n] = count_dict.get(n, 0) + 1
# print(count_dict)



# 395.Convert a string to title case
# text = "python programming language"
# print(text.title())



# 396.Reverse the words in a sentence
# sentence = "Python is fun"
# reversed_sentence = " ".join(sentence.split()[::-1])
# print(reversed_sentence)



# 397.Get the ASCII value of a character
# char = 'A'
# print(ord(char))



# 398.Calculate the sum of digits of a number
# num = 1234
# digit_sum = sum(int(d) for d in str(num))
# print(digit_sum)



# 399.Flatten a nested list
# nested = [[1, 2], [3, 4], [5]]
# flat = [item for sublist in nested for item in sublist]
# print(flat)



# 400.Find all even numbers in a list
# nums = [1, 2, 3, 4, 5, 6]
# evens = [n for n in nums if n % 2 == 0]
# print(evens)



# 401.Convert a string to a list of characters
# text = "hello"
# chars = list(text)
# print(chars)



# 402.Write a Python program to display all prime numbers within a range.
# start = int(input("Enter start: "))
# end = int(input("Enter end: "))

# for num in range(start, end+1):
#     if num > 1:
#         for i in range(2, int(num**0.5)+1):
#             if num % i == 0:
#                 break
#         else:
#             print(num, end=" ")



# 403.Write a Python program to remove duplicates from a list while preserving order.
# items = [1, 2, 2, 3, 4, 4, 5]
# unique_items = []
# for item in items:
#     if item not in unique_items:
#         unique_items.append(item)

# print("Unique List:", unique_items)



# 404.Write a Python program to find the second smallest number in a list.
# numbers = [5, 1, 8, 3, 2]
# numbers.sort()
# second_smallest = numbers[1]
# print("Second smallest number:", second_smallest)



# 405.Write a Python program to create a dictionary from two lists.
# keys = ['name', 'age', 'city']
# values = ['John', 25, 'New York']

# my_dict = dict(zip(keys, values))
# print(my_dict)



# 406. Write a Python program to print all even numbers from 1 to 20.
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i, end=" ")



# 407.Write a Python program to check whether a number is prime.
# num = 13
# if num > 1:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")
# else:
#     print("Not Prime")



# 408. Write a Python program to find the factorial of a number.
# num = 5
# fact = 1
# for i in range(1, num+1):
#     fact *= i
#     print("Factorial:", fact)



# 409. Write a Python program to reverse a string without using slicing.
# text = "Python"
# reversed_text = "".join(reversed(text))
# print(reversed_text)



# 410.Write a Python program to count the number of digits in a number.
# num = 987654
# count = len(str(num))
# print("Digits:", count)



# 411.Write a Python program to check if a string starts and ends with the same character.
# text = input("enter a text:")
# if text[0] == text[-1]:
#     print("yes")
# else:
#     print("no")    



# 412.Write a Python program to find the largest of three numbers without using max().
# a, b, c = 10, 25, 15
# if a >= b and a >= c:
#     largest = a
# elif b >= a and b >= c:
#     largest = b
# else:
#     largest = c
# print("Largest:", largest)



# 413.Write a Python program to find the second smallest number in a list.
# nums = [12, 5, 8, 3, 15]
# nums_sorted = sorted(nums)
# second_smallest = nums_sorted[1]
# print(second_smallest)



# 414. Write a Python program to multiply all items in a list.
# nums = [2, 3, 4]
# product = 1

# for num in nums:
#     product *= num

# print(product)



# 415.Write a Python program to get unique values from a list.
# my_list = [1, 2, 2, 3, 4, 4, 5]
# unique_list = list(set(my_list))
# print("Unique values:", unique_list)



# 416. Write a Python program to print even numbers from 1 to 20.
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i, end=" ")



# 417.Write a Python program to find the sum of digits of a number.
# num = int(input("Enter a number: "))
# digit_sum = sum(int(d) for d in str(num))
# print(digit_sum)



# 418.Write a Python program to get the smallest number from a list.
numbers = [5, 10, 3, 8, 2, 7]
smallest = min(numbers)
print("Smallest number:", smallest)




























       



























































