# fruits ={"Apple","Orange","Mange","Banana","Grapes"}
# print("My favoirate fruits:",fruits)


# numbers = {1, 2, 2, 3, 4, 4, 5}
# print(numbers)


# cities = set()
# cities.add("Latur")
# cities.add("Pune")
# cities.add("mumbai")
# cities.add("chennai")
# cities.add("Hydrabad")
# print(cities)



# colors = {"Red", "Voilet", "White"}
# colors.add("Orange")
# colors.add("Yellow")
# print(colors)


# fruits = {"Apple", "Kiwi", "Orange", "Strawberry", "Banana" }
# fruits.remove("Kiwi")
# print(fruits)


# animals = {"Dog", "Elephant", "Cow", "Lion"}
# animals.discard("Cow")
# print(animals)


# animals = {"Dog", "Elephant", "Cow", "Lion"}
# remove_item = animals.pop()
# print(remove_item)



# animals = {"Dog", "Elephant", "Cow", "Lion"}
# animals.clear()
# print(animals)


# subject = {"Hindi", "English", "Marathi", "Math"}
# if "Math" in subject:
#     print("Math in subjects")
# else:
#     print("Math is not in subjects")


# Countries = {"India", "Russia", "Japan", "Canada", "America"}
# country_len = len(Countries)
# print(country_len)


# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 3, 5, 7, 9}
# union = set1 | set2
# print(union)


# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 3, 5, 7, 9}
# intersection = set1 & set2 
# print(intersection)


# name1 = {"Pradip", "Ishwar", "Raman","Ajay"}
# name2 = {"Pradip", "More", "25" }
# difference = name1 - name2
# print(difference)



# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 3, 5, 7, 9}
# symetric = set1.symmetric_difference(set2)
# print(symetric)



# set1 = {2, 4, 6, 8, 10}
# set2 = {1, 3, 5, 7, 9}
# union= set1.union(set2)
# print(union)



# sports1 = {"Cricket", "Football", "Hockey", "Tennis"}
# sports2 = {"Badminton", "Football", "Basketball", "Tennis"}
# common_sports = sports1.intersection(sports2)
# if common_sports:
#     print("Common sports are:", common_sports)
# else:
#     print("No common sports.")


# A = {1, 2, 3}
# B= {1, 2, 3, 4, 5}
# if A.issubset(B):
#     print("A is the subset of B.")
# else:
#     print("A i not subset of B.")



# X = {2, 4, 6, 8}
# Y = {4, 8}
# if  Y.issubset(X):
#     print("Y is the subset of X.")
# else:
#     print("Y is not subset of x")



# set1 = {2, 4, 6, 8, 10}
# set2 = {1, 3, 5, 7, 9}
# if set1.isdisjoint(set2):
#     print("The sets are disjoint")
# else:
#     print("The sets are not disjoint")


# set1 = {1, 2, 3}
# set2 = {4, 5, 6}
# set1.update(set2)
# print("Updated set1 with union of set1 and set2:", set1)



# animals = {"Dog", "Elephant", "Cow", "Lion"}
# for animal in animals:
#     print(animal)



# numbers = {10, 20, 25, 45, 65, 75, 95, 100, 125}
# count = sum(1 for num in numbers if num > 50)
# print(f"Count of elements greater than 50: count")



# Words = {"Dog", "Elephant", "Cow", "Lion"}
# for name in Words:
#     if len(name) >= 5:
#         print(name)



# set1 = {2, 4, 6, 8, 10}
# set2 = {1, 3, 5, 7, 9}
# for item in set2:
#     set1.add(item)
#     print(set1)


# Marks = {75, 80, 85, 90, 95}
# for mark in Marks:
#     if mark >= 90:
#         print(mark)



# set1 = {2, 4, 6, 8, 10}
# set2 = {1, 3, 5, 7, 9}
# common = set()
# for item in set1:
#     if item in set2:   
#         common.add(item)
# print("Common elements:", common)



# numbers = {25, 30, 45, 50, 85}
# largest_number = max(numbers)
# print("Largest number:", largest_number)



# numbers = {25, 30, 45, 50, 85}
# smallest_number = min(numbers)
# print("Smallest number:", smallest_number)



# str = {"Badminton", "Football", "Basketball", "Tennis"}
# longest_str = max(str, key=len)
# print(longest_str)



# str = {"Badminton", "Football", "Basketball", "Tennis"}
# smallest_str = min(str, key=len)
# print(smallest_str)


# numbers = [1, 1, 2, 3, 4, 5, 4, 3, 5, 6, 7, 7]
# unique_num = set([1, 1, 2, 3, 4, 5, 4, 3, 5, 6, 7, 7])
# print(unique_num)




# fruits = ("Apple", "Kiwi", "Orange", "Strawberry", "Banana" )
# fruit_set = set(fruits)
# print(fruit_set)


# Marks = [(85, 90), (75, 80), (90, 95), (70, 75), (85, 90)]
# unique_marks = set(Marks)
# print(unique_marks)


# numbers = {25, 30, 45, 50, 85}
# num_lst = list(numbers)
# num_lst.sort()
# print(num_lst)


# numbers = {25, 30, 45, 50, 85}
# num_tuple = tuple(numbers)
# print(num_tuple)


# cities = {"Latur", "Pune", "Mumbai", "Pune", "Latur"}
# unique_cities = set(cities)
# print(unique_cities)
# print(len(unique_cities))


# roll_numbers = (22, 35, 40, 52, 51)
# roll_num_set = set(roll_numbers)
# roll_no = 52
# if roll_no in roll_num_set:
#     print(f"{roll_no} exist in set")
# else:
#     printt(f"{roll_no} is not exist in set")


# names = ["Pradip", "Utkarsh", "Manoj", "Akshay", "Ishwar"]
# unique_names = set(names)
# sort_name = sorted(unique_names)
# print(sort_name)


# seats = [("s1"), ("s2"), ("s3"), ("s2"), ("s1")]
# unique_seats = list(set(seats))
# print(unique_seats)


# Scores = (325-5, 330-6, 325-5, 340-5, 330-6)
# unique_scores = set(Scores)
# print(unique_scores)








