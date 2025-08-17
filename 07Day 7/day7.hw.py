
# lst = ["Mango", "Banana", "Dragonfruit", "Apple", "Grapes"]
# print(lst)



# lst = ["Mango", "Banana", "Dragonfruit", "Apple", "Grapes"]
# print(lst[2])



# lst = ["Mango", "Banana", "Dragonfruit", "Apple", "Grapes"]
# print(lst[-1])



# lst = ["Mango", "Banana", "Dragonfruit", "Apple", "Grapes"]
# lst.insert(2, "Grapes")
# print(lst)


# lst = ["Mango", "Banana", "Dragonfruit", "Apple", "Grapes"]
# lst.append("Mango")
# print(lst)


# lst = ["Mango", "Banana", "Dragonfruit", "Apple", "Grapes"]
# lst.insert(0, "Kiwi")
# print(lst)


# lst = ["Mango", "Banana", "Dragonfruit", "Apple", "Grapes"]
# lst.append("Mango")
# print(lst)


# lst = ["Mango", "Banana", "Dragonfruit", "Apple", "Grapes"]
# del lst[0:2]
# print(lst)


# lst = ["Mango", "Banana", "Dragonfruit", "Apple", "Grapes"]
# del lst[0:3]
# print(lst)


# lst = ["Mango", "Banana", "Dragonfruit", "Apple", "Grapes"]
# print(len(lst))


# lst = ["Mango", "Banana", "Dragonfruit", "Apple", "Grapes"]
# lst_Fruits = "Apple" in lst
# print(lst_Fruits)
# lst_Fruits = "Apple" is not lst
# print(lst_Fruits)


# lst = [10, 20, 30, 40, 50]
# lst.append(60)
# print(lst)

# lst = [10, 20, 30, 40, 50]
# lst.insert(2, 25)
# print(lst)


# lst = [10, 20, 30, 40, 50]
# lst.remove(40)
# print(lst)

# lst = [10, 20, 30, 40, 50]
# remove = lst.pop()
# print(lst, remove)


# lst = [10, 20, 30, 40, 50]
# lst.clear()
# print(lst)


# lst =  [1, 5, 2, 8, 3]
# lst.sort()
# print(lst)


# lst =  [1, 5, 2, 8, 3]
# lst.sort(reverse= True)
# print(lst)


# lst = ["A", "C", "B"]
# lst.sort()
# print(lst)


# lst = ["Red", "Green", "Blue"]
# lst.reverse()
# print(lst)


# lst = [1, 2, 2, 3, 4, 2]
# lst1 = lst.count(2)
# print(lst1)


# list_a = [1, 2]
# list_b = [3, 4]
# list_c = list_a + list_b
# print(list_c)


# list_d = ["a", "b"]
# list_e = ["c", "d"]
# list_d.extend(list_e)
# print(list_d)


# lst1 = [25,30,40]
# lst1.append([45, 46])
# print(lst1)
# lst1.extend([45, 46])
# print(lst1)


# my_list = [1, 2, 3]
# new_list = my_list
# new_list.append(4)
# print(new_list)


# my_list = [1, 2, 3]
# copy_list = my_list.copy()
# copy_list.append(4)
# print(my_list)
# print(copy_list)



# lst = ["Red", "Green", "Blue"]
# for i in lst:
#     print(i, end=" ")


# lst = [1, 2, 3, 4, 5]
# for i in lst:
#     print(i**2, end=", ")


# lst = [1, 2, 3, 4, 5]
# largest_number = lst[0]
# for i in lst:
#     if i > largest_number:
#         largest_number = i
# print(largest_number)


# lst = [1, 2, 3, 4, 5]
# for i in lst:
#     print(i ** 2, end=", ")


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = [num for num in lst if num % 2 == 0]
# print(even_numbers)


# lst = ["a", "e", "i", "o", "u"]
# word = input("ente a name:")
# count = 0
# for letter in word:
#     if letter in lst:
#         count += 1
# print("number of vowels in the word: ", count)


# str = "Python"
# reverse_str = ''.join(reversed(str))
# print(reverse_str)


