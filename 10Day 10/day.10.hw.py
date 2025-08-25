# Fruits_Colour = {
#     "Apple": "Red",
#     "Banana": "Yellow",
#     "Guava": "Green"}
# print(Fruits_Colour)


# Countries = {
#     "India": "Delhi",
#     "England": "London",
#     "France": "Paris"
# }
# for capital in Countries.values():
#     print(capital)

# Countries ["Japan"] = "Tokyo"     #add a new country
# for capital in Countries.values(): 
#     print(capital)

# Countries["England"] = "Manchester" #updating the capital
# for capital in Countries.values():
#     print(capital)

# Countries.update({"England": "Manchestar"})  #updating the capital by another method
# for capital in Countries.values():
#     print(capital)


# del Countries["France"]     #deleted the country
# print(Countries)


# print(Countries.keys())  # Print keys

# print(Countries.values())  #print values  

# if "India" in Countries:
#      print("India is present in keys")
# else:
#     print("India is not present in keys")


# Freinds = {
#     "Ishwar": 25,
#     "Utkarsh": 27,
#     "Aditya": 25,
# }

# print(Freinds["Ishwar"])

# Dictionary = {}
# Dictionary["Ishwar"] = 25
# Dictionary["Utkarsh"] = 27
# Dictionary["Aditya"] = 25
# print(Dictionary)


# Fruit = "Banana"

# Fruit_Count = {}
# for fruit in Fruit:
#     if fruit in Fruit_Count:
#         Fruit_Count[fruit] += 1
#     else:
#         Fruit_Count[fruit] = 1
# print(Fruit_Count)

# Students = {
#      "Prathmesh": 95,
#      "Niraj": 72,
#      "Rohit": 38,
#      "Ashish":79,
#      "Abhi":86
# }
# topper_name = " "
# topper_marks = -1 
# for name,marks in Students.items():
#       if marks > topper_marks:
#         topper_marks = marks
#         topper_name = name
# print(topper_name, topper_marks)


# topper = max(Students, key=Students.get)   #another method to find maximum value.
# print(topper, Students[topper])


# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "d": 4}
# d1.update(d2)
# print(d1)

# merged = {**d1, **d2}   # another method for mix
# print(merged)


# Dictionary = {}
# if not Dictionary:
#     print("Dictionary is empty")
# else:
#     print("dictionary is not empty")


# numbers = {1: "One", 2: "Two", 3: "Three"}
# print(numbers[2])

# Squares = { }
# for i in range(1, 6):
#     Squares [i] = i * i
# print(Squares)


# num = {
#     "A": 12,
#     "B": 20,
#     "C": 24,
#     "D": 30
# }

# sum_values = sum(num.values())
# print(sum_values)

# sum_values = 0
# for value in num.values():    #Another method
#     sum_values += value
# print(sum_values)



# my_dict = {
#     "A": 12,
#     "B": 20,
#     "C": 24,
#     "D": 30
# }

# max_value = max(my_dict, key=my_dict.get)
# print(max_value, my_dict[max_value])


# my_dict = {
#     "A": 12,
#     "B": 20,
#     "C": 24,
#     "D": 30
# }
# swapped = {}
# for key, value in my_dict.items():
#     swapped[value] = key
#     print(swapped)



# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "d": 4}

# if d1 == d2 :
#     print("dictionaries are equal")
# else:
#     print("dictionaries are not equal")


# employees = {
#     1: {"name": "thomas", "age": 25, "department": "developer"},
#     2: {"name": "tony", "age": 28, "department": "testing"},
#     3: {"name": "john", "age": 30, "department": "marketing"}
# }

# print(employees[2]["department"])


# Books = {
#     "Wings of fire": "A.P.J Abdul Kalam",
#     "Mrityunjay": "Shivaji Sawant",
#     "Yayati": "V. S. Khandekar"
# }
# for title in Books.keys():
#     print(title)

# Family = {
#     "Dad": "Puran Poli",
#     "Mom": "Pav Bhaji",
#     "Brother": "Biryani",
#     "Me": "Butter Chicken"
# }        

# print(Family["Mom"])


# Sentence = input("enter a sentence:")
# words = Sentence.split()
# word_count = {}
# for word in words :
#     word_count[word] = word_count.get(word, 0) + 1
# print("\nWord Frequency:")
# for word, count in word_count.items():
#     print(f"{word}: {count}")


# marks =  {
#     "Prathmesh": 95,
#     "Niraj": 72,
#     "Rohit": 38,
#     "Ashish":79,
#     "Abhi":86
# }
# Average =  sum(marks.values()) / 4 
# print(Average)


# states = {
#     "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
#     "Karnataka": ["Bengaluru", "Mysuru", "Mangalore"],
#     "Gujarat": ["Ahmedabad", "Surat", "Vadodara"]
# }

# print(states["Maharashtra"])


# Movies = {
#     "ghost rider": 2007,
#     "pushpa": 2021,
#     "rrr": 2022
# }
# for movie, year in Movies.items():
#     if year > 2010:
#         print(movie, year)


# Write a program to remove all duplicate values from a dictionary.
# fruits = {
#     "Apple": 120,
#     "Banana": 40,
#     "Mango": 80,
#     "Grapes": 60
# }
# print("Fruits costing more than 50:")
# for fruit, price in fruits.items():
#     if price > 50:
#         print(fruit, price)


# rooms = {
#     "Kitchen": "Gold",
#     "Dining room": "Silver",
#     "Garden": "Diamond"
# }
# room = input("Enter a room name: ")
# if room in rooms:
#     print(rooms[room])
# else:
#     print("No rooms!")

# Countries = {
#     "India": "New Delhi",
#     "USA": "New York",
#     "France": "Paris",
#     "Japan": "Tokyo"
# }
# country = input("Enter a country name: ")
# if country in Countries:
#     print(Countries[country])
# else:
#     print("Not found in country")


# students = {
#     101: "Aditya",
#     102: "Kiran",
#     103: "Ganesh"
# }
# roll = int(input("Enter roll number: "))
# if roll in students:
#     print(students[roll])
# else:
#     print("Roll number not found")


# dictionary = {
#     "apple": "saib",
#     "water": "pani",
#     "book": "kitab"
# }
# word = input("Enter an English word: ")
# if word in dictionary:
#     print(dictionary[word])
# else:
#     print("Word not found")


# User = {
#     "Red Room": "Gold",
#     "Blue Room": "Diamond"
# }
# Guess = input("Guess the room with treasure: ")
# if Guess in User:
#     print(User[Guess])
# else:
#     print("Wrong guess!")










