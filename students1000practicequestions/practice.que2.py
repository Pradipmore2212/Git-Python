
#  Q1. Get the last element of list a = [1, 2, 2, 3, 1].
# a = [1, 2, 2, 3, 1]
# print(a[-1])


#  Q2. Reverse list a = [1, 2, 2, 3, 1] in-place.
# a = [1, 2, 2, 3, 1]
# a.reverse()
# print(a)


#  Q3. Return a sorted copy of a = [1, 2, 2, 3, 1].
# a = [1, 2, 2, 3, 1]
# sorted_list = sorted(a)  
# print(sorted_list)


#  Q4. Append 1 to list a = [1, 2, 2, 3, 1].
# a = [1, 2, 2, 3, 1]
# a.append(1)
# print(a)


#  Q5. Remove first occurrence of 1 from a = [1, 2, 2, 3, 1].
# a = [1, 2, 2, 3, 1]
# a.remove(1)
# print(a)


#  Q6. Get slice of a = [1, 2, 2, 3, 1] from index 1 to 3.
# a = [1, 2, 2, 3, 1]
# slice_a = a[1:4]
# print(slice_a)


#  Q7. Compute sum of a = [1, 2, 2, 3, 1].
# a = [1, 2, 2, 3, 1]
# print(sum(a))


##  Q8. Find unique elements of a = [1, 2, 2, 3, 1] preserving order.
# a = [1, 2, 2, 3, 1]
# unique = []
# for x in a:
#     if x not in unique:
#         unique.append(x)
# print(unique)


# Q9. Merge two lists a=[1, 2, 2, 3, 1] and b=[2, 3, 4, 6, 2].
# a=[1, 2, 2, 3, 1]
# b=[2, 3, 4, 6, 2]

# c = a + b
# print(c)


##  Q10. Find intersection of lists a=[1, 2, 2, 3, 1] and b=[2, 3, 4, 6, 2].
# a=[1, 2, 2, 3, 1]
# b=[2, 3, 4, 6, 2]

# intersection = list(set(a) & set(b))
# print(intersection)


#  Q11. Count occurrences of 1 in a = [1, 2, 2, 3, 1].
# a = [1, 2, 2, 3, 1]
# print(a.count(1))



#  Q12. Replace index 2 in a=[1, 2, 2, 3, 1] with 99.
# a=[1, 2, 2, 3, 1]
# a[2] = 99
# print(a)



#  Q13. Get even numbers from nums = [1, 2, 3, 4, 5, 6].
# nums = [1, 2, 3, 4, 5, 6]
# evens = []
# for i in nums:
#     if i %2 == 0:
#         evens.append(i)
# print(evens)



#  Q14. Square each number in nums = [1, 2, 3, 4, 5, 6].
# nums = [1, 2, 3, 4, 5, 6]
# squares = []
# for i in nums:
#     squares.append(i**2)
# print(squares)



##  Q15. Flatten nested list [[1,2],[3,4],[5]] in one line.
# nested = [[1, 2], [3, 4], [5]]
# result = []
# for sublist in nested:
#     for i in sublist:
#         result.append(i)
# print(result)



#  Q16. Create list of pairs (x, x^2) for nums = [1, 2, 3, 4, 5, 6].

# nums = [1, 2, 3, 4, 5, 6]
# pairs = []
# for i in nums:
#     pairs.append((i, i**2))
# print(pairs)



#  Q17. Rotate list a=[1, 2, 2, 3, 1] right by 2.
# a = [1, 2, 2, 3, 1]
# rotate = a[-2:] + a[:-2]  #slice from index -2 to end and from start to index -2.
# print(rotate)



#  Q18. Get second largest from nums = [1, 2, 3, 4, 5, 6].
# nums = [1, 2, 3, 4, 5, 6]
# second_largest = nums[4:5]
# print(second_largest)



#  Q19. Remove None values from [1,None,2,None,3].
# values = [1,None,2,None,3]
# while None in values: 
#     values.remove(None)
# print(values)


#  Q20. Zip [1, 2, 3, 4, 5, 6] and ['beta', 'gamma', 'delta', 'epsilon', 'zeta'] into list of tuples.
# nums = [1, 2, 3, 4, 5, 6]
# words = ['beta', 'gamma', 'delta', 'epsilon', 'zeta']
# zipped_list = zip(nums, words)
# print(list(zipped_list))

#  Q21. Get the last element of list a = [2, 3, 4, 6, 2].
# a = [2, 3, 4, 6, 2]
# last_element = a.pop()
# print(last_element)


# Q22. Reverse list a = [2, 3, 4, 6, 2] in-place.
# a = [2, 3, 4, 6, 2]
# a.reverse()
# print(a)



#  Q23. Return a sorted copy of a = [2, 3, 4, 6, 2].
# a = [2, 3, 4, 6, 2]
# sorted_copy = sorted(a)
# print(sorted_copy)



#  Q24. Append 2 to list a = [2, 3, 4, 6, 2].
# a = [2, 3, 4, 6, 2]
# a.append(2)
# print(a)



#  Q25. Remove first occurrence of 2 from a = [2, 3, 4, 6, 2].
# a = [2, 3, 4, 6, 2]
# a.remove(2)
# print(a)



#  Q26. Get slice of a = [2, 3, 4, 6, 2] from index 1 to 3.
# a = [2, 3, 4, 6, 2]
# slice_num = a[1:3]
# print(slice_num)



#  Q27. Compute sum of a = [2, 3, 4, 6, 2].
# a = [2, 3, 4, 6, 2]
# print(sum(a))


# Q28. Find unique elements of a = [2, 3, 4, 6, 2] preserving order.
# a = [2, 3, 4, 6, 2]
# unique = []
# for i in a:
#     if i not in unique:
#         unique.append(i)
# print(unique)

# or
# a = [2, 3, 4, 6, 2]
# unique = list(dict.fromkeys(a))
# print(unique)


# Q29. Merge two lists a=[2, 3, 4, 6, 2] and b=[3, 4, 6, 9, 3].
# a = [2, 3, 4, 6, 2]
# b = [3, 4, 6, 9, 3]
# merge_list = a + b 
# print(merge_list)



#  Q30. Find intersection of lists a=[2, 3, 4, 6, 2] and b=[3, 4, 6, 9, 3].
# a = [2, 3, 4, 6, 2]
# b = [3, 4, 6, 9, 3]
# intersection = []
# for i in a:
#     if i in b and i not in intersection:
#         intersection.append(i)
# print(intersection)
# or
# intersection = list(set(a)&set(b))
# print(intersection)


#  Q31. Count occurrences of 2 in a = [2, 3, 4, 6, 2].
# a = [2, 3, 4, 6, 2]
# print(a.count(2))



#  Q32. Replace index 2 in a=[2, 3, 4, 6, 2] with 99.
# a = [2, 3, 4, 6, 2]
# a[2] = 99
# print(a)


#  Q33. Get even numbers from nums = [1, 2, 3, 4, 5, 6, 7].
# nums = [1, 2, 3, 4, 5, 6, 7]
# evens = []
# for i in nums:
#     if i %2 == 0:
#         evens.append(i)
# print(evens)



#  Q34. Square each number in nums = [1, 2, 3, 4, 5, 6, 7].
# nums =[1, 2, 3, 4, 5, 6, 7]
# squares = []
# for i in nums:
#     squares.append(i**2)
# print(squares)



#  Q35. Flatten nested list [[1,2],[3,4],[5]] in one line.
# nested = [[1, 2], [3, 4], [5]]
# flat = sum(nested, [])
# print(flat)



#  Q36. Create list of pairs (x, x^2) for nums = [1, 2, 3, 4, 5, 6, 7].
# nums = [1, 2, 3, 4, 5, 6, 7]
# pairs = []
# for i in nums:
#     pairs.append((i, i ** 2))
# print(pairs)


#  Q37. Rotate list a=[2, 3, 4, 6, 2] right by 2.
# a = [2, 3, 4, 6, 2]
# rotates = a[-2:] + a[:-2]
# print(rotates)


# Q38. Get second largest from nums = [1, 2, 3, 4, 5, 6, 7]
# nums = [1, 2, 3, 4, 5, 6, 7]
# second_largest = nums[5:6]
# print(second_largest)


# Q39. Remove None values from [1,None,2,None,3].
# nums = [1,None,2,None,3]
# while None in nums:
#     nums.remove(None)
# print(None)


#  Q40. Zip [1, 2, 3, 4, 5, 6, 7] and ['gamma', 'delta', 'epsilon', 'zeta', 'eta'] into list of tuples.
# nums = [1, 2, 3, 4, 5, 6, 7]
# word = ['gamma', 'delta', 'epsilon', 'zeta', 'eta']
# zipped_lst = zip(nums, word)
# print(list(zipped_lst))


# Q41. Get the last element of list a = [3, 4, 6, 9, 3].
# a = [3, 4, 6, 9, 3]
# last_element = a.pop()
# print(last_element)


#  Q42. Reverse list a = [3, 4, 6, 9, 3] in-place.
# a = [3, 4, 6, 9, 3]
# a.reverse()
# print(a)


# Q43. Return a sorted copy of a = [3, 4, 6, 9, 3].
# a = [3, 4, 6, 9, 3]
# sort_copy = sorted(a)
# print(a)


# Q44. Append 3 to list a = [3, 4, 6, 9, 3].
# a = [3, 4, 6, 9, 3]
# a.append(3)
# print(a)


# Q45. Remove first occurrence of 3 from a = [3, 4, 6, 9, 3].
# a = [3, 4, 6, 9, 3]
# a.remove(3)
# print(a)


#  Q46. Get slice of a = [3, 4, 6, 9, 3] from index 1 to 3.
# a = [3, 4, 6, 9, 3]
# slice_list = a[1:4]
# print(slice_list)


# Q47. Compute sum of a = [3, 4, 6, 9, 3].
# a = [3, 4, 6, 9, 3]
# print(sum(a))


# Q48. Find unique elements of a = [3, 4, 6, 9, 3] preserving order.
# a = [3, 4, 6, 9, 3]
# unique = []
# for i in a:
#     if i not in unique:
#         unique.append(i)
# print(unique)
# unique = list(dict.fromkeys(a))
# print(unique)


# Q49. Merge two lists a=[3, 4, 6, 9, 3] and b=[4, 5, 8, 12, 4].
# a = [3, 4, 6, 9, 3]
# b = [4, 5, 8, 12, 4]
# merged = a + b
# print(merged)

#  Q50. Find intersection of lists a=[3, 4, 6, 9, 3] and b=[4, 5, 8, 12, 4].
# a = [3, 4, 6, 9, 3]
# b = [4, 5, 8, 12, 4]
# print(list(set(a) & set(b)))


# Q51. Count occurrences of 3 in a = [3, 4, 6, 9, 3].
# a = [3, 4, 6, 9, 3]
# print(a.count(3))


# Q52. Replace index 2 in a=[3, 4, 6, 9, 3] with 99.
# a = [3, 4, 6, 9, 3]
# a[2] = 99 
# print(a)


# Q53. Get even numbers from nums = [1, 2, 3, 4, 5, 6, 7, 8].
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# evens = []
# for i in nums:
#     if i %2 == 0:
#         evens.append(i)
# print(evens)


# Q54. Square each number in nums = [1, 2, 3, 4, 5, 6, 7, 8].
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# squares = []
# for i in nums:
#     squares.append(i ** 2)
# print(squares)


# Q55. Flatten nested list [[1,2],[3,4],[5]] in one line.
# nested = [[1, 2], [3, 4], [5]]
# flat = sum(nested, [])
# print(flat)


#  Q56. Create list of pairs (x, x^2) for nums = [1, 2, 3, 4, 5, 6, 7, 8].
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# pairs = []
# for i in nums:
#     pairs.append((i, i**2))
# print(pairs)


# Q57. Rotate list a=[3, 4, 6, 9, 3] right by 2.
# a = [3, 4, 6, 9, 3]
# rotate = a[-2:] + a[:-2]
# print(rotate)


#  Q58. Get second largest from nums = [1, 2, 3, 4, 5, 6, 7, 8].
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# print(nums[6:7])


#  Q59. Remove None values from [1,None,2,None,3].
# nums = [1, None, 2, None, 3]
# while None in nums:
#     nums.remove(None)
# print(nums) 


# Q60. Zip [1, 2, 3, 4, 5, 6, 7, 8] and ['delta', 'epsilon', 'zeta', 'eta', 'theta'] into list of tuples.
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# word = ['delta', 'epsilon', 'zeta', 'eta', 'theta']
# zipped_lst = zip(nums, word)
# print(list(zipped_lst))


# Q61. Get the last element of list a = [4, 5, 8, 12, 4].
# a = [4, 5, 8, 12, 4]
# print(a[-1])


#  Q62. Reverse list a = [4, 5, 8, 12, 4] in-place.
# a = [4, 5, 8, 12, 4]
# a.reverse()
# print(a)


# Q63. Return a sorted copy of a = [4, 5, 8, 12, 4].
# a = [4, 5, 8, 12, 4]
# sorted_copy = sorted(a)
# print(sorted_copy)


# Q64. Append 4 to list a = [4, 5, 8, 12, 4].
# a = [4, 5, 8, 12, 4]
# a.append(4)
# print(a)


# Q65. Remove first occurrence of 4 from a = [4, 5, 8, 12, 4].
# a = [4, 5, 8, 12, 4]
# a.remove(4)
# print(a)


# Q66. Get slice of a = [4, 5, 8, 12, 4] from index 1 to 3.
# a = [4, 5, 8, 12, 4]
# sliced = a[1:3]
# print(sliced)


# Q67. Compute sum of a = [4, 5, 8, 12, 4].
# a = [4, 5, 8, 12, 4]
# print(sum(a))


# Q68. Find unique elements of a = [4, 5, 8, 12, 4] preserving order.
# a = [4, 5, 8, 12, 4]
# unique = []
# for i in a:
#     if i not in unique:
#         unique.append(i)    
# print(unique)
# or
# unique = (list(dict.fromkeys(a)))
# print(unique)


# Q69. Merge two lists a=[4, 5, 8, 12, 4] and b=[5, 6, 10, 2, 0].
# a=[4, 5, 8, 12, 4]
# b=[5, 6, 10, 2, 0]
# merged = a + b
# print(merged)


#  Q70. Find intersection of lists a=[4, 5, 8, 12, 4] and b=[5, 6, 10, 2, 0].
# a=[4, 5, 8, 12, 4]
# b=[5, 6, 10, 2, 0]
# intersection = list(set(a) & set(b))
# print(intersection)


# Q71. Count occurrences of 4 in a = [4, 5, 8, 12, 4].
# a = [4, 5, 8, 12, 4]
# print(a.count(4))


