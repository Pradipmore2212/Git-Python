for num in range(2, 101): 
    is_prime = True          
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:     
            is_prime = False 
            break            
    if is_prime:
        print(num)



num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")


text = input("Enter a string: ")
count = 0
for char in text:
    if char.lower() in "aeiou":
        count += 1
print("Number of vowels:", count)



for i in range(1, 5):
    print("*" * i)



text = input("Enter a string: ")
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print("Reversed:", reversed_text)



numbers = [12, 3, 5, 8, 10, 15, 22, 7, 4, 1]
total = 0
for num in numbers:
    if num % 2 != 0:
        continue
    total += num
print("Sum of even numbers:", total)



a, b = 0, 1
print(a)
print(b)
for _ in range(13):
    c = a + b
    print(c)
    a, b = b, c



while True:
    text = input("Type something (type 'exit' to stop): ")
    if text.lower() == "exit":
        break



num = int(input("Enter a number: "))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")



num = int(input("Enter a number: "))
fact = 1
while num > 1:
    fact *= num
    num -= 1
print("Factorial:", fact)



num = float(input("Enter a number: "))
count = 0
while num >= 1:
    num /= 2
    count += 1
print("Divided", count, "times")



while True:
    password = input("Enter password: ")
    if password == "python123":
        print("Access granted.")
        break
    else:
        print("Wrong password. Try again.")



for i in range(1, 51):
    if i % 3 == 0 and i % 7 == 0:
        break
    print(i)


for i in range(1, 31):
    if i % 4 == 0:
        continue
    print(i)



numbers = [3, -1, 7, -5, 10]
for num in numbers:
    if num < 0:
        pass  # Future feature: handle negative numbers
    else:
        print("Positive number:", num)



balance = 5000
while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    option = input("Choose an option: ")
    if option == "1":
      print("Your balance is ₹", balance)

    elif option == "2":
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print("₹", amount, "deposited.")

    elif option == "3":
        amount = int(input("Enter withdrawal amount: "))
        if amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print("₹", amount, "withdrawn.")

    elif option == "4":
        print("Thank you for using our ATM!")
        break

    else:
        print("Invalid option.")



from dev.config import questions #Import questions (answers hidden from user)


print("Welcome to the Quiz Game!")
print("Type 'quit' anytime to exit.\n")

for q in questions:
    print(q["question"])  

    for option in q["options"]:
        print(option)



    user_input = input("Your answer (a/b/c/d): ").lower()

    if user_input == "quit":
        print("Game exited by user.")
        break

    if user_input == "hint":
        pass

    if user_input == q["answer"]:
        print(" Correct!\n")
    else:
        print(" Wrong! Try again.\n")



for _ in range(5):  
    print("\nChoose a pattern: triangle, square, pyramid")
    choice = input("Enter pattern name (or type 'exit' to quit): ").lower()

    if choice == "exit":
        print("Goodbye!")
        break

    size = int(input("Enter size (must be >= 2): "))

    if size < 2:
        print("Invalid size. Skipping this pattern.")
        continue

    if choice == "triangle":
        for i in range(1, size + 1):
            print("*" * i)

    elif choice == "square":
        for _ in range(size):
            print("*" * size)

    elif choice == "pyramid":
        for i in range(1, size + 1):
            spaces = size - i
            stars = 2 * i - 1
            print(" " * spaces + "*" * stars)

    else:
        print("Invalid pattern name.")



books = ["Python Basics", "C++ Primer", "Java for Beginners", "HTML & CSS", "Data Science 101"]

borrowed_books = []

print("Welcome to the Library System!")
print("Available actions: 'borrow', 'return', 'view', 'exit'\n")

while True:
    action = input("Enter your action: ").strip().lower()

    if action == "exit":
        print("Exiting the system. Thank you!")
        break

    elif action == "view":
        print("\nAvailable books:")
        for book in books:
            print("•", book)
        print()

    elif action == "borrow":
        book_name = input("Enter the name of the book to borrow: ").strip()

        if book_name not in books:
            print("Book not available. Try again.\n")
            continue  

        books.remove(book_name)
        borrowed_books.append(book_name)
        print(f"You borrowed '{book_name}'.\n")

    elif action == "return":
        book_name = input("Enter the name of the book to return: ").strip()

        if book_name not in borrowed_books:
            print("Book was not borrowed from us.\n")
            continue 

        borrowed_books.remove(book_name)
        books.append(book_name)
        print(f"You returned '{book_name}'.\n")

        pass

    else:
        print("Invalid action. Try again.\n")


















