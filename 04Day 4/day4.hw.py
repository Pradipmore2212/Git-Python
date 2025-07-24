text = "HelloWorld"
first_five = text[0:5]
print(first_five)


text = "Pythonprogramming"
every_second = text[0::2]
print(every_second)


text = "DataEngineer"
reversed_text = text[::-1]
print(reversed_text)


text = "machinelearning"
slice_learn = text[7:12]
print(slice_learn)


text = "apple apple banana"
replace_text = text.replace("apple", "orange")
print(replace_text)


text = "this is easy, is it not?"
replace_text = text.replace("is", "was", 2)
print(replace_text)

text = "welcome To Python"
upper_text = text.upper()
print(upper_text)

text = "HELLO EVERYONE"
lower_text = text.lower()
print(lower_text)


text1 = "Good"
text2 = "Morning"
result = text1 + " " + text2
print(result)


text1 = "Data"
text2 ="Science"
text3 = "Rocks"
result = text1 + " " +text2 + " " + text3
print(result)


name = "Asutosh"
age = "28"

result = "My name is {} and I am {} years old.".format(name,age)
print(result)


value = 45.6789
formated_value = "{:.2f}".format(value)
print(formated_value)

text = "hello world"
capitalized_text = text.capitalize()
print(capitalized_text)


str1 = "python"
str2 = "PYTHON"

result = str1.casefold() == str2.casefold()
print(result)


text = "Python"
centered_text = text.center(20, '*')
print(centered_text)



text = "Banana"
count_a = text.count("a")
print(count_a)


text = "The theater is near the theme park"
lower_text = text.lower()
count_the = lower_text.count("the")
print(count_the)


filename = "programming.py"
result = filename.endswith(".py")
print(result)


filename = "hello.txt"
result = filename.endswith(".doc")
print(result)


text = "hello world"
upper_text =text.upper()
result = upper_text.replace("HELLO", "HI" )
print(result)


text = "hello World"
last_five = text[-5:]
print(last_five)


