# Q72. Replace index 2 in a=[4, 5, 8, 12, 4] with 99.
# a=[4, 5, 8, 12, 4]
# a[2] = 99
# print(a)


#  Q73. Get even numbers from nums = [1, 2, 3, 4, 5, 6, 7, 8, 9].
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# evens = []
# for i in nums:
#     if i % 2 == 0:
#         evens.append(i)
# print(evens)


#  Q74. Square each number in nums = [1, 2, 3, 4, 5, 6, 7, 8, 9].
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# squares = []
# for i in nums:
#     squares.append(i**2)
# print(squares)


#  Q75. Flatten nested list [[1,2],[3,4],[5]] in one line.
# nested = [[1,2], [3,4], [5]]
# lst = sum(nested, [])
# print(lst)


# Q76. Create list of pairs (x, x^2) for nums = [1, 2, 3, 4, 5, 6, 7, 8, 9].
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lst = []
# for i in nums:
#     lst.append((i, i**2))
# print(lst)   


# Q77. Rotate list a=[4, 5, 8, 12, 4] right by 2.
# a=[4, 5, 8, 12, 4]
# rotate_lst = a[-2:] + a[:-2]
# print(rotate_lst)


# Q78. Get second largest from nums = [1, 2, 3, 4, 5, 6, 7, 8, 9].
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# second_largest = nums[7:8]
# print(second_largest)


#  Q79. Remove None values from [1,None,2,None,3].
# values = [1, None, 2, None, 3]
# while None in values:
#     values.remove(None)
# print(values) 


#  Q80. Zip [1, 2, 3, 4, 5, 6, 7, 8, 9] and ['epsilon', 'zeta', 'eta', 'theta', 'alpha'] into list of tuples.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# word = ['epsilon', 'zeta', 'eta', 'theta', 'alpha']
# zipped_lst = zip(nums, word)
# print(list(zipped_lst))


#  Q81. Get the last element of list a = [5, 6, 10, 2, 0].
# a = [5, 6, 10, 2, 0]
# last_element = a.pop()
# print(last_element)


# Q82. Reverse list a = [5, 6, 10, 2, 0] in-place.
# a = [5, 6, 10, 2, 0]
# a.reverse()
# print(a)


#  Q83. Return a sorted copy of a = [5, 6, 10, 2, 0].
# a = [5, 6, 10, 2, 0]
# sorted_copy = sorted(a)
# print(sorted_copy)


#  Q84. Append 5 to list a = [5, 6, 10, 2, 0].
# a = [5, 6, 10, 2, 0]
# a.append(5)
# print(a)


# Q85. Remove first occurrence of 0 from a = [5, 6, 10, 2, 0].
# a = [5, 6, 10, 2, 0]
# a.remove(0)
# print(a)


# Q86. Get slice of a = [5, 6, 10, 2, 0] from index 1 to 3.
# a = [5, 6, 10, 2, 0]
# slice_a = a[1:4]
# print(slice_a)


# Q87. Compute sum of a = [5, 6, 10, 2, 0].
# a = [5, 6, 10, 2, 0]
# print(sum(a))


# Q88. Find unique elements of a = [5, 6, 10, 2, 0] preserving order.
# a = [5, 6, 10, 2, 0]
# unique = []
# for i in a:
#     if i is not unique:
#         unique.append(i)
# print(unique)


# Q89. Merge two lists a=[5, 6, 10, 2, 0] and b=[6, 7, 1, 5, 1].
# a=[5, 6, 10, 2, 0]
# b=[6, 7, 1, 5, 1]
# merged = a + b 
# print(merged)



#  Q90. Find intersection of lists a=[5, 6, 10, 2, 0] and b=[6, 7, 1, 5, 1].
# a=[5, 6, 10, 2, 0]
# b=[6, 7, 1, 5, 1]
# intersection = list(set(a)&set(b))
# print(intersection)


# Q91. Count occurrences of 5 in a = [5, 6, 10, 2, 0].
# a = [5, 6, 10, 2, 0]
# print(a.count(5))


# Q92. Replace index 2 in a=[5, 6, 10, 2, 0] with 99.
# a=[5, 6, 10, 2, 0]
# a[2] = 99
# print(a)


# Q93. Get even numbers from nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = []
# for i in nums:
#     if i %2 == 0:
#         evens.append(i)
# print(evens) 


#  Q94. Square each number in nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squares = []
# for i in nums:
#     squares.append(i**2)
# print(squares)


# Q95. Flatten nested list [[1,2],[3,4],[5]] in one line.
# lst = [[1,2],[3,4],[5]] 
# nested = sum(lst, [])
# print(nested)


# Q96. Create list of pairs (x, x^2) for nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pairs = []
# for i in nums:
#     pairs.append((i, i**2))
# print(pairs)


#  Q97. Rotate list a=[5, 6, 10, 2, 0] right by 2.
# a=[5, 6, 10, 2, 0]
# rotate = a[-2:] + a[:-2]
# print(rotate)


# Q98. Get second largest from nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# second_largest = nums[8:9]
# print(second_largest)


# Q99. Remove None values from [1,None,2,None,3].
# values = [1,None,2,None,3]
# while None in values:
#     values.remove(None)
# print(values)

# Q100. Zip [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and ['zeta', 'eta', 'theta', 'alpha', 'beta'] into list of tuples.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# words = ['zeta', 'eta', 'theta', 'alpha', 'beta']
# zipped_lst = zip(nums, words)
# print(list(zipped_lst))


# Q101. Get the last element of list a = [6, 7, 1, 5, 1].
# a = [6, 7, 1, 5, 1]
# print(a.pop())


# Q102. Reverse list a = [6, 7, 1, 5, 1] in-place.
# a = [6, 7, 1, 5, 1]
# a.reverse()
# print(a)


# Q103. Return a sorted copy of a = [6, 7, 1, 5, 1].
# a = [6, 7, 1, 5, 1]
# sort_copy = sorted(a)
# print(sort_copy)


# Q104. Append 6 to list a = [6, 7, 1, 5, 1].
# a = [6, 7, 1, 5, 1]
# a.append(6)
# print(a)


# Q105. Remove first occurrence of 1 from a = [6, 7, 1, 5, 1].
# a = [6, 7, 1, 5, 1]
# a.remove(1)
# print(a)


# Q106. Get slice of a = [6, 7, 1, 5, 1] from index 1 to 3.
# a = [6, 7, 1, 5, 1]
# print(a[1:3])


# Q107. Compute sum of a = [6, 7, 1, 5, 1].
# a = [6, 7, 1, 5, 1]
# total = 0
# for i in a:
#     total += i 
# print(total)


# Q108. Find unique elements of a = [6, 7, 1, 5, 1] preserving order.
# a = [6, 7, 1, 5, 1]
# unique = []
# for i in a:
#     if i is not unique:
#         unique.append(i)
# print(unique)


#  Q109. Merge two lists a=[6, 7, 1, 5, 1] and b=[0, 8, 3, 8, 2].
# a=[6, 7, 1, 5, 1]
# b=[0, 8, 3, 8, 2]
# merged = a + b
# print(merged)


# Q110. Find intersection of lists a=[6, 7, 1, 5, 1] and b=[0, 8, 3, 8, 2].
# a=[6, 7, 1, 5, 1]
# b=[0, 8, 3, 8, 2]
# intersection = list(set(a)&set(b))
# print(intersection)
# or 
# intersection = []
# for i in a:
#     if i in b and i is not intersection:
#         intersection.append(i)
# print(intersection)     


# Q111. Count occurrences of 6 in a = [6, 7, 1, 5, 1].
# a = [6, 7, 1, 5, 1]
# print(a.count(6))


# Q112. Replace index 2 in a=[6, 7, 1, 5, 1] with 99.
# a=[6, 7, 1, 5, 1]
# a[2] = 99
# print(a)


#  Q113. Get even numbers from nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# evens = []
# for i in nums:
#     if i % 2 == 0:
#         evens.append(i)
# print(i)


# Q114. Square each number in nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# squares = []
# for i in nums:
#     squares.append(i**2)
# print(squares)


# Q115. Flatten nested list [[1,2],[3,4],[5]] in one line.
# nested = [[1,2],[3,4],[5]]
# lst = []
# for sublist in nested:
#     for item in sublist:
#         lst.append(item)
# print(lst)    
# or 
# nested = [[1,2],[3,4],[5]]
# lst = sum(nested, [])
# print(lst)


# Q116. Create list of pairs (x, x^2) for nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# pairs = []
# for i in nums:
#     pairs.append((i, i**2))
# print(pairs)


#  Q117. Rotate list a=[6, 7, 1, 5, 1] right by 2.
# a=[6, 7, 1, 5, 1]
# rotate = a[-2:] + a[:-2]
# print(rotate)
# or
# rotate = 2
# for i in range (rotate):
#     last = a.pop()
#     a.insert(0, last)
# print(a)


# Q118. Get second largest from nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# second_largest = nums[9:10]
# print(second_largest)


#  Q119. Remove None values from [1,None,2,None,3].
# values = [1,None,2,None,3]
# while None in values:
#     values.remove(None)
# print(values)


#  Q120. Zip [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and ['eta', 'theta', 'alpha', 'beta', 'gamma'] into list of tuples.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# word = ['eta', 'theta', 'alpha', 'beta', 'gamma']
# zipped = zip(nums, word)
# print(list(zipped))


#  Q121. Get the last element of list a = [0, 8, 3, 8, 2].
# a = [0, 8, 3, 8, 2]
# print(a.pop())


#  Q122. Reverse list a = [0, 8, 3, 8, 2] in-place.
# a = [0, 8, 3, 8, 2]
# a.reverse()
# print(a)


# Q123. Return a sorted copy of a = [0, 8, 3, 8, 2].
# a = [0, 8, 3, 8, 2]
# sort_copy = sorted(a)
# print(sort_copy)


# Q124. Append 7 to list a = [0, 8, 3, 8, 2].
# a = [0, 8, 3, 8, 2]
# a.append(7)
# print(a)


# Q125. Remove first occurrence of 2 from a = [0, 8, 3, 8, 2].
# a = [0, 8, 3, 8, 2]
# a.remove(2)
# print(a)


# Q126. Get slice of a = [0, 8, 3, 8, 2] from index 1 to 3.
# a = [0, 8, 3, 8, 2]
# print(a[1:3])


# Q127. Compute sum of a = [0, 8, 3, 8, 2].
# a = [0, 8, 3, 8, 2]
# print(sum(a))
# total = 0
# for i in a:
#     total += i
# print(total)


# Q128. Find unique elements of a = [0, 8, 3, 8, 2] preserving order.
# a = [0, 8, 3, 8, 2]
# unique = []
# for i in a:
#     if i not in unique:
#         unique.append(i)
# print(unique)


#  Q129. Merge two lists a=[0, 8, 3, 8, 2] and b=[1, 0, 5, 11, 3].
# a=[0, 8, 3, 8, 2]
# b=[1, 0, 5, 11, 3]
# merged = a + b
# print(merged)



#  Q130. Find intersection of lists a=[0, 8, 3, 8, 2] and b=[1, 0, 5, 11, 3].
# a=[0, 8, 3, 8, 2]
# b=[1, 0, 5, 11, 3]
# intersection = list(set(a) & set(b))
# print(intersection)

# Q131. Count occurrences of 0 in a = [0, 8, 3, 8, 2].
# a = [0, 8, 3, 8, 2]
# print(a.count(0))


#  Q132. Replace index 2 in a=[0, 8, 3, 8, 2] with 99.
# a=[0, 8, 3, 8, 2]
# a[2] = 99
# print(a)


#  Q133. Get even numbers from nums = [1, 2, 3, 4, 5].
# nums = [1, 2, 3, 4, 5]
# evens = []
# for i in nums:
#     if i % 2 == 0:
#         evens.append(i)
# print(evens)


# Q134. Square each number in nums = [1, 2, 3, 4, 5].
# nums = [1, 2, 3, 4, 5]
# squares = []
# for i in nums:
#     squares.append(i**2)
# print(squares)


#  Q135. Flatten nested list [[1,2],[3,4],[5]] in one line.
# nested = [[1,2],[3,4],[5]]
# flat = []
# for sublist in nested:
#     for i in sublist:
#         flat.append(i)
# print(flat)   
# or
# flat = sum(nested, [])         
# print(flat)


# Q136. Create list of pairs (x, x^2) for nums = [1, 2, 3, 4, 5].
# nums = [1, 2, 3, 4, 5]
# pairs = []
# for i in nums:
#     pairs.append((i, i**2))
# print(pairs) 


#  Q137. Rotate list a=[0, 8, 3, 8, 2] right by 2.
# a=[0, 8, 3, 8, 2] 
# rotates = a[-2:] + a[:-2]
# print(rotates)


# Q138. Get second largest from nums = [1, 2, 3, 4, 5].
# nums = [1, 2, 3, 4, 5]
# second_largest = nums[3:4]
# print(second_largest)


#  Q139. Remove None values from [1,None,2,None,3].
# values = [1,None,2,None,3]
# while None in values:
#     values.remove(None)
# print(values) 


# Q140. Zip [1, 2, 3, 4, 5] and ['theta', 'alpha', 'beta', 'gamma', 'delta'] into list of tuples.
# a = [1, 2, 3, 4, 5]
# b = ['theta', 'alpha', 'beta', 'gamma', 'delta']
# zipped = list(zip(a, b))
# print(zipped)


# Q141. Get the last element of list a = [1, 0, 5, 11, 3].
# a = [1, 0, 5, 11, 3]
# print(a[-1]) 


# Q142. Reverse list a = [1, 0, 5, 11, 3] in-place.
# a = [1, 0, 5, 11, 3]
# a.reverse()
# print(a)


# Q143. Return a sorted copy of a = [1, 0, 5, 11, 3].
# a = [1, 0, 5, 11, 3]
# sorted_list = sorted(a)
# print(sorted_list)


# Q144. Append 8 to list a = [1, 0, 5, 11, 3].
# a = [1, 0, 5, 11, 3]
# a.append(8)
# print(a)  


# Q145. Remove first occurrence of 3 from a = [1, 0, 5, 11, 3].
# a = [1, 0, 5, 11, 3]
# a.remove(3)
# print(a)


# Q146. Get slice of a = [1, 0, 5, 11, 3] from index 1 to 3.
# a = [1, 0, 5, 11, 3]
# slice_a = a[1:3]
# print(slice_a) 


# Q147. Compute sum of a = [1, 0, 5, 11, 3].
# a = [1, 0, 5, 11, 3]
# print(sum(a))


# Q148. Find unique elements of a = [1, 0, 5, 11, 3] preserving order.
# a = [1, 0, 5, 11, 3]
# unique = []
# for x in a:
#     if x not in unique:
#         unique.append(x)
# print(unique) 


