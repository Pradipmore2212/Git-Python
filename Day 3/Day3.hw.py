# Check Data Type and if it's a number
user_input = input("Enter a value: ")
print("Data Type:", type(user_input))


# Check if it's a number
try:
    float(user_input)
    print("It's a number.")
except ValueError:
    print("It's NOT a number.")

# detect type of three inputs
#def detect_type(value):
# try:
#    if '.' in a value:
#float(value)
#return "float"
#else:
# int(value) 
#return "integer"
#except Value error:
# return "string"
val1 = input("Enter first value: ")
val2 = input("Enter second value: ")
val3 = input("Enter third value: ")


#print("Value 1 is:", detect_type(val1))
#print("Value 2 is:", detect_type(val2))
#print("Value 3 is:", detect_type(val3))

num1 = input("Enter first number:")
num2 = input("Enter second number:")

print("concatenation:", num1 + num2)
print("integer sum:",int(num1) + int(num2))
print("float sum:",float(num1) + float(num2))

def convert_temperature(celsius: float) -> tuple:
    fahrenheit = (celsius * 9 / 5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin
user_input = float(input("enter temperature in celsius:"))

f, k = convert_temperature(user_input)

print(f"fahrenheit: {f:.2f}")
print(f"kelvin: {k:.2f}")

birth_year = input("enter your birth year:")
birth_year = int(birth_year)
current_year = 2025
age = current_year - birth_year
print(f"your age in {current_year} is: {age}")

def add_numbers(a: float, b: float) -> float:
    return round(a + b, 2)

num1 = float(input("Enter first float: "))
num2 = float(input("Enter second float: "))

result = add_numbers(num1, num2)
print("Rounded Sum:", result)


def calculate_area(length: float, width: float) -> float:
    return length * width

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = calculate_area(length, width)
print("Area of Rectangle:", area)



def get_student_info() -> dict:
    name: str = input("Enter student name: ")
    roll_no: int = int(input("Enter roll number: "))
    marks: float = float(input("Enter marks: "))

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks
    }
    return student

item_name: str = input("Enter item name: ")
quantity: int = int(input("Enter quantity: "))
price: float = float(input("Enter price per item: "))

total = quantity * price

print("\n----- RECEIPT -----")
print(f"Item     : {item_name}")
print(f"Quantity : {quantity}")
print(f"Price    : ₹{price:.2f}")
print(f"Total    : ₹{total:.2f}")





















