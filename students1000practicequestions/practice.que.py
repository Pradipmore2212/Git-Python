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
primes = []
for num in range(2, 51):
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
        primes.append(num)
print(primes)



















