# Q149. Merge two lists a=[1, 0, 5, 11, 3] and b=[2, 1, 7, 1, 4].
# a = [1, 0, 5, 11, 3]
# b = [2, 1, 7, 1, 4]
# c = a + b
# print(c)


# Q150. Find intersection of lists a=[1, 0, 5, 11, 3] and b=[2, 1, 7, 1, 4].
# a = [1, 0, 5, 11, 3]
# b = [2, 1, 7, 1, 4]
# intersection = list(set(a) & set(b))
# print(intersection)


# Q151. Count occurrences of 1 in a = [1, 0, 5, 11, 3].
# a = [1, 0, 5, 11, 3]
# print(a.count(1)) 


# Q152. Replace index 2 in a=[1, 0, 5, 11, 3] with 99.
# a = [1, 0, 5, 11, 3]
# a[2] = 99
# print(a)


# Q153. Get even numbers from nums = [1, 2, 3, 4, 5, 6].
# nums = [1, 2, 3, 4, 5, 6]
# evens = []
# for i in nums:
#     if i % 2 == 0:
#         evens.append(i)
# print(evens)


# Q154. Square each number in nums = [1, 2, 3, 4, 5, 6].
# nums = [1, 2, 3, 4, 5, 6]
# squares = []
# for i in nums:
#     squares.append(i ** 2)
# print(squares) 


# Q155. Flatten nested list [[1,2],[3,4],[5]] in one line.
# nested = [[1, 2], [3, 4], [5]]
# flat = [i for sub in nested for i in sub]
# print(flat)


# Q156. Create list of pairs (x, x^2) for nums = [1, 2, 3, 4, 5, 6].
# nums = [1, 2, 3, 4, 5, 6]
# pairs = []
# for i in nums:
#     pairs.append((i, i ** 2))
# print(pairs)


# Q157. Rotate list a=[1, 0, 5, 11, 3] right by 2.
# a = [1, 0, 5, 11, 3]
# rotated = a[-2:] + a[:-2]
# print(rotated) 


# Q158. Get second largest from nums = [1, 2, 3, 4, 5, 6].
# nums = [1, 2, 3, 4, 5, 6]
# second_largest = sorted(set(nums))[-2]
# print(second_largest)


# Q159. Remove None values from [1,None,2,None,3].
# values = [1, None, 2, None, 3]
# while None in values:
#     values.remove(None)
# print(values) 


# Q160. Zip [1, 2, 3, 4, 5, 6] and ['alpha', 'beta', 'gamma', 'delta', 'epsilon'] into list of tuples.
# nums = [1, 2, 3, 4, 5, 6]
# words = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
# zipped = list(zip(nums, words))
# print(zipped) 


# Q161. Get the last element of list a = [2, 1, 7, 1, 4].
# a = [2, 1, 7, 1, 4]
# print(a[-1])  


# Q162. Reverse list a = [2, 1, 7, 1, 4] in-place.
# a = [2, 1, 7, 1, 4]
# a.reverse()
# print(a) 


# Q163. Return a sorted copy of a = [2, 1, 7, 1, 4].
# a = [2, 1, 7, 1, 4]
# sorted_list = sorted(a)
# print(sorted_list)  


# Q164. Append 9 to list a = [2, 1, 7, 1, 4].
# a = [2, 1, 7, 1, 4]
# a.append(9)
# print(a) 


# Q165. Remove first occurrence of 4 from a = [2, 1, 7, 1, 4].
# a = [2, 1, 7, 1, 4]
# a.remove(4)
# print(a) 


# Q166. Get slice of a = [2, 1, 7, 1, 4] from index 1 to 3.
# a = [2, 1, 7, 1, 4]
# slice_a = a[1:4]
# print(slice_a)  


# Q167. Compute sum of a = [2, 1, 7, 1, 4].
# a = [2, 1, 7, 1, 4]
# print(sum(a)) 


# Q168. Find unique elements of a = [2, 1, 7, 1, 4] preserving order.
# a = [2, 1, 7, 1, 4]
# unique = []
# for i in a:
#     if i not in unique:
#         unique.append(i)
# print(unique)


# Q169. Merge two lists a=[2, 1, 7, 1, 4] and b=[3, 2, 9, 4, 0].
# a = [2, 1, 7, 1, 4]
# b = [3, 2, 9, 4, 0]
# c = a + b
# print(c)


# Q170. Find intersection of lists a=[2, 1, 7, 1, 4] and b=[3, 2, 9, 4, 0].
# a = [2, 1, 7, 1, 4]
# b = [3, 2, 9, 4, 0]
# intersection_set = list(set(a) & set(b))
# print(intersection_set)


# Q171. Count occurrences of 2 in a = [2, 1, 7, 1, 4].
# a = [2, 1, 7, 1, 4]
# print(a.count(2))


# Q172. Replace index 2 in a=[2, 1, 7, 1, 4] with 99.
# a = [2, 1, 7, 1, 4]
# a[2] = 99
# print(a)


# Q173. Get even numbers from nums = [1, 2, 3, 4, 5, 6, 7].
# nums = [1, 2, 3, 4, 5, 6, 7]
# evens = []
# for i in nums:
#     if i % 2 == 0:
#         evens.append(i)
# print(evens) 


# Q174. Square each number in nums = [1, 2, 3, 4, 5, 6, 7].
# nums = [1, 2, 3, 4, 5, 6, 7]
# squares = []
# for i in nums:
#     squares.append(i ** 2)
# print(squares)


# Q175. Flatten nested list [[1,2],[3,4],[5]] in one line.
# nested = [[1, 2], [3, 4], [5]]
# flat = [i for sub in nested for i in sub]
# print(flat) 


# Q176. Create list of pairs (x, x^2) for nums = [1, 2, 3, 4, 5, 6, 7].
# nums = [1, 2, 3, 4, 5, 6, 7]
# pairs = []
# for i in nums:
#     pairs.append((i, i**2))
# print(pairs)


# Q177. Rotate list a=[2, 1, 7, 1, 4] right by 2.
# a = [2, 1, 7, 1, 4]
# rotated = a[-2:] + a[:-2]
# print(rotated) 


# Q178. Get second largest from nums = [1, 2, 3, 4, 5, 6, 7].
# nums = [1, 2, 3, 4, 5, 6, 7]
# second_largest = sorted(nums)[-2]
# print(second_largest)


# Q179. Remove None values from [1, None, 2, None, 3, None].
# values = [1, None, 2, None, 3, None]
# while None in values:
#     values.remove(None)
# print(values) 


# Q180. Zip [1, 2, 3, 4, 5, 6, 7] and ['phi', 'chi', 'psi', 'omega'] into list of tuples.
# nums = [1, 2, 3, 4, 5, 6, 7]
# words = ['phi', 'chi', 'psi', 'omega']
# zipped = list(zip(nums, words))
# print(zipped)


# Q181. Get the last element of list a = [3, 2, 9, 4, 0].
# a = [3, 2, 9, 4, 0]
# print(a.pop())


#  Q182. Reverse list a = [3, 2, 9, 4, 0] in-place.
# a = [3, 2, 9, 4, 0]
# a.reverse()
# print(a)


# Q183. Return a sorted copy of a = [3, 2, 9, 4, 0].
# a = [3, 2, 9, 4, 0]
# print(sorted(a))


# Q184. Append 0 to list a = [3, 2, 9, 4, 0].
# a = [3, 2, 9, 4, 0]
# a.append(0)
# print(a)


#  Q185. Remove first occurrence of 0 from a = [3, 2, 9, 4, 0].
# a = [3, 2, 9, 4, 0]
# a.remove(0)
# print(a)


#  Q186. Get slice of a = [3, 2, 9, 4, 0] from index 1 to 3.
# a = [3, 2, 9, 4, 0]
# print(a[1:4])


#  Q187. Compute sum of a = [3, 2, 9, 4, 0].
# a = [3, 2, 9, 4, 0]
# print(sum(a))
# or
# total = 0
# for i in a:
#     total += i
# print(total) 


# Q188. Find unique elements of a = [3, 2, 9, 4, 0] preserving order.
# a = [3, 2, 9, 4, 0]
# unique = []
# for i in a:
#     if i not in unique:
#         unique.append(i)
# print(unique)   


# Q189. Merge two lists a=[3, 2, 9, 4, 0] and b=[4, 3, 0, 7, 1].
# a=[3, 2, 9, 4, 0]
# b=[4, 3, 0, 7, 1]
# merged = a + b
# print(merged)


#  Q190. Find intersection of lists a=[3, 2, 9, 4, 0] and b=[4, 3, 0, 7, 1].
# a=[3, 2, 9, 4, 0]
# b=[4, 3, 0, 7, 1]
# intersection = list(set(a)&set(b))
# print(intersection)



# Q191. Count occurrences of 3 in a = [3, 2, 9, 4, 0].
# a = [3, 2, 9, 4, 0]
# print(a.count(3))


# Q192. Replace index 2 in a=[3, 2, 9, 4, 0] with 99.
# a=[3, 2, 9, 4, 0]
# a[2] = 99
# print(a)


# Q193. Get even numbers from nums = [1, 2, 3, 4, 5, 6, 7, 8].
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# evens = []
# for i in nums:
#     if i % 2 == 0:
#         evens.append(i)
# print(evens)


# Q194. Square each number in nums = [1, 2, 3, 4, 5, 6, 7, 8].
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# squares = []
# for i in nums:
#     squares.append(i**2)
# print(squares)


#  Q195. Flatten nested list [[1,2],[3,4],[5]] in one line.
# nested = [[1,2],[3,4],[5]]
# flat = []
# for sublist in nested:
#     for i in sublist:
#         flat.append(i)
# print(flat)  


# Q196. Create list of pairs (x, x^2) for nums = [1, 2, 3, 4, 5, 6, 7, 8].      
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# pairs = []
# for i in nums:
#     pairs.append((i,i**2))
# print(pairs)

# Q197. Rotate list a=[3, 2, 9, 4, 0] right by 2.
# a=[3, 2, 9, 4, 0]
# rotate = a[-2:] + a[:-2]
# print(rotate)


# Q198. Get second largest from nums = [1, 2, 3, 4, 5, 6, 7, 8].
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# print(nums[6:7])


#  Q199. Remove None values from [1,None,2,None,3].
# values = [1,None,2,None,3]
# while None in values:
#     values.remove(None)
# print(values)    


# Q200. Zip [1, 2, 3, 4, 5, 6, 7, 8] and ['gamma', 'delta', 'epsilon', 'zeta', 'eta'] into list of tuples.
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# word = ['gamma', 'delta', 'epsilon', 'zeta', 'eta'] 
# zip_lst = list(zip(nums, word))
# print(zip_lst)

# Q201. Get the last element of list a = [4, 3, 0, 7, 1].
# a = [4, 3, 0, 7, 1]
# a.pop()
# print(a)


#  Q202. Reverse list a = [4, 3, 0, 7, 1] in-place.
# a = [4, 3, 0, 7, 1]
# a.reverse()
# print(a)


#  Q203. Return a sorted copy of a = [4, 3, 0, 7, 1].
# a = [4, 3, 0, 7, 1]
# print(sorted(a))


# Q204. Append 1 to list a = [4, 3, 0, 7, 1].
# a = [4, 3, 0, 7, 1]
# a.append(1)
# print(a)


# Q205. Remove first occurrence of 1 from a = [4, 3, 0, 7, 1].
# a = [4, 3, 0, 7, 1]
# a.remove(1)
# print(a)

#  Q206. Get slice of a = [4, 3, 0, 7, 1] from index 1 to 3.
# a = [4, 3, 0, 7, 1]
# print(a[1:3])


#  Q207. Compute sum of a = [4, 3, 0, 7, 1].
# a = [4, 3, 0, 7, 1]
# print(sum(a))
# total = 0
# for i in a:
#     total += i
# print(total)    


#  Q208. Find unique elements of a = [4, 3, 0, 7, 1] preserving order.
# a = [4, 3, 0, 7, 1]
# unique = []
# for i in a:
#     if i not in unique:
#         unique.append(i)
# print(unique)


#  Q209. Merge two lists a=[4, 3, 0, 7, 1] and b=[5, 4, 2, 10, 2].
# a=[4, 3, 0, 7, 1]
# b=[5, 4, 2, 10, 2]
# merged = a + b
# print(merged)


# Q210. Find intersection of lists a=[4, 3, 0, 7, 1] and b=[5, 4, 2, 10, 2].
# a=[4, 3, 0, 7, 1]
# b=[5, 4, 2, 10, 2]
# intersection = list(set(a)&set(b))
# print(intersection)


#  Q211. Count occurrences of 4 in a = [4, 3, 0, 7, 1].
# a = [4, 3, 0, 7, 1]
# print(a.count(4))


# Q212. Replace index 2 in a=[4, 3, 0, 7, 1] with 99.
# a=[4, 3, 0, 7, 1]
# a[2] = 99
# print(a)


# Q213. Get even numbers from nums = [1, 2, 3, 4, 5, 6, 7, 8, 9].
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# evens = []
# for i in nums:
#     if i % 2 == 0:
#         evens.append(i)
# print(evens)


# Q214. Square each number in nums = [1, 2, 3, 4, 5, 6, 7, 8, 9].
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# squares = []
# for i in nums:
#     squares.append(i**2)
# print(squares)


# Q215. Flatten nested list [[1,2],[3,4],[5]] in one line.
# nested = [[1,2],[3,4],[5]]
# flat = []
# for sublist in nested:
#     for i in sublist:
#         flat.append(i)
# print(flat)
# or
# flat = sum(nested, [])
# print(flat)


#  Q216. Create list of pairs (x, x^2) for nums = [1, 2, 3, 4, 5, 6, 7, 8, 9].
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# squares = []
# for i in nums:
#     squares.append((i, i**2))
# print(squares) 


#  Q217. Rotate list a=[4, 3, 0, 7, 1] right by 2.
# a=[4, 3, 0, 7, 1]
# rotate = a[-2:] + a[:-2]
# print(rotate)


# Q218. Get second largest from nums = [1, 2, 3, 4, 5, 6, 7, 8, 9].
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# second_largest = sorted(nums)[-2]
# print(second_largest)


# Q219. Remove None values from [1,None,2,None,3].
# lst = [1,None,2,None,3]
# while None in lst:
#     lst.remove(None)
# print(lst)    


# Q220. Zip [1, 2, 3, 4, 5, 6, 7, 8, 9] and ['delta', 'epsilon', 'zeta', 'eta', 'theta'] into list of tuples.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# word = ['delta', 'epsilon', 'zeta', 'eta', 'theta']
# zip_lst = list(zip(nums, word))
# print(zip_lst)


# Q221. Get the last element of list a = [5, 4, 2, 10, 2].
# a = [5, 4, 2, 10, 2]
# print(a[-1])


