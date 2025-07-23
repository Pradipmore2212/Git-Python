num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")



num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("the number is negative")
else:
    print("the number is zero")

age = int(input("enter your age:"))

if age > 18:
    print("user is valid to vote") 
else:
    print("user is not valid to vote")     



a = int(input("enter a first number"))
b = int(input("enter a second number"))

if a>b:
    print("first number is greater")
elif a<b:
    print("second number is greater")
else:
    print("both are equal")        



marks = int(input("enter your marks:"))

if marks>=40:
    print("pass")
else:
    print("fail")


from dev.config import Password,USERNAME,Secret_number

username = int(input("Enter your username: "))
password = int(input("Enter your password: "))

if password == Password and username == USERNAME:
    print("Login successful")
else:
    print("Login unsuccessful")

year = int(input("enter a year"))

if (year %400 == 0): 
 print("leap year")
else:
    print("not a leap year")

age = int(input("enter your age"))

if age <=5 :
    print("ticket free")
elif age <= 12 :
    print("ticket price 50rs")
else:
    print("ticket price 100rs")


character = input("enter a character: ")
if character.isupper():
    print("it is an uppercase character.")
elif character.islower():
    print("it is an lowercase character.") 
elif character.isdigit():
    print("it is a digit ")
else:
    print("it is an special character.")



guess = int(input("guess the number"))
if guess == Secret_number:
    print("guess it right")
else:
    print("guess is wrong")


units = int(input("enter units consumed: "))

if units <=50:
    print("bill is 2rs/unit")
elif units <=150:
    print("bill is 3rs/unit")
else:
    print("bill is 5rs/unit")


price = float(input("enter price:"))
 
Discount_price = (price * 0.10)
print(f"10% Discount = Rs {Discount_price:.2f}")
gst_price = Discount_price * 0.18
print(f"18% GST on discounted price = Rs {gst_price:.2f}")
final_price = (price - Discount_price) + gst_price
print(f"Final Price after adding GST = Rs {final_price:.2f}")



numa =int(input(" Enter First number:"))
numb = int(input("Enter second number:"))
numc =int(input("Enter third number:"))


if (numa > numb) and (numa<numc) or (numa>numc) and (numa<numb):
    print("second largest is:",numa)
elif (numb > numa) and (numb < numc) or (numb <numa and numb> numc):
   print("second largest number is:",numb)
else:
    print("second largest number is:",numc)


weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
else:
    print("Overweight")




marks=int(input("Enter your Marks: "))


if marks>=90:
     print("grade A")
elif marks>=75 :
     print("grade B")

elif marks>=50:
     print("grade C")

else:
    print("fail")



balance = float(input("Enter your account balance: "))
amount = float(input("Enter amount to withdraw: "))
  
if amount<= balance:
    print("Balance is sufficient", balance)
else:
    print("balance is insufficient", balance)


a = int(input("enter side a:"))
b = int(input("enter side b:"))
c = int(input("Enter side c:"))

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
     print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid triangle")




user = input("Enter rock, paper or scissors: ")
computer = input(["rock", "paper", "scissors"])

if user == computer:
   print("It's a tie!")
elif (user == "rock" and computer == "scissors") or  (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
   print("You win!")
else:
   print("You lose!")


age = int(input("Enter your age: "))
time = input("Enter your time: ")

if age <18:
    print("if you are a student and age<=18 20%")
else:
    print("do not have any discount: ")    



color = input("Enter traffic signal color: ")
if color == "green":
    print("Go")
elif color == "red":
    print("Stop")
elif color == "yellow":
    print("Wait")
else:
    print("Invalid color")




 







