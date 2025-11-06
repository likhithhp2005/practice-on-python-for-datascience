# Write a Python program to manage student information using a dictionary.
# The program should allow the user to:
# Add a student by entering their ID and Name.
# Search for a student by ID and display their name if found.
# View all students in the system.
# Exit the program.
s={}
while True:
    print("\n1.Add students to the list.")
    print("2.view the list of students.")
    print("3.exit")

    c=input("enter your choice:")
    
    if c=="1":
        id=input("enter student ID:")
        name=input("Enter student name:")
        s[id]=name
        print("Studend added successfully!!")
    elif c=="2":
        if not s:
             print("no student found!")
        else:
             for id,name in s.items():    
                print(f"Student name is :{name},  Student ID is :{id}")  
    elif c=="3":
         print("you have exited!!")
         break
         
    else:
         print("invalid choice, try again!!!")     




# Write a Python program that randomly selects one student’s name from a list.
# This program can be used by a teacher to randomly choose a student for answering a question or giving a presentation.

import random
students = ["Aarav", "Neha", "Ravi", "Priya", "Karan", "Sneha", "Vikram"]
print("The students are:",students)
if students:
    selected_student = random.choice(students)
    print(f"The selected student is: {selected_student}")
else:
    print("The student list is empty!")




# Create a dictionary where product names are keys and prices are values.
# 1.Use get() to print the price of a product entered by the user.
# 2.Add a new product using setdefault().
# 3.Remove the last inserted product using popitem().
# 4.Show all items using items().
# Create a dictionary of products and prices
products = {"Pen": 10, "Book": 50, "Bag": 500}
name = input("Enter product name: ")
print("Price:", products.get(name, "Product not found"))
new_name = input("\nEnter new product name: ")
new_price = int(input("Enter its price: "))
products.setdefault(new_name, new_price)
products.popitem()
print("\nAll products:")
for p, price in products.items():
    print(p, ":", price)


def calculator():
    print("Welcome to the Python Calculator!")
    print("Operations available: +, -, *, /, %")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /, %): ")

        if op == '+':
            print(f"Result: {num1 + num2}")
        elif op == '-':
            print(f"Result: {num1 - num2}")
        elif op == '*':
            print(f"Result: {num1 * num2}")
        elif op == '/':
            try:
                print(f"Result: {num1 / num2}")
            except ZeroDivisionError:
                print("❌ Error: Division by zero is not allowed.")
        elif op == '%':
            try:
                print(f"Result: {num1 % num2}")
            except ZeroDivisionError:
                print("❌ Error: Modulus by zero is not allowed.")
        else:
            print("❌ Invalid operation! Please choose from +, -, *, /, %.")

    except ValueError:
        print("❌ Error: Please enter valid numbers.")

    finally:
        print("✅ Program finished!")






#Create a Calculator with Multiple Operations and Exception Handling
def calculator():
    print("CALCULATOR!")
    print("Operations available: +, -, *, /, ")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /, ): ")

        if op == '+':
            print(f"Result: {num1 + num2}")
        elif op == '-':
            print(f"Result: {num1 - num2}")
        elif op == '*':
            print(f"Result: {num1 * num2}")
        elif op == '/':
            try:
                print(f"Result: {num1 / num2}")
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid choice!")

    except ValueError:
        print("Error: Please enter only integer!")
    finally:
        print("Program terminated!!")
        calculator()






# . Write a Python program that takes a character as input from the user.
# Find and print the ASCII value of the entered character.
try:
    ch = input("Enter a character: ")
    if len(ch) != 1:
        print("Please enter only a single character.")
    else:
        print(f"The ASCII value of '{ch}' is: {ord(ch)}")

except Exception as e:
    print("An error occurred:", e)

finally:
    print("Program terminated!")







# Create a DataFrame with the following data: Name Age City Ravi 20 Chennai
#  Meena 19 Mumbai John 21 Delhi Print: The shape of the DataFrame The
#  column names The first and last row Task 2: Accessing D
import pandas as pd
data = {
    'Name': ['Ravi', 'Meena', 'John'],
    'Age': [20, 19, 21],
    'City': ['Chennai', 'Mumbai', 'Delhi']
}
df = pd.DataFrame(data)
print("DataFrame:\n", df, "\n")
print("Shape of DataFrame:", df.shape)
print("Column Names:", df.columns.tolist())
print("\nFirst Row:\n", df.head(1))
print("\nLast Row:\n", df.tail(1))
print("\nName Column:\n", df['Name'])
print("\nNames and Cities of students aged > 19:\n", df.loc[df['Age'] > 19, ['Name', 'City']])
df['Marks'] = [85, 90, 75]
print("\nafter adding Marks column:\n", df)
df = df.drop('City', axis=1)
print("\nafter removing City column:\n", df)