# Q222. Reverse list a = [5, 4, 2, 10, 2] in-place.
# a = [5, 4, 2, 10, 2]
# a.reverse()
# print(a)


# Q223. Return a sorted copy of a = [5, 4, 2, 10, 2].
# a = [5, 4, 2, 10, 2]
# print(sorted(a))


# Q224. Append 2 to list a = [5, 4, 2, 10, 2].
# a = [5, 4, 2, 10, 2]
# a.append(2)
# print(a)


# Q225. Remove first occurrence of 2 from a = [5, 4, 2, 10, 2].
# a = [5, 4, 2, 10, 2]
# a.remove(2)
# print(a)


# Q226. Get slice of a = [5, 4, 2, 10, 2] from index 1 to 3.
# a = [5, 4, 2, 10, 2]
# print(a[1:3])


# Q227. Compute sum of a = [5, 4, 2, 10, 2].
# a = [5, 4, 2, 10, 2]
# print(sum(a))


# Q228. Find unique elements of a = [5, 4, 2, 10, 2] preserving order.
# a = [5, 4, 2, 10, 2]
# unique = []
# for i in a:
#     if i not in unique:
#         unique.append(i)
# print(unique)


# Q229. Merge two lists a=[5, 4, 2, 10, 2] and b=[6, 5, 4, 0, 3].
# a = [5, 4, 2, 10, 2]
# b = [6, 5, 4, 0, 3]
# merged = a + b
# print(merged)


# Q230. Find intersection of lists a=[5, 4, 2, 10, 2] and b=[6, 5, 4, 0, 3].
# a = [5, 4, 2, 10, 2]
# b = [6, 5, 4, 0, 3]
# intersection = list(set(a) & set(b))
# print(intersection)


# Q231. Count occurrences of 5 in a = [5, 4, 2, 10, 2].
# a = [5, 4, 2, 10, 2]
# print(a.count(5))


# Q232. Replace index 2 in a=[5, 4, 2, 10, 2] with 99.
# a = [5, 4, 2, 10, 2]
# a[2] = 99
# print(a)


# Q233. Get even numbers from nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = []
# for i in nums:
#     if i % 2 == 0:
#         evens.append(i)
# print(evens)


# Q234. Square each number in nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squares = []
# for i in nums:
#     squares.append(i**2)
# print(squares)


# Q235. Flatten nested list [[1,2],[3,4],[5]] in one line.
# nested = [[1,2],[3,4],[5]]
# flat = []
# for sublist in nested:
#     for i in sublist:
#         flat.append(i)
# print(flat)
# # or
# flat = sum(nested, [])
# print(flat)


# Q236. Create list of pairs (x, x^2) for nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pairs = []
# for i in nums:
#     pairs.append((i, i**2))
# print(pairs)


# Q237. Rotate list a=[5, 4, 2, 10, 2] right by 2.
# a = [5, 4, 2, 10, 2]
# rotate = a[-2:] + a[:-2]
# print(rotate)


# Q238. Get second largest from nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# second_largest = sorted(nums)[-2]
# print(second_largest)


# Q239. Remove None values from [1,None,2,None,3].
# lst = [1,None,2,None,3]
# while None in lst:
#     lst.remove(None)
# print(lst)


# Q240. Zip [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and ['epsilon', 'zeta', 'eta', 'theta', 'alpha'] into list of tuples.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# words = ['epsilon', 'zeta', 'eta', 'theta', 'alpha']
# zip_lst = list(zip(nums, words))
# print(zip_lst)


# Q241. Get the last element of list a = [6, 5, 4, 0, 3].
# a = [6, 5, 4, 0, 3]
# print(a[-1])


# Q242. Reverse list a = [6, 5, 4, 0, 3] in-place.
# a = [6, 5, 4, 0, 3]
# a.reverse()
# print(a)


# Q243. Return a sorted copy of a = [6, 5, 4, 0, 3].
# a = [6, 5, 4, 0, 3]
# print(sorted(a))


# Q244. Append 3 to list a = [6, 5, 4, 0, 3].
# a = [6, 5, 4, 0, 3]
# a.append(3)
# print(a)


# Q245. Remove first occurrence of 3 from a = [6, 5, 4, 0, 3].
# a = [6, 5, 4, 0, 3]
# a.remove(3)
# print(a)


# Q246. Get slice of a = [6, 5, 4, 0, 3] from index 1 to 3.
# a = [6, 5, 4, 0, 3]
# print(a[1:3])


# Q247. Compute sum of a = [6, 5, 4, 0, 3].
# a = [6, 5, 4, 0, 3]
# print(sum(a))


# Q248. Find unique elements of a = [6, 5, 4, 0, 3] preserving order.
# a = [6, 5, 4, 0, 3]
# unique = []
# for i in a:
#     if i not in unique:
#         unique.append(i)
# print(unique)


# Q249. Merge two lists a=[6, 5, 4, 0, 3] and b=[0, 6, 6, 3, 4].
# a = [6, 5, 4, 0, 3]
# b = [0, 6, 6, 3, 4]
# merged = a + b
# print(merged)


# Q250. Find intersection of lists a=[6, 5, 4, 0, 3] and b=[0, 6, 6, 3, 4].
# a = [6, 5, 4, 0, 3]
# b = [0, 6, 6, 3, 4]
# intersection = list(set(a) & set(b))
# print(intersection)
# ---------------------------------------------------------------------------------------
# tuple:-

#  Q251. Access third element of t = (1, 4, 2, 3).
# t = (1, 4, 2, 3)
# print(t[3])


# Q252. Slice t = (1, 4, 2, 3) from 1 to 3.
# t = (1, 4, 2, 3)
# slice_t = t[1:3]
# print(slice_t)


#  Q253. Concatenate tuples t=(1, 4, 2, 3) and u=(2, 5, 4, 6).
# t=(1, 4, 2, 3)
# u=(2, 5, 4, 6)
# print(t + u)


# Q254. Unpack t = (1, 4, 2, 3) into a,b,c,d.
# t = (1, 4, 2, 3)
# k = ('a', 'b', 'c', 'd')
# t = k
# print(t)


# Q255. Count 1 in t = (1, 4, 2, 3).
# t = (1, 4, 2, 3)
# print(t.count(1))


#  Q256. Find index of first 1 in t = (1, 4, 2, 3).
# t = (1, 4, 2, 3)
# print(t.index(1))


# Q257. Convert list [1,2,3] to tuple.
# lst = [1,2,3]
# print(tuple(lst))


# Q258. Check if 3 is in (1,2,3).
# tupln = (1, 2, 3)
# if 3  in tupln:
#     print("3 is in list")


#  Q259. Swap values of x=5 and y=7 using tuple unpacking.
# x=5
# y=7
# x, y = 7, 5
# print(x)
# print(y)


# Q260. Nested access: get 3 from t=(1,(2,3),(4,5)).
# t=(1,(2,3),(4,5))
# nested = t[1] [1]
# print(nested)


# Q261. Access third element of t = (2, 5, 4, 6).
# t = (2, 5, 4, 6)
# print(t[2])


# Q262. Slice t = (2, 5, 4, 6) from 1 to 3.
# t = (2, 5, 4, 6)
# print(t[1:3])


# Q263. Concatenate tuples t=(2, 5, 4, 6) and u=(3, 6, 6, 9).
# t = (2, 5, 4, 6)
# u = (3, 6, 6, 9)
# print(t + u)


# Q264. Unpack t = (2, 5, 4, 6) into a,b,c,d.
# t = (2, 5, 4, 6)
# a, b, c, d = t
# print(a, b, c, d)


# Q265. Count 2 in t = (2, 5, 4, 6).
# t = (2, 5, 4, 6)
# print(t.count(2))


# Q266. Find index of first 2 in t = (2, 5, 4, 6).
# t = (2, 5, 4, 6)
# print(t.index(2))


# Q267. Convert list [1,2,3] to tuple.
# lst = [1, 2, 3]
# print(tuple(lst))


# Q268. Check if 3 is in (1,2,3).
# t = (1, 2, 3)
# print(3 in t)


# Q269. Swap values of x=5 and y=7 using tuple unpacking.
# x = 5
# y = 7
# x, y = 7, 5
# print(x, y)


# Q270. Nested access: get 3 from t=(1,(2,3),(4,5)).
# t = (1, (2, 3), (4, 5))
# print(t[1][1])


# Q271. Access third element of t = (3, 6, 6, 9).
# t = (3, 6, 6, 9)
# print(t[2])


# Q272. Slice t = (3, 6, 6, 9) from 1 to 3.
# t = (3, 6, 6, 9)
# print(t[1:3])


# Q273. Concatenate tuples t=(3, 6, 6, 9) and u=(4, 0, 8, 1).
# t = (3, 6, 6, 9)
# u = (4, 0, 8, 1)
# print(t + u)


# Q274. Unpack t = (3, 6, 6, 9) into a,b,c,d.
# t = (3, 6, 6, 9)
# a, b, c, d = t
# print(a, b, c, d)


# Q275. Count 0 in t = (3, 6, 6, 9).
# t = (3, 6, 6, 9)
# print(t.count(0))


# Q276. Find index of first 3 in t = (3, 6, 6, 9).
# t = (3, 6, 6, 9)
# print(t.index(3))


# Q277. Convert list [1,2,3] to tuple.
# lst = [1, 2, 3]
# print(tuple(lst))


# Q278. Check if 3 is in (1,2,3).
# t = (1, 2, 3)
# print(3 in t)


# Q279. Swap values of x=5 and y=7 using tuple unpacking.
# x, y = 5, 7
# x, y = y, x
# print(x, y)


# Q280. Nested access: get 3 from t=(1,(2,3),(4,5)).
# t = (1, (2, 3), (4, 5))
# print(t[1][1])


# Q281. Access third element of t = (4, 0, 8, 1).
# t = (4, 0, 8, 1)
# print(t[2])


# Q282. Slice t = (4, 0, 8, 1) from 1 to 3.
# t = (4, 0, 8, 1)
# print(t[1:3])


# Q283. Concatenate tuples t=(4, 0, 8, 1) and u=(0, 1, 1, 4).
# t = (4, 0, 8, 1)
# u = (0, 1, 1, 4)
# print(t + u)


# Q284. Unpack t = (4, 0, 8, 1) into a,b,c,d.
# t = (4, 0, 8, 1)
# a, b, c, d = t
# print(a, b, c, d)


# Q285. Count 1 in t = (4, 0, 8, 1).
# t = (4, 0, 8, 1)
# print(t.count(1))


# Q286. Find index of first 4 in t = (4, 0, 8, 1).
# t = (4, 0, 8, 1)
# print(t.index(4))


# Q287. Convert list [1,2,3] to tuple.
# lst = [1, 2, 3]
# print(tuple(lst))


# Q288. Check if 3 is in (1,2,3).
# t = (1, 2, 3)
# print(3 in t)


# Q289. Swap values of x=5 and y=7 using tuple unpacking.
# x, y = 5, 7
# x, y = y, x
# print(x, y)


# Q290. Nested access: get 3 from t=(1,(2,3),(4,5)).
# t = (1, (2, 3), (4, 5))
# print(t[1][1])


# Q291. Access third element of t = (0, 1, 1, 4).
# t = (0, 1, 1, 4)
# print(t[2])


# Q292. Slice t = (0, 1, 1, 4) from 1 to 3.
# t = (0, 1, 1, 4)
# print(t[1:3])


# Q293. Concatenate tuples t=(0, 1, 1, 4) and u=(1, 2, 3, 7).
# t = (0, 1, 1, 4)
# u = (1, 2, 3, 7)
# print(t + u)


# Q294. Unpack t = (0, 1, 1, 4) into a,b,c,d.
# t = (0, 1, 1, 4)
# a, b, c, d = t
# print(a, b, c, d)


# Q295. Count 2 in t = (0, 1, 1, 4).
# t = (0, 1, 1, 4)
# print(t.count(2))


# Q296. Find index of first 0 in t = (0, 1, 1, 4).
# t = (0, 1, 1, 4)
# print(t.index(0))


# Q297. Convert list [1,2,3] to tuple.
# lst = [1, 2, 3]
# print(tuple(lst))


# Q298. Check if 3 is in (1,2,3).
# t = (1, 2, 3)
# print(3 in t)


# Q299. Swap values of x=5 and y=7 using tuple unpacking.
# x, y = 5, 7
# x, y = y, x
# print(x, y)


# Q300. Nested access: get 3 from t=(1,(2,3),(4,5)).
# t = (1, (2, 3), (4, 5))
# print(t[1][1])


#  Q301. Access third element of t = (1, 2, 3, 7).
# t = (1, 2, 3, 7)
# print(t[3])


#  Q302. Slice t = (1, 2, 3, 7) from 1 to 3.
# t = (1, 2, 3, 7)
# slice_t = t[1:3]
# print(slice_t)


#  Q303. Concatenate tuples t=(1, 2, 3, 7) and u=(2, 3, 5, 10).
# t=(1, 2, 3, 7)
# u=(2, 3, 5, 10)
# print(t + u)


#  Q304. Unpack t = (1, 2, 3, 7) into a,b,c,d.
# t = (1, 2, 3, 7)
# t = 'a', 'b', 'c', 'd'
# print(t)


#  Q305. Count 0 in t = (1, 2, 3, 7).
# t = (1, 2, 3, 7)
# print(t.count(0))


#  Q306. Find index of first 1 in t = (1, 2, 3, 7).
# t = (1, 2, 3, 7)
# print(t.index(1))


#  Q307. Convert list [1,2,3] to tuple.
# lst = [1,2,3]
# print(tuple(lst))


# Q308. Check if 3 is in (1,2,3).
# t = (1,2,3)
# if 3 in t:
#     print("3 is in list")


# Q309. Swap values of x=5 and y=7 using tuple unpacking.
# x = 5
# y = 7
# x, y = 7, 5
# print(x, y)


#  Q310. Nested access: get 3 from t=(1,(2,3),(4,5)).
# t = (1,(2,3),(4,5))
# nested = t[1][1] 
# print(nested)


# Q311. Access third element of t = (2, 3, 5, 10).
# t = (2, 3, 5, 10)
# print(t[2])


# Q312. Slice t = (2, 3, 5, 10) from 1 to 3.
# t = (2, 3, 5, 10)
# print(t[1:3])


# Q313. Concatenate tuples t=(2, 3, 5, 10) and u=(3, 4, 7, 2).
# t = (2, 3, 5, 10)
# u = (3, 4, 7, 2)
# print(t + u) 


# Q314. Unpack t = (2, 3, 5, 10) into a,b,c,d.
# t = (2, 3, 5, 10)
# a, b, c, d = t
# print(a, b, c, d)


# Q315. Count 1 in t = (2, 3, 5, 10).
# t = (2, 3, 5, 10)
# print(t.count(1))