# lst = [1, 2, 3, 4, 5]
# total =0 
# for i in lst:
#      total += i
# print(total)


# lst = [10, 20, 30, 40, 50]
# smallest = lst[0]
# for num in lst:
#     if num < smallest:
#         smallest = lst
# print(smallest)


# lst = [1, 2, 2, 3, 4, 4, 5]
# unique_lst = list(set(lst))
# print(unique_lst)


# board = [['', '', ''],
#          ['', '', ''],
#          ['', '', '']]

# for row in board:
#     print(row)


# secret_lst = [22, 23, 25, 27, 35]
# guess_number = int(input("Guess a number: "))
# if guess_number in secret_lst:
#     print("correct answer")
# else:
#     print("incorrect!, Try again.")    


# user = input("Enter a sentence: ")
# lst = user.split()
# print("List of words:", lst)



# lst = ["I", "am", "Pradip"]
# sentence = " ".join(lst)
# print(sentence)


# number = int(input("enter a number:"))
# factorial = []
# fact = 1
# for i in range(1, number + 1):
#     fact *= i
#     factorial.append(fact)
# print(factorial)


# user = input("Enter word: ")
# lst = list(user)
# if lst == lst[::-1]:
#     print("Palindrome")
# else:
#     print("Not palindrome")


# nested_list =[[1, 2], [3, 4]]
# print(nested_list[1][1])



# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]

# B = [[9, 8, 7],
#      [6, 5, 4],
#      [3, 2, 1]]

# result = [[0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0]]

# for i in range(len(A)):           
#     for j in range(len(A[0])):   
#         result[i][j] = A[i][j] + B[i][j]

# print("Result of Matrix Addition:")
# for row in result:
#     print(row)



# sentence = input("Enter a sentence: ")
# word = sentence.split()
# word_lst = []
# for word in word:
#      word_lst.append([word, word.count(word)])
# print(word_lst)     


# shopping_lst = []
# for i in range(3):
#     user = input("Enter items: ")
#     i +=1
#     shopping_lst.append(user)
# print(shopping_lst)



# def filter_numbers(numbers, threshold):
#     return [num for num in numbers if num > threshold]

# numbers = [1, 5, 8, 2, 10, 3]
# threshold = 5
# filtered_numbers = filter_numbers(numbers, threshold)
# print(filtered_numbers)


# data = ['A', 'B', 'C', 'D', 'E', 'F']
# sublist = data[2:4]
# print(sublist) 
# print(data)


# list1 = ['A', 'B', 'C', 'D']
# try:
#     to_find = list1.index('E')  
#     print(f"Element found at index {to_find}")
# except ValueError:
#     print("Element not found in the list.")


# list1 =[1,4,2,88,5,3,1,7,5,2,9,7]
# value = input("Enter which number have  to remove:")
# while value in list1:
#     list1.remove(value)
# print(f"after removing {value}:", list1)



# list1 = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
# print(list1[1][0])


# list1 = [10, 25, 5, 40, 25, 40]
# unique_list = list(set(list1))
# unique_list.sort(reverse=True)   # Sort the list in descending order
# if len(unique_list) >= 2:
#     second_largest = unique_list[1]
#     print("Second largest number is:", second_largest)
# else:
#     print("List does not have enough distinct elements.")


# def rotate_list(lst, k):
# #     n = len(lst)
# #     k = k % n  # handle cases where k > n
# #     return lst[-k:] + lst[:-k]
# # data = [1, 2, 3, 4, 5]                     
# # rotated = rotate_list(data, 2)
# # print(rotated)


# limit = 20
# primes = []
# for num in range(2, limit + 1):
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.append(num)
# print(primes)


# number = 10
# fib = [0,1]
# for i in range(2,number + 1):
#     fib.append(fib[i -1] + fib[i-2])
#     print(fib)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# transpose = []
# for i in range(len(matrix[0])):  # iterate over columns
#     row = []
#     for j in range(len(matrix)):  # iterate over rows
#         row.append(matrix[j][i])
#     transpose.append(row)
# print(transpose)