# Q316. Find index of first 2 in t = (2, 3, 5, 10).
# t = (2, 3, 5, 10)
# print(t.index(2))   


# Q317. Convert list [1,2,3] to tuple.
# lst = [1, 2, 3]
# print(tuple(lst))


# Q318. Check if 3 is in (1,2,3).
# t = (1, 2, 3)
# print(3 in t)


# Q319. Swap values of x=5 and y=7 using tuple unpacking.
# x, y = 5, 7
# x, y = y, x
# print(x, y)


# Q320. Nested access: get 3 from t=(1,(2,3),(4,5)).
# t = (1, (2, 3), (4, 5))
# print(t[1][1])


# Q321. Access third element of t = (3, 4, 7, 2).
# t = (3, 4, 7, 2)
# print(t[2]) 


# Q322. Slice t = (3, 4, 7, 2) from 1 to 3.
# t = (3, 4, 7, 2)
# print(t[1:3])


# Q323. Concatenate tuples t=(3, 4, 7, 2) and u=(4, 5, 0, 5).
# t = (3, 4, 7, 2)
# u = (4, 5, 0, 5)
# print(t + u) 


# Q324. Unpack t = (3, 4, 7, 2) into a,b,c,d.
# t = (3, 4, 7, 2)
# a, b, c, d = t
# print(a, b, c, d)


# Q325. Count 2 in t = (3, 4, 7, 2).
# t = (3, 4, 7, 2)
# print(t.count(2))


# Q326. Find index of first 3 in t = (3, 4, 7, 2).
# t = (3, 4, 7, 2)
# print(t.index(3))


# Q327. Convert list [1,2,3] to tuple.
# lst = [1, 2, 3]
# print(tuple(lst))


# Q328. Check if 3 is in (1,2,3).
# t = (1, 2, 3)
# if 3 in t:
#     print("3 is in list")


# Q329. Swap values of x=5 and y=7 using tuple unpacking.
# x, y = 5, 7
# x, y = y, x
# print(x, y) 


# Q330. Nested access: get 3 from t=(1,(2,3),(4,5)).
# t = (1, (2, 3), (4, 5))
# print(t[1][1])


# Q331. Access third element of t = (4, 5, 0, 5).
# t = (4, 5, 0, 5)
# print(t[2])


# Q332. Slice t = (4, 5, 0, 5) from 1 to 3.
# t = (4, 5, 0, 5)
# print(t[1:3])


# Q333. Concatenate tuples t=(4, 5, 0, 5) and u=(0, 6, 2, 8).
# t = (4, 5, 0, 5)
# u = (0, 6, 2, 8)
# print(t + u)   


# Q334. Unpack t = (4, 5, 0, 5) into a,b,c,d.
# t = (4, 5, 0, 5)
# a, b, c, d = t
# print(t)


# Q335. Count 0 in t = (4, 5, 0, 5).
# t = (4, 5, 0, 5)
# print(t.count(0))


# Q336. Find index of first 4 in t = (4, 5, 0, 5).
# t = (4, 5, 0, 5)
# print(t.index(4)) 


# Q337. Convert list [1,2,3] to tuple.
# lst = [1, 2, 3]
# print(tuple(lst)) 


# Q338. Check if 3 is in (1,2,3).
# t = (1, 2, 3)
# print(3 in t)


# Q339. Swap values of x=5 and y=7 using tuple unpacking.
# x, y = 5, 7
# x, y = y, x
# print(x, y)


# Q340. Nested access: get 3 from t=(1,(2,3),(4,5)).
# t = (1, (2, 3), (4, 5))
# print(t[1][1])


# Q341. Access third element of t = (0, 6, 2, 8).
# t = (0, 6, 2, 8)
# print(t[2])


# Q342. Slice t = (0, 6, 2, 8) from 1 to 3.
# t = (0, 6, 2, 8)
# print(t[1:3]) 


# Q343. Concatenate tuples t=(0, 6, 2, 8) and u=(1, 0, 4, 0).
# t = (0, 6, 2, 8)
# u = (1, 0, 4, 0)
# print(t + u)


# Q344. Unpack t = (0, 6, 2, 8) into a,b,c,d.
# t = (0, 6, 2, 8)
# a, b, c, d = t
# print(a, b, c, d)


# Q345. Count 1 in t = (0, 6, 2, 8).
# t = (0, 6, 2, 8)
# print(t.count(1)) 


# Q346. Find index of first 0 in t = (0, 6, 2, 8).
# t = (0, 6, 2, 8)
# print(t.index(0))


# Q347. Convert list [1,2,3] to tuple.
# lst = [1, 2, 3]
# print(tuple(lst))


# Q348. Check if 3 is in (1,2,3).
# t = (1, 2, 3)
# print(3 in t)


# Q349. Swap values of x=5 and y=7 using tuple unpacking.
# x, y = 5, 7
# x, y = y, x
# print(x, y)


# Q350. Nested access: get 3 from t=(1,(2,3),(4,5)).
# t = (1, (2, 3), (4, 5))
# print(t[1][1])


# Q351. Access third element of t = (1, 0, 4, 0).
# t = (1, 0, 4, 0)
# print(t[3])


#  Q352. Slice t = (1, 0, 4, 0) from 1 to 3.
# t = (1, 0, 4, 0)
# print(t[1:3])


#  Q353. Concatenate tuples t=(1, 0, 4, 0) and u=(2, 1, 6, 3).
# t=(1, 0, 4, 0)
# u=(2, 1, 6, 3)
# print(t + u)


# Q354. Unpack t = (1, 0, 4, 0) into a,b,c,d.
# t = (1, 0, 4, 0)
# a,b,c,d = 1, 0, 4, 0
# print(a, b, c, d)


# # Q355. Count 2 in t = (1, 0, 4, 0).
# t = (1, 0, 4, 0)
# print(t.count(2))


# Q356. Find index of first 1 in t = (1, 0, 4, 0).
# t = (1, 0, 4, 0)
# print(t.index(1))


# # Q357. Convert list [1,2,3] to tuple.
# lst = [1,2,3]
# print(tuple(lst))


#  Q358. Check if 3 is in (1,2,3).
# t = (1,2,3)
# print(3 in t)


#  Q359. Swap values of x=5 and y=7 using tuple unpacking.
# x = 5
# y = 7
# x, y = 7, 5
# print(x, y)


#  Q360. Nested access: get 3 from t=(1,(2,3),(4,5)).
# t=(1,(2,3),(4,5))
# print(t[1][1])


# Q361. Access third element of t = (2, 1, 6, 3).
# t = (2, 1, 6, 3)
# print(t[2])


# Q362. Slice t = (2, 1, 6, 3) from 1 to 3.
# t = (2, 1, 6, 3)
# print(t[1:3])


# Q363. Concatenate tuples t=(2, 1, 6, 3) and u=(3, 2, 8, 6).
# t = (2, 1, 6, 3)
# u = (3, 2, 8, 6)
# print(t + u)  


# Q364. Unpack t = (2, 1, 6, 3) into a,b,c,d.
# t = (2, 1, 6, 3)
# a, b, c, d = t
# print(a, b, c, d)


# Q365. Count 0 in t = (2, 1, 6, 3).
# t = (2, 1, 6, 3)
# print(t.count(0)) 


# Q366. Find index of first 2 in t = (2, 1, 6, 3).
# t = (2, 1, 6, 3)
# print(t.index(2))


# Q367. Convert list [1,2,3] to tuple.
# lst = [1, 2, 3]
# print(tuple(lst))


# Q368. Check if 3 is in (1,2,3).
# t = (1, 2, 3)
# print(3 in t)


# Q369. Swap values of x=5 and y=7 using tuple unpacking.
# x, y = 5, 7
# x, y = y, x
# print(x, y)


# Q370. Nested access: get 3 from t=(1,(2,3),(4,5)).
# t = (1, (2, 3), (4, 5))
# print(t[1][1])   


# Q371. Access third element of t = (3, 2, 8, 6).
# t = (3, 2, 8, 6)
# print(t[3])


#  Q372. Slice t = (3, 2, 8, 6) from 1 to 3.
# t = (3, 2, 8, 6)
# print(t[1:3])


#  Q373. Concatenate tuples t=(3, 2, 8, 6) and u=(4, 3, 1, 9).
# t=(3, 2, 8, 6)
# u=(4, 3, 1, 9)
# print(t + u)


#  Q374. Unpack t = (3, 2, 8, 6) into a,b,c,d.
# t = (3, 2, 8, 6)
# a = 'a', 'b', 'c', 'd'
# t = a
# print(t)


#  Q375. Count 1 in t = (3, 2, 8, 6).
# t = (3, 2, 8, 6)
# print(t.count(1))


#  Q376. Find index of first 3 in t = (3, 2, 8, 6).
# t = (3, 2, 8, 6)
# print(t.index(3))


#  Q377. Convert list [1,2,3] to tuple.
# lst = [1,2,3]
# print(tuple(lst))


# Q378. Check if 3 is in (1,2,3).
# t = (1,2,3)
# print(3 in t)


# Q379. Swap values of x=5 and y=7 using tuple unpacking.
# x = 5
# y = 7
# x, y = 7, 5
# print(x, y)


# Q380. Nested access: get 3 from t=(1,(2,3),(4,5)).
# t=(1,(2,3),(4,5))
# print(t[1][1])


# Q381. Access third element of t = (4, 3, 1, 9).
# t = (4, 3, 1, 9)
# print(t[3])


# Q382. Slice t = (4, 3, 1, 9) from 1 to 3.
# t = (4, 3, 1, 9)
# print(t[1:3])


# Q383. Concatenate tuples t=(4, 3, 1, 9) and u=(0, 4, 3, 1).
# t=(4, 3, 1, 9)
# u=(0, 4, 3, 1)
# print(t+u)


#  Q384. Unpack t = (4, 3, 1, 9) into a,b,c,d.
# t = (4, 3, 1, 9)
# a,b,c,d = t
# print(t)


# Q385. Count 2 in t = (4, 3, 1, 9).
# t = (4, 3, 1, 9)
# print(t.count(2))


# Q386. Find index of first 4 in t = (4, 3, 1, 9).
# t = (4, 3, 1, 9)
# print(t.index(4))


# Q387. Convert list [1,2,3] to tuple.
# lst = [1,2,3]
# print(tuple(lst))


# Q388. Check if 3 is in (1,2,3).
# lst = (1,2,3)
# print(3 in lst)


#  Q389. Swap values of x=5 and y=7 using tuple unpacking.
# x=5
# y=7
# x, y = 7, 5
# print(x,y)


# Q390. Nested access: get 3 from t=(1,(2,3),(4,5)).
# t=(1,(2,3),(4,5))
# print(t[1][1])


#  Q391. Access third element of t = (0, 4, 3, 1).
# t = (0, 4, 3, 1)
# print(t[3])


# Q392. Slice t = (0, 4, 3, 1) from 1 to 3.
# t = (0, 4, 3, 1)
# print(t[1:3])


#  Q393. Concatenate tuples t=(0, 4, 3, 1) and u=(1, 5, 5, 4).
# t=(0, 4, 3, 1)
# u=(1, 5, 5, 4)
# print(t + u)


#  Q394. Unpack t = (0, 4, 3, 1) into a,b,c,d.
# t = (0, 4, 3, 1)
# k = ('a, b, c, d')
# t = k
# print(t)


# Q395. Count 0 in t = (0, 4, 3, 1).
# t = (0, 4, 3, 1)
# print(t.count(0))


# Q396. Find index of first 0 in t = (0, 4, 3, 1).
# t = (0, 4, 3, 1)
# print(t.index(0))


# Q397. Convert list [1,2,3] to tuple.
# lst = [1,2,3]
# print(tuple(lst))


# Q398. Check if 3 is in (1,2,3).
# t = (1,2,3)
# print(3 in t)


#  Q399. Swap values of x=5 and y=7 using tuple unpacking.
# x = 5
# y = 7
# x, y = 7, 5
# print(x, y)


#  Q400. Nested access: get 3 from t=(1,(2,3),(4,5)).
# t=(1,(2,3),(4,5))
# print(t[1][1])


#  Q401. Access third element of t = (1, 5, 5, 4).
# t = (1, 5, 5, 4)
# print(t[3])


# Q402. Slice t = (1, 5, 5, 4) from 1 to 3.
# t = (1, 5, 5, 4)
# print(t[1:3])


# Q403. Concatenate tuples t=(1, 5, 5, 4) and u=(2, 6, 7, 7).
# t=(1, 5, 5, 4)
# u=(2, 6, 7, 7)
# print(t + u)


#  Q404. Unpack t = (1, 5, 5, 4) into a,b,c,d.
# t = (1, 5, 5, 4)
# a, b, c, d = t
# print(a, b, c, d)


#  Q405. Count 1 in t = (1, 5, 5, 4).
# t = (1, 5, 5, 4)
# print(t.count(1))


#  Q406. Find index of first 1 in t = (1, 5, 5, 4).
# t = (1, 5, 5, 4)
# print(t.index(1))


# Q407. Convert list [1,2,3] to tuple.
# lst = [1,2,3]
# print(tuple(lst))


#  Q408. Check if 3 is in (1,2,3).
# t = (1,2,3)
# print(3 in t)


#  Q409. Swap values of x=5 and y=7 using tuple unpacking.
# x = 5
# y = 7
# x, y = 7, 5
# print(x, y)


# Q410. Nested access: get 3 from t=(1,(2,3),(4,5)).
# t=(1,(2,3),(4,5))
# print(t[1][1])


# Q411. Access third element of t = (2, 6, 7, 7).
# t = (2, 6, 7, 7)
# print(t[3])


#  Q412. Slice t = (2, 6, 7, 7) from 1 to 3.
# t = (2, 6, 7, 7)
# print(t[1:3])


# Q413. Concatenate tuples t=(2, 6, 7, 7) and u=(3, 0, 0, 10).
# t=(2, 6, 7, 7)
# u=(3, 0, 0, 10)
# print(t + u)


# Q414. Unpack t = (2, 6, 7, 7) into a,b,c,d.
# t = (2, 6, 7, 7) 
# a,b,c,d = t
# print(a,b,c,d)


#  Q415. Count 2 in t = (2, 6, 7, 7).
# t = (2, 6, 7, 7)
# print(t.count(2))


#  Q416. Find index of first 2 in t = (2, 6, 7, 7).
# t = (2, 6, 7, 7)
# print(t.index(2))


# Q417. Convert list [1,2,3] to tuple.
# lst = [1,2,3]
# print(tuple(lst))


# Q418. Check if 3 is in (1,2,3).
# t = (1,2,3)
# print(3 in t)


#  Q419. Swap values of x=5 and y=7 using tuple unpacking.
# x = 5
# y = 7
# x, y = 7, 5
# print(x, y)


#  Q420. Nested access: get 3 from t=(1,(2,3),(4,5)).
# t=(1,(2,3),(4,5))
# print(t[1][1])


# Q421. Access third element of t = (3, 0, 0, 10).
# t = (3, 0, 0, 10)
# print(t[3])


#  Q422. Slice t = (3, 0, 0, 10) from 1 to 3.
# t = (3, 0, 0, 10)
# print(t[1:3])


# Q423. Concatenate tuples t=(3, 0, 0, 10) and u=(4, 1, 2, 2).
# t=(3, 0, 0, 10) 
# u=(4, 1, 2, 2)
# print(t + u)


# Q424. Unpack t = (3, 0, 0, 10) into a,b,c,d.
# t = (3, 0, 0, 10)
# a,b,c,d = t
# print(a,b,c,d)


#  Q425. Count 0 in t = (3, 0, 0, 10).
# t = (3, 0, 0, 10)
# print(t.count(0))


#  Q426. Find index of first 3 in t = (3, 0, 0, 10).
# t = (3, 0, 0, 10)
# print(t.index(3))


#  Q427. Convert list [1,2,3] to tuple.
# lst = [1,2,3]
# print(tuple(lst))


#  Q428. Check if 3 is in (1,2,3).
# t = (1,2,3)
# print(3 in t)


#  Q429. Swap values of x=5 and y=7 using tuple unpacking.
# x = 5
# y = 7
# x, y = 7, 5
# print(x, y)


# Q430. Nested access: get 3 from t=(1,(2,3),(4,5)).
# t=(1,(2,3),(4,5))
# print(t[1][1])


# Q431. Access third element of t = (4, 1, 2, 2).
# t = (4, 1, 2, 2)
# print(t[3])



#  Q432. Slice t = (4, 1, 2, 2) from 1 to 3.
# t = (4, 1, 2, 2)
# print(t[1:3])


#  Q433. Concatenate tuples t=(4, 1, 2, 2) and u=(0, 2, 4, 5)
# t=(4, 1, 2, 2)
# u=(0, 2, 4, 5)
# print(t + u)


#  Q434. Unpack t = (4, 1, 2, 2) into a,b,c,d.
# t = (4, 1, 2, 2) 
# a,b,c,d = (4, 1, 2, 2)
# print(a,b,c,d)


#  Q435. Count 1 in t = (4, 1, 2, 2).
# t = (4, 1, 2, 2)
# print(t.count(t))


# Q436. Find index of first 4 in t = (4, 1, 2, 2).
# t = (4, 1, 2, 2)
# print(t.index(4))


#  Q437. Convert list [1,2,3] to tuple.
# lst = [1, 2, 3]
# print(tuple(lst))


# Q438. Check if 3 is in (1,2,3).
# lst = (1, 2, 3)
# print(3 in lst)


#  Q439. Swap values of x=5 and y=7 using tuple unpacking.
# x = 5
# y = 7
# x, y = 7, 5
# print(x, y)


# Q440. Nested access: get 3 from t=(1,(2,3),(4,5)).
# t=(1,(2,3),(4,5)) 
# print(t[1][1])


# Q441. Access third element of t = (0, 2, 4, 5).
# t = (0, 2, 4, 5)
# print(t[3])


#  Q442. Slice t = (0, 2, 4, 5) from 1 to 3.
# t = (0, 2, 4, 5)
# print(t[1:3])


#  Q443. Concatenate tuples t=(0, 2, 4, 5) and u=(1, 3, 6, 8).
# t=(0, 2, 4, 5)
# u=(1, 3, 6, 8)
# print(t + u)


# Q444. Unpack t = (0, 2, 4, 5) into a,b,c,d.
# t = (0, 2, 4, 5)
# a,b,c,d = (0, 2, 4, 5)
# print(a, b, c, d)


#  Q445. Count 2 in t = (0, 2, 4, 5).
# t = (0, 2, 4, 5)
# print(t.count(2))


#  Q446. Find index of first 0 in t = (0, 2, 4, 5).
# t = (0, 2, 4, 5)
# print(t.index(0))


#  Q447. Convert list [1,2,3] to tuple.
# lst = [1,2,3]
# print(tuple(lst))


# Q448. Check if 3 is in (1,2,3).
# lst = (1,2,3)
# print(3 in lst)


#  Q449. Swap values of x=5 and y=7 using tuple unpacking.
# x=5
# y = 7
# x, y = 7, 5
# print(x, y)


#  Q450. Nested access: get 3 from t=(1,(2,3),(4,5)).
# t=(1,(2,3),(4,5))
# print(t[1][1])


# Q451. Union of sets a={1, 2, 3, 4, 5, 6} and b={1, 2, 3, 4, 5, 6, 7, 8}.
# a={1, 2, 3, 4, 5, 6}
# b={1, 2, 3, 4, 5, 6, 7, 8}
# print(a|b)


#  Q452. Intersection of sets a={1, 2, 3, 4, 5, 6} and b={1, 2, 3, 4, 5, 6, 7, 8}.
# a={1, 2, 3, 4, 5, 6}
# b={1, 2, 3, 4, 5, 6, 7, 8}
# print(a&b)


#  Q453. Difference a−b for a={1, 2, 3, 4, 5, 6}, b={1, 2, 3, 4, 5, 6, 7, 8}.
# a={1, 2, 3, 4, 5, 6}
# b={1, 2, 3, 4, 5, 6, 7, 8}
# print(a - b)


#  Q454. Symmetric difference for a={1, 2, 3, 4, 5, 6}, b={1, 2, 3, 4, 5, 6, 7, 8}.
# a={1, 2, 3, 4, 5, 6}
# b={1, 2, 3, 4, 5, 6, 7, 8}
# print(a^b)


#  Q455. Add element 1 to set a={1, 2, 3, 4, 5, 6}.
# a={1, 2, 3, 4, 5, 6}
# a.add(1)
# print(a)


# Q456. Remove element 1 from set a={1, 2, 3, 4, 5, 6} if present.
# a={1, 2, 3, 4, 5, 6}
# a.remove(1)
# print(a)



#  Q457. Check if a={1, 2, 3, 4, 5, 6} is subset of b={1, 2, 3, 4, 5, 6, 7, 8}.
# a={1, 2, 3, 4, 5, 6}
# b={1, 2, 3, 4, 5, 6, 7, 8}
# print(a.issubset(b))


# Q458. Unique values from list [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6].
# lst = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
# unique = []
# for i in lst:
#     if i not in unique:
#         unique.append(i)
# print(unique)     


#  Q459. Set comprehension: squares of 1..5.
# squares = {i**2 for i in range(1, 6)}
# print(squares)


# Q460. Find duplicates in list [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6].
# a = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
# duplicates = (i for i in a if a.count(i)>1)
# print(duplicates)


#  Q461. Union of sets a={1, 2, 3, 4, 5, 6, 7} and b={1, 2, 3, 4, 5, 6, 7, 8, 9}.
# a={1, 2, 3, 4, 5, 6, 7}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(a|b)


#  Q462. Intersection of sets a={1, 2, 3, 4, 5, 6, 7} and b={1, 2, 3, 4, 5, 6, 7, 8, 9}.
# a={1, 2, 3, 4, 5, 6, 7}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(a&b)


#  Q463. Difference a−b for a={1, 2, 3, 4, 5, 6, 7}, b={1, 2, 3, 4, 5, 6, 7, 8, 9}.
# a={1, 2, 3, 4, 5, 6, 7}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(a-b)


#  Q464. Symmetric difference for a={1, 2, 3, 4, 5, 6, 7}, b={1, 2, 3, 4, 5, 6, 7, 8, 9}.
# a={1, 2, 3, 4, 5, 6, 7}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(a^b)


#  Q465. Add element 2 to set a={1, 2, 3, 4, 5, 6, 7}.
# a={1, 2, 3, 4, 5, 6, 7}
# a.add(2)
# print(a)


# Q466. Remove element 2 from set a={1, 2, 3, 4, 5, 6, 7} if present.
# a={1, 2, 3, 4, 5, 6, 7}
# a.remove(2)
# print(a)


#  Q467. Check if a={1, 2, 3, 4, 5, 6, 7} is subset of b={1, 2, 3, 4, 5, 6, 7, 8, 9}.
# a={1, 2, 3, 4, 5, 6, 7}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9}
# subset = a.issubset(b)
# print(subset)


#  Q468. Unique values from list [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7].
# lst = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]
# unique = []
# for i in lst :
#     if i not in unique:
#         unique.append(i)
# print(unique)     
# unique = list(set(lst))
# print(unique)   


#  Q469. Set comprehension: squares of 1..5.
# squares = {i**2 for i in range(1, 6)}
# print(squares)


# Q470. Find duplicates in list [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7].
# lst = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]
# duplicates = {i for i in lst if lst.count(i)>1}
# print(duplicates)


# Q471. Union of sets a={1, 2, 3, 4, 5, 6, 7, 8} and b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}.
# a={1, 2, 3, 4, 5, 6, 7, 8}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(a|b)


# Q472. Intersection of sets a={1, 2, 3, 4, 5, 6, 7, 8} and b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}.
# a={1, 2, 3, 4, 5, 6, 7, 8}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(a&b)


# Q473. Difference a−b for a={1, 2, 3, 4, 5, 6, 7, 8}, b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}.
# a={1, 2, 3, 4, 5, 6, 7, 8}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(a-b)


#  Q474. Symmetric difference for a={1, 2, 3, 4, 5, 6, 7, 8}, b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}.
# a={1, 2, 3, 4, 5, 6, 7, 8}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(a^b)


#  Q475. Add element 3 to set a={1, 2, 3, 4, 5, 6, 7, 8}.
# a={1, 2, 3, 4, 5, 6, 7, 8}
# a.add(3)
# print(a)


#  Q476. Remove element 3 from set a={1, 2, 3, 4, 5, 6, 7, 8} if present.
# a={1, 2, 3, 4, 5, 6, 7, 8}
# a.remove(3)
# print(a)


#  Q477. Check if a={1, 2, 3, 4, 5, 6, 7, 8} is subset of b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}.
# a={1, 2, 3, 4, 5, 6, }
# b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# c = a.issubset(b)
# print(c)


#  Q478. Unique values from list [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8].
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
# unique = []
# for i in lst:
#     if i not in unique:
#         unique.append(i)
# print(unique)  


#  Q479. Set comprehension: squares of 1..5.
# squares = {i**2 for i in range(1, 6)}
# print(squares)


# Q480. Find duplicates in list [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8].
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
# duplicates = {i for i in lst if lst.count(i)>1}
# print(duplicates)


# Q481. Union of sets a={1, 2, 3, 4, 5, 6, 7, 8, 9} and b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# print(a|b)


# Q482. Intersection of sets a={1, 2, 3, 4, 5, 6, 7, 8, 9} and b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# print(a&b)


#  Q483. Difference a−b for a={1, 2, 3, 4, 5, 6, 7, 8, 9}, b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# print(a-b)


#  Q484. Symmetric difference for a={1, 2, 3, 4, 5, 6, 7, 8, 9}, b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# print(a^b)


#  Q485. Add element 4 to set a={1, 2, 3, 4, 5, 6, 7, 8, 9}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9}
# a.add(4)
# print(a)


# Q486. Remove element 4 from set a={1, 2, 3, 4, 5, 6, 7, 8, 9} if present.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9}
# a.remove(4)
# print(a)


# Q487. Check if a={1, 2, 3, 4, 5, 6, 7, 8, 9} is subset of b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# print(a.issubset(b))


# Q488. Unique values from list [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9].
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# unique = []
# for i in lst:
#     if i not in unique:
#         unique.append(i)
# print(unique)


#  Q489. Set comprehension: squares of 1..5.
# squares = {i**2 for i in range(1, 6)}
# print(squares)


# Q490. Find duplicates in list [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9].
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# duplicates = {i for i in lst if lst.count(i)>1}
# print(duplicates)


# Q491. Union of sets a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10} and b={1, 2, 3, 4, 5}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# b={1, 2, 3, 4, 5}
# print(a|b)


#  Q492. Intersection of sets a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10} and b={1, 2, 3, 4, 5}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# b={1, 2, 3, 4, 5}
# print(a&b)


#  Q493. Difference a−b for a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, b={1, 2, 3, 4, 5}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# b={1, 2, 3, 4, 5}
# print(a-b)


# Q494. Symmetric difference for a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, b={1, 2, 3, 4, 5}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# b={1, 2, 3, 4, 5}
# print(a^b)


# Q495. Add element 5 to set a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# a.add(5)
# print(a)


# Q496. Remove element 0 from set a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10} if present.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# a.remove(0)
# print(a)


#  Q497. Check if a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10} is subset of b={1, 2, 3, 4, 5}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# b={1, 2, 3, 4, 5}
# print(a.issubset(b))


# Q498. Unique values from list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# unique = []
# for i in lst:
#     if i not in unique:
#         unique.append(i)
# print(unique)        


# Q499. Set comprehension: squares of 1..5.
# squares = {i**2 for i in range(1, 6)}
# print(squares)


#  Q500. Find duplicates in list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# duplicate = {i for i in lst if lst.count(i)>1}
# print(duplicate)


#  Q501. Union of sets a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11} and b={1, 2, 3, 4, 5, 6}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# b={1, 2, 3, 4, 5, 6}
# print(a|b)


# Q502. Intersection of sets a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11} and b={1, 2, 3, 4, 5, 6}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# b={1, 2, 3, 4, 5, 6}
# print(a&b)


#  Q503. Difference a−b for a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, b={1, 2, 3, 4, 5, 6}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# b={1, 2, 3, 4, 5, 6}
# print(a-b)


#  Q504. Symmetric difference for a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, b={1, 2, 3, 4, 5, 6}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# b={1, 2, 3, 4, 5, 6}
# print(a^b)


# Q505. Add element 6 to set a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# a.add(6)
# print(a)


#  Q506. Remove element 1 from set a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11} if present
# a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# a.remove(2)
# print(a)


#  Q507. Check if a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11} is subset of b={1, 2, 3, 4, 5, 6}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# b={1, 2, 3, 4, 5, 6}
# print(a.issubset(b))


# Q508. Unique values from list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# unique = []
# for i in lst:
#     if i not in unique:
#         unique.append(i)
# print(unique)


# Q509. Set comprehension: squares of 1..5.
# squares = {i**2 for i in range(1, 6)}
# print(squares)


# Q510. Find duplicates in list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# duplicates = {i for i in lst if lst.count(i)>1}
# print(duplicates)


# Q511. Union of sets a={1, 2, 3, 4, 5} and b={1, 2, 3, 4, 5, 6, 7}.
# a={1, 2, 3, 4, 5}
# b={1, 2, 3, 4, 5, 6, 7}
# print(a|b)


# Q512. Intersection of sets a={1, 2, 3, 4, 5} and b={1, 2, 3, 4, 5, 6, 7}.
# a={1, 2, 3, 4, 5}
# b={1, 2, 3, 4, 5, 6, 7}
# print(a&b)


# Q513. Difference a−b for a={1, 2, 3, 4, 5}, b={1, 2, 3, 4, 5, 6, 7}.
# a={1, 2, 3, 4, 5}
# b={1, 2, 3, 4, 5, 6, 7}
# print(a-b)


# Q514. Symmetric difference for a={1, 2, 3, 4, 5}, b={1, 2, 3, 4, 5, 6, 7}.
# a={1, 2, 3, 4, 5}
# b={1, 2, 3, 4, 5, 6, 7}
# print(a^b)


# Q515. Add element 7 to set a={1, 2, 3, 4, 5}.
# a={1, 2, 3, 4, 5}
# a.add(7)
# print(a)


# Q516. Remove element 2 from set a={1, 2, 3, 4, 5} if present.
# a={1, 2, 3, 4, 5}
# a.remove(2)
# print(a)


# Q517. Check if a={1, 2, 3, 4, 5} is subset of b={1, 2, 3, 4, 5, 6, 7}.
# a={1, 2, 3, 4, 5}
# b={1, 2, 3, 4, 5, 6, 7}
# print(a.issubset(b))


# Q518. Unique values from list [1, 2, 3, 4, 5, 1, 2, 3, 4, 5].
# lst=[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# unique=[]
# for i in lst:
#     if i not in unique:
#         unique.append(i)
# print(unique)


# Q519. Set comprehension: squares of 1..5.
# squares={i**2 for i in range(1,6)}
# print(squares)


# Q520. Find duplicates in list [1, 2, 3, 4, 5, 1, 2, 3, 4, 5].
# lst=[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# duplicates={i for i in lst if lst.count(i)>1}
# print(duplicates)


# Q521. Union of sets a={1, 2, 3, 4, 5, 6} and b={1, 2, 3, 4, 5, 6, 7, 8}.
# a={1, 2, 3, 4, 5, 6}
# b={1, 2, 3, 4, 5, 6, 7, 8}
# print(a|b)


# Q522. Intersection of sets a={1, 2, 3, 4, 5, 6} and b={1, 2, 3, 4, 5, 6, 7, 8}.
# a={1, 2, 3, 4, 5, 6}
# b={1, 2, 3, 4, 5, 6, 7, 8}
# print(a&b)


# Q523. Difference a−b for a={1, 2, 3, 4, 5, 6}, b={1, 2, 3, 4, 5, 6, 7, 8}.
# a={1, 2, 3, 4, 5, 6}
# b={1, 2, 3, 4, 5, 6, 7, 8}
# print(a-b)


# Q524. Symmetric difference for a={1, 2, 3, 4, 5, 6}, b={1, 2, 3, 4, 5, 6, 7, 8}.
# a={1, 2, 3, 4, 5, 6}
# b={1, 2, 3, 4, 5, 6, 7, 8}
# print(a^b)


# Q525. Add element 8 to set a={1, 2, 3, 4, 5, 6}.
# a={1, 2, 3, 4, 5, 6}
# a.add(8)
# print(a)


# Q526. Remove element 3 from set a={1, 2, 3, 4, 5, 6} if present.
# a={1, 2, 3, 4, 5, 6}
# a.remove(3)
# print(a)


# Q527. Check if a={1, 2, 3, 4, 5, 6} is subset of b={1, 2, 3, 4, 5, 6, 7, 8}.
# a={1, 2, 3, 4, 5, 6}
# b={1, 2, 3, 4, 5, 6, 7, 8}
# print(a.issubset(b))


# Q528. Unique values from list [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6].
# lst=[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
# unique=[]
# for i in lst:
#     if i not in unique:
#         unique.append(i)
# print(unique)


# Q529. Set comprehension: squares of 1..5.
# squares={i**2 for i in range(1,6)}
# print(squares)


# Q530. Find duplicates in list [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6].
# lst=[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
# duplicates={i for i in lst if lst.count(i)>1}
# print(duplicates)


# Q531. Union of sets a={1,2,3,4,5,6,7} and b={1,2,3,4,5,6,7,8,9}.
# a={1,2,3,4,5,6,7}
# b={1,2,3,4,5,6,7,8,9}
# print(a|b)


# Q532. Intersection of sets a={1,2,3,4,5,6,7} and b={1,2,3,4,5,6,7,8,9}.
# a={1,2,3,4,5,6,7}
# b={1,2,3,4,5,6,7,8,9}
# print(a&b)


# Q533. Difference a−b for a={1,2,3,4,5,6,7}, b={1,2,3,4,5,6,7,8,9}.
# a={1,2,3,4,5,6,7}
# b={1,2,3,4,5,6,7,8,9}
# print(a-b)


# Q534. Symmetric difference for a={1,2,3,4,5,6,7}, b={1,2,3,4,5,6,7,8,9}.
# a={1,2,3,4,5,6,7}
# b={1,2,3,4,5,6,7,8,9}
# print(a^b)


# Q535. Add element 9 to set a={1,2,3,4,5,6,7}.
# a={1,2,3,4,5,6,7}
# a.add(9)
# print(a)


# Q536. Remove element 4 from set a={1,2,3,4,5,6,7} if present.
# a={1,2,3,4,5,6,7}
# a.remove(4)
# print(a)


# Q537. Check if a={1,2,3,4,5,6,7} is subset of b={1,2,3,4,5,6,7,8,9}.
# a={1,2,3,4,5,6,7}
# b={1,2,3,4,5,6,7,8,9}
# print(a.issubset(b))


# Q538. Unique values from list [1,2,3,4,5,6,7,1,2,3,4,5,6,7].
# lst=[1,2,3,4,5,6,7,1,2,3,4,5,6,7]
# unique=[]
# for i in lst:
#     if i not in unique:
#         unique.append(i)
# print(unique)


# Q539. Set comprehension: squares of 1..5.
# squares={i**2 for i in range(1,6)}
# print(squares)


# Q540. Find duplicates in list [1,2,3,4,5,6,7,1,2,3,4,5,6,7].
# lst=[1,2,3,4,5,6,7,1,2,3,4,5,6,7]
# duplicates={i for i in lst if lst.count(i)>1}
# print(duplicates)


# Q541. Union of sets a={1,2,3,4,5,6,7,8} and b={1,2,3,4,5,6,7,8,9,10}.
# a={1,2,3,4,5,6,7,8}
# b={1,2,3,4,5,6,7,8,9,10}
# print(a|b)


# Q542. Intersection of sets a={1,2,3,4,5,6,7,8} and b={1,2,3,4,5,6,7,8,9,10}.
# a={1,2,3,4,5,6,7,8}
# b={1,2,3,4,5,6,7,8,9,10}
# print(a&b)


# Q543. Difference a−b for a={1,2,3,4,5,6,7,8}, b={1,2,3,4,5,6,7,8,9,10}.
# a={1,2,3,4,5,6,7,8}
# b={1,2,3,4,5,6,7,8,9,10}
# print(a-b)


# Q544. Symmetric difference for a={1,2,3,4,5,6,7,8}, b={1,2,3,4,5,6,7,8,9,10}.
# a={1,2,3,4,5,6,7,8}
# b={1,2,3,4,5,6,7,8,9,10}
# print(a^b)


# Q545. Add element 10 to set a={1,2,3,4,5,6,7,8}.
# a={1,2,3,4,5,6,7,8}
# a.add(10)
# print(a)


# Q546. Remove element 5 from set a={1,2,3,4,5,6,7,8} if present.
# a={1,2,3,4,5,6,7,8}
# a.remove(5)
# print(a)


# Q547. Check if a={1,2,3,4,5,6,7,8} is subset of b={1,2,3,4,5,6,7,8,9,10}.
# a={1,2,3,4,5,6,7,8}
# b={1,2,3,4,5,6,7,8,9,10}
# print(a.issubset(b))


# Q548. Unique values from list [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8].
# lst=[1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
# unique=[]
# for i in lst:
#     if i not in unique:
#         unique.append(i)
# print(unique)


# Q549. Set comprehension: squares of 1..5.
# squares={i**2 for i in range(1,6)}
# print(squares)


# Q550. Find duplicates in list [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8].
# lst=[1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
# duplicates={i for i in lst if lst.count(i)>1}
# print(duplicates)


# Q551. Union of sets a={1,2,3,4,5,6,7,8,9} and b={1,2,3,4,5,6,7,8,9,10,11}.
# a={1,2,3,4,5,6,7,8,9}
# b={1,2,3,4,5,6,7,8,9,10,11}
# print(a|b)


# Q552. Intersection of sets a={1,2,3,4,5,6,7,8,9} and b={1,2,3,4,5,6,7,8,9,10,11}.
# a={1,2,3,4,5,6,7,8,9}
# b={1,2,3,4,5,6,7,8,9,10,11}
# print(a&b)


# Q553. Difference a−b for a={1,2,3,4,5,6,7,8,9}, b={1,2,3,4,5,6,7,8,9,10,11}.
# a={1,2,3,4,5,6,7,8,9}
# b={1,2,3,4,5,6,7,8,9,10,11}
# print(a-b)


# Q554. Symmetric difference for a={1,2,3,4,5,6,7,8,9}, b={1,2,3,4,5,6,7,8,9,10,11}.
# a={1,2,3,4,5,6,7,8,9}
# b={1,2,3,4,5,6,7,8,9,10,11}
# print(a^b)


# Q555. Add element 11 to set a={1,2,3,4,5,6,7,8,9}.
# a={1,2,3,4,5,6,7,8,9}
# a.add(11)
# print(a)


# Q556. Remove element 6 from set a={1,2,3,4,5,6,7,8,9} if present.
# a={1,2,3,4,5,6,7,8,9}
# a.remove(6)
# print(a)


# Q557. Check if a={1,2,3,4,5,6,7,8,9} is subset of b={1,2,3,4,5,6,7,8,9,10,11}.
# a={1,2,3,4,5,6,7,8,9}
# b={1,2,3,4,5,6,7,8,9,10,11}
# print(a.issubset(b))


# Q558. Unique values from list [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9].
# lst=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
# unique=[]
# for i in lst:
#     if i not in unique:
#         unique.append(i)
# print(unique)


# Q559. Set comprehension: squares of 1..5.
# squares={i**2 for i in range(1,6)}
# print(squares)


# Q560. Find duplicates in list [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9].
# lst=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
# duplicates={i for i in lst if lst.count(i)>1}
# print(duplicates)


# Q561. Union of sets a={1,2,3,4,5,6,7,8,9,10} and b={1,2,3,4,5,6,7,8,9,10,11,12}.
# a={1,2,3,4,5,6,7,8,9,10}
# b={1,2,3,4,5,6,7,8,9,10,11,12}
# print(a|b)


# Q562. Intersection of sets a={1,2,3,4,5,6,7,8,9,10} and b={1,2,3,4,5,6,7,8,9,10,11,12}.
# a={1,2,3,4,5,6,7,8,9,10}
# b={1,2,3,4,5,6,7,8,9,10,11,12}
# print(a&b)


# Q563. Difference a−b for a={1,2,3,4,5,6,7,8,9,10}, b={1,2,3,4,5,6,7,8,9,10,11,12}.
# a={1,2,3,4,5,6,7,8,9,10}
# b={1,2,3,4,5,6,7,8,9,10,11,12}
# print(a-b)


# Q564. Symmetric difference for a={1,2,3,4,5,6,7,8,9,10}, b={1,2,3,4,5,6,7,8,9,10,11,12}.
# a={1,2,3,4,5,6,7,8,9,10}
# b={1,2,3,4,5,6,7,8,9,10,11,12}
# print(a^b)


# Q565. Add element 12 to set a={1,2,3,4,5,6,7,8,9,10}.
# a={1,2,3,4,5,6,7,8,9,10}
# a.add(12)
# print(a)


# Q566. Remove element 7 from set a={1,2,3,4,5,6,7,8,9,10} if present.
# a={1,2,3,4,5,6,7,8,9,10}
# a.remove(7)
# print(a)


# Q567. Check if a={1,2,3,4,5,6,7,8,9,10} is subset of b={1,2,3,4,5,6,7,8,9,10,11,12}.
# a={1,2,3,4,5,6,7,8,9,10}
# b={1,2,3,4,5,6,7,8,9,10,11,12}
# print(a.issubset(b))


# Q568. Unique values from list [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10].
# lst=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
# unique=[]
# for i in lst:
#     if i not in unique:
#         unique.append(i)
# print(unique)


# Q569. Set comprehension: squares of 1..5.
# squares={i**2 for i in range(1,6)}
# print(squares)


# Q570. Find duplicates in list [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10].
# lst=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
# duplicates={i for i in lst if lst.count(i)>1}
# print(duplicates)



#  Q571. Union of sets a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11} and b={1, 2, 3, 4, 5, 6}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# b={1, 2, 3, 4, 5, 6}
# print(a|b)


#  Q572. Intersection of sets a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11} and b={1, 2, 3, 4, 5, 6}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# b={1, 2, 3, 4, 5, 6}
# print(a&b)


#  Q573. Difference a−b for a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, b={1, 2, 3, 4, 5, 6}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# b={1, 2, 3, 4, 5, 6}
# print(a-b)


#  Q574. Symmetric difference for a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, b={1, 2, 3, 4, 5, 6}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# b={1, 2, 3, 4, 5, 6}
# print(a^b)


# Q575. Add element 3 to set a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# a.add(3)
# print(a)


# Q576. Remove element 3 from set a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11} if present.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# a.remove(3)
# print(a)


#  Q577. Check if a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11} is subset of b={1, 2, 3, 4, 5, 6}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# b={1, 2, 3, 4, 5, 6}
# print(a.issubset(b))


# Q578. Unique values from list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# unique = []
# for i in lst:
#     if i not in unique:
#         unique.append(i)
# print(unique)        


#  Q579. Set comprehension: squares of 1..5.
# squares = {i**2 for i in range(1, 6)}
# print(squares)


# Q580. Find duplicates in list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# duplicates = {i for i in lst if lst.count(i)>1}
# print(duplicates)


#  Q581. Union of sets a={1, 2, 3, 4, 5} and b={1, 2, 3, 4, 5, 6, 7}.
# a={1, 2, 3, 4, 5}
# b={1, 2, 3, 4, 5, 6, 7}
# print(a|b)


#  Q582. Intersection of sets a={1, 2, 3, 4, 5} and b={1, 2, 3, 4, 5, 6, 7}.
# a={1, 2, 3, 4, 5}
# b={1, 2, 3, 4, 5, 6, 7}
# print(a&b)


#  Q583. Difference a−b for a={1, 2, 3, 4, 5}, b={1, 2, 3, 4, 5, 6, 7}.
# a={1, 2, 3, 4, 5}
# b={1, 2, 3, 4, 5, 6, 7}
# print(a-b)


# Q584. Symmetric difference for a={1, 2, 3, 4, 5}, b={1, 2, 3, 4, 5, 6, 7}.
# a={1, 2, 3, 4, 5}
# b={1, 2, 3, 4, 5, 6, 7}
# print(a^b)


# Q585. Add element 4 to set a={1, 2, 3, 4, 5}.
# a={1, 2, 3, 4, 5}
# a.add(4)
# print(a)


#  Q586. Remove element 4 from set a={1, 2, 3, 4, 5} if present.
# a={1, 2, 3, 4, 5} 
# a.remove(4)
# print(a)


# Q587. Check if a={1, 2, 3, 4, 5} is subset of b={1, 2, 3, 4, 5, 6, 7}.
# a={1, 2, 3, 4, 5}
# b={1, 2, 3, 4, 5, 6, 7}
# print(a.issubset(b))


# Q588. Unique values from list [1, 2, 3, 4, 5, 1, 2, 3, 4, 5].
# lst = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# unique = {i for i in lst}
# print(unique)


# Q589. Set comprehension: squares of 1..5.
# squares = {i**2 for i in range(1,6)}
# print(squares)


# Q590. Find duplicates in list [1, 2, 3, 4, 5, 1, 2, 3, 4, 5].
# lst = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# duplicates = {i for i in lst if lst.count(i)>1}
# print(duplicates)


# Q591. Union of sets a={1, 2, 3, 4, 5, 6} and b={1, 2, 3, 4, 5, 6, 7, 8}.
# a={1, 2, 3, 4, 5, 6}
# b={1, 2, 3, 4, 5, 6, 7, 8}
# print(a|b)


#  Q592. Intersection of sets a={1, 2, 3, 4, 5, 6} and b={1, 2, 3, 4, 5, 6, 7, 8}.
# a={1, 2, 3, 4, 5, 6}
# b={1, 2, 3, 4, 5, 6, 7, 8}
# print(a&b)


#  Q593. Difference a−b for a={1, 2, 3, 4, 5, 6}, b={1, 2, 3, 4, 5, 6, 7, 8}.
# a={1, 2, 3, 4, 5, 6}
# b={1, 2, 3, 4, 5, 6, 7, 8}
# print(a-b)


#  Q594. Symmetric difference for a={1, 2, 3, 4, 5, 6}, b={1, 2, 3, 4, 5, 6, 7, 8}.
# a={1, 2, 3, 4, 5, 6}
# b={1, 2, 3, 4, 5, 6, 7, 8}
# print(a^b)


#  Q595. Add element 5 to set a={1, 2, 3, 4, 5, 6}.
# a={1, 2, 3, 4, 5, 6}
# a.add(5)
# print(a)


#  Q596. Remove element 0 from set a={1, 2, 3, 4, 5, 6} if present.
# a={1, 2, 3, 4, 5, 6}
# a.remove(0)
# print(a)


#  Q597. Check if a={1, 2, 3, 4, 5, 6} is subset of b={1, 2, 3, 4, 5, 6, 7, 8}.
# a={1, 2, 3, 4, 5, 6}
# b={1, 2, 3, 4, 5, 6, 7, 8}
# print(a.issubset(b))


#  Q598. Unique values from list [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6].
# lst = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
# unique = {i for i in lst}
# print(unique)


# Q599. Set comprehension: squares of 1..5.
# squares = {i**2 for i in range(1, 6)}
# print(squares)


# Q600. Find duplicates in list [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6].
# lst = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
# duplicates = {i for i in lst if lst.count(i)>1}
# print(duplicates)


# Q601. Union of sets a={1, 2, 3, 4, 5, 6, 7} and b={1, 2, 3, 4, 5, 6, 7, 8, 9}.
# a={1, 2, 3, 4, 5, 6, 7}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(a|b)


#  Q602. Intersection of sets a={1, 2, 3, 4, 5, 6, 7} and b={1, 2, 3, 4, 5, 6, 7, 8, 9}.
# a={1, 2, 3, 4, 5, 6, 7}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(a&b)


#  Q603. Difference a−b for a={1, 2, 3, 4, 5, 6, 7}, b={1, 2, 3, 4, 5, 6, 7, 8, 9}.
# a={1, 2, 3, 4, 5, 6, 7}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(a-b)


#  Q604. Symmetric difference for a={1, 2, 3, 4, 5, 6, 7}, b={1, 2, 3, 4, 5, 6, 7, 8, 9}.
# a={1, 2, 3, 4, 5, 6, 7}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(a^b)


#  Q605. Add element 6 to set a={1, 2, 3, 4, 5, 6, 7}.
# a={1, 2, 3, 4, 5, 6, 7}
# a.add(6)
# print(a)


# Q606. Remove element 1 from set a={1, 2, 3, 4, 5, 6, 7} if present.
# a={1, 2, 3, 4, 5, 6, 7}
# a.remove(1)
# print(a)


# Q607. Check if a={1, 2, 3, 4, 5, 6, 7} is subset of b={1, 2, 3, 4, 5, 6, 7, 8, 9}.
# a={1, 2, 3, 4, 5, 6, 7}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(a.issubset(b))


#  Q608. Unique values from list [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7].
# lst = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]
# unique = {i for i in lst}
# print(unique)


#  Q609. Set comprehension: squares of 1..5.
# squares = {i**2 for i in range(1, 6)}
# print(squares)


# Q610. Find duplicates in list [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7].
# lst = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]
# duplicates = {i for i in lst if lst.count(i)>1}
# print(duplicates)


#  Q611. Union of sets a={1, 2, 3, 4, 5, 6, 7, 8} and b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}.
# a={1, 2, 3, 4, 5, 6, 7, 8}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(a|b)


#  Q612. Intersection of sets a={1, 2, 3, 4, 5, 6, 7, 8} and b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}.
# a={1, 2, 3, 4, 5, 6, 7, 8}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(a&b)


#  Q613. Difference a−b for a={1, 2, 3, 4, 5, 6, 7, 8}, b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}.
# a={1, 2, 3, 4, 5, 6, 7, 8}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(a-b)


#  Q614. Symmetric difference for a={1, 2, 3, 4, 5, 6, 7, 8}, b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}.
# a={1, 2, 3, 4, 5, 6, 7, 8}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(a^b)


#  Q615. Add element 7 to set a={1, 2, 3, 4, 5, 6, 7, 8}.
# a = {1, 2, 3, 4, 5, 6, 7, 8}
# a.add(7)
# print(a)


# Q616. Remove element 2 from set a={1, 2, 3, 4, 5, 6, 7, 8} if present.
# a={1, 2, 3, 4, 5, 6, 7, 8}
# a.remove(2)
# print(a)


#  Q617. Check if a={1, 2, 3, 4, 5, 6, 7, 8} is subset of b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}.
# a={1, 2, 3, 4, 5, 6, 7, 8}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(a.issubset(b))


#  Q618. Unique values from list [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8].
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
# unique = {i for i in lst}
# print(unique)


# Q619. Set comprehension: squares of 1..5.
# squares = {i**2 for i in range(1, 6)}
# print(squares)


#  Q620. Find duplicates in list [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8].
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
# duplicates = {i for i in lst if lst.count(i)>1}
# print(duplicates)


# Q621. Union of sets a={1, 2, 3, 4, 5, 6, 7, 8, 9} and b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# print(a|b)


#  Q622. Intersection of sets a={1, 2, 3, 4, 5, 6, 7, 8, 9} and b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# print(a&b)


#  Q623. Difference a−b for a={1, 2, 3, 4, 5, 6, 7, 8, 9}, b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# print(a-b)


#  Q624. Symmetric difference for a={1, 2, 3, 4, 5, 6, 7, 8, 9}, b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# print(a^b)


#  Q625. Add element 8 to set a={1, 2, 3, 4, 5, 6, 7, 8, 9}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9}
# a.add(8)
# print(a)


#  Q626. Remove element 3 from set a={1, 2, 3, 4, 5, 6, 7, 8, 9} if present.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9} 
# a.remove(3)
# print(a)


#  Q627. Check if a={1, 2, 3, 4, 5, 6, 7, 8, 9} is subset of b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}.
# a={1, 2, 3, 4, 5, 6, 7, 8, 9}
# b={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# print(a.issubset(b))


# Q628. Unique values from list [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9].
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# unique = {i for i in lst}
# print(unique)


#  Q629. Set comprehension: squares of 1..5.
# squares = {i**2 for i in range(1, 6)}
# print(squares)


#  Q630. Find duplicates in list [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9].
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# duplicates = {i for i in lst if lst.count(i)>1}
# print(duplicates)


# Q631. Union of sets a={1,2,3,4,5,6,7,8,9,10} and b={1,2,3,4,5}.
# a={1,2,3,4,5,6,7,8,9,10}
# b={1,2,3,4,5}
# print(a|b)

# Q632. Intersection of sets a={1,2,3,4,5,6,7,8,9,10} and b={1,2,3,4,5}.
# a={1,2,3,4,5,6,7,8,9,10}
# b={1,2,3,4,5}
# print(a&b)

# Q633. Difference a−b for a={1,2,3,4,5,6,7,8,9,10}, b={1,2,3,4,5}.
# a={1,2,3,4,5,6,7,8,9,10}
# b={1,2,3,4,5}
# print(a-b)

# Q634. Symmetric difference for a={1,2,3,4,5,6,7,8,9,10}, b={1,2,3,4,5}.
# a={1,2,3,4,5,6,7,8,9,10}
# b={1,2,3,4,5}
# print(a^b)

# Q635. Add element 9 to set a={1,2,3,4,5,6,7,8,9,10}.
# a={1,2,3,4,5,6,7,8,9,10}
# a.add(9)
# print(a)

# Q636. Remove element 4 from set a={1,2,3,4,5,6,7,8,9,10} if present.
# a={1,2,3,4,5,6,7,8,9,10}
# a.remove(4)
# print(a)

# Q637. Check if a={1,2,3,4,5,6,7,8,9,10} is subset of b={1,2,3,4,5}.
# a={1,2,3,4,5,6,7,8,9,10}
# b={1,2,3,4,5}
# print(a.issubset(b))

# Q638. Unique values from list [1..10 twice].
# lst=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
# unique={i for i in lst}
# print(unique)

# Q639. Set comprehension: squares of 1..5.
# squares={i**2 for i in range(1,6)}
# print(squares)

# Q640. Find duplicates in list [1..10 twice].
# lst=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
# duplicates={i for i in lst if lst.count(i)>1}
# print(duplicates)

# Q641. Union of sets a={1..11} and b={1..6}.
# a={1,2,3,4,5,6,7,8,9,10,11}
# b={1,2,3,4,5,6}
# print(a|b)

# Q642. Intersection of sets a={1..11} and b={1..6}.
# a={1,2,3,4,5,6,7,8,9,10,11}
# b={1,2,3,4,5,6}
# print(a&b)

# Q643. Difference a−b for a={1..11}, b={1..6}.
# a={1,2,3,4,5,6,7,8,9,10,11}
# b={1,2,3,4,5,6}
# print(a-b)

# Q644. Symmetric difference for a={1..11}, b={1..6}.
# a={1,2,3,4,5,6,7,8,9,10,11}
# b={1,2,3,4,5,6}
# print(a^b)

# Q645. Add element 0 to set a={1..11}.
# a={1,2,3,4,5,6,7,8,9,10,11}
# a.add(0)
# print(a)

# Q646. Remove element 0 from set a={1..11} if present.
# a={1,2,3,4,5,6,7,8,9,10,11}
# a.remove(0)   
# print(a)

# Q647. Check if a={1..11} is subset of b={1..6}.
# a={1,2,3,4,5,6,7,8,9,10,11}
# b={1,2,3,4,5,6}
# print(a.issubset(b))

# Q648. Unique values from list [1..11 twice].
# lst=[1,2,3,4,5,6,7,8,9,10,11,1,2,3,4,5,6,7,8,9,10,11]
# unique={i for i in lst}
# print(unique)

# Q649. Set comprehension: squares of 1..5.
# squares={i**2 for i in range(1,6)}
# print(squares)

# Q650. Find duplicates in list [1..11 twice].
# lst=[1,2,3,4,5,6,7,8,9,10,11,1,2,3,4,5,6,7,8,9,10,11]
# duplicates={i for i in lst if lst.count(i)>1}
# print(duplicates)


#  Q651. Get value for key 'k2' in d={'k1': 2, 'k2': 3, 'k3': 4} with default 0.
# d={'k1': 2, 'k2': 3, 'k3': 4}
# print(d.get('k2', 0))


#  Q652. Update key 'k1' to 99 in d={'k1': 2, 'k2': 3, 'k3': 4}.
# d={'k1': 2, 'k2': 3, 'k3': 4}
# d['k1'] = 99
# print(d)


# Q653. Merge dicts d={'k1': 2, 'k2': 3, 'k3': 4} and e={'k1': 4, 'k2': 5, 'k3': 6, 'k4': 7, 'k5': 8} (Python 3.9+).
# d={'k1': 2, 'k2': 3, 'k3': 4}
# e={'k1': 4, 'k2': 5, 'k3': 6, 'k4': 7, 'k5': 8}
# # merged = d | e
# print(merged)
# d.update(e)
# print(d)


# Q654. Keys of d={'k1': 2, 'k2': 3, 'k3': 4}.
# d={'k1': 2, 'k2': 3, 'k3': 4}
# print(d.keys())


#  Q655. Values of d={'k1': 2, 'k2': 3, 'k3': 4}.
# d={'k1': 2, 'k2': 3, 'k3': 4}
# print(d.values())


#  Q656. Items of d={'k1': 2, 'k2': 3, 'k3': 4}.
# d={'k1': 2, 'k2': 3, 'k3': 4}
# print(d.items())


# Q657. Invert dict {'a':1,'b':2} (values unique).
# d = {'a':1,'b':2}
# inverted = {v: k for k, v in d.items()}
# print(inverted)
# inverted = dict((v, k) for k, v in d.items())
# print(inverted)


# Q658. Count frequency of elements in list [1,2,1,3,2,1] using dict.
# lst = [1,2,1,3,2,1]
# frequency = {}
# for i in lst:
#     frequency[i] = frequency.get(i, 0) + 1
# print(frequency) 


# Q659. Max key by value in d={'a':3,'b':7,'c':5}.
# d={'a':3,'b':7,'c':5}
# max_key = max(d, key=d.get)
# print(max_key)


#  Q660. Sort dict {'b':2,'a':3,'c':1} by value ascending (list of tuples).
# d = {'b':2,'a':3,'c':1}
# sorted_items = sorted(d.items(), key=lambda x: x[1])
# print(sorted_items)





























