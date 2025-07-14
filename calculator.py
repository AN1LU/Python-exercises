# calculator.py
# calculator.py this module performs basic arithmetic operations

def enter_data():
    d1 = input("Enter some the first number: ")
    d2 = input("Enter the second number: ")
    if not d1.isdigit() or not d2.isdigit():
        raise ValueError("Both inputs must be valid integers.")     
    return d1, d2

def add_numbers(d1, d2):
    return int(d1) + int(d2)

def subtract_numbers(d1, d2):
    return int(d1) - int(d2)    

def multiply_numbers(d1, d2):
    return int(d1) * int(d2) 
   
def divide_numbers(d1, d2):
    if int(d2) == 0:
        raise ValueError("Cannot divide by zero.")
    return int(d1) / int(d2)    

def calculator():
    try:
        d1, d2 = enter_data()
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice == '1':
            result = add_numbers(d1, d2)
            operation = "Addition"
        elif choice == '2':
            result = subtract_numbers(d1, d2)
            operation = "Subtraction"
        elif choice == '3':
            result = multiply_numbers(d1, d2)
            operation = "Multiplication"
        elif choice == '4':
            result = divide_numbers(d1, d2)
            operation = "Division"
        else:
            raise ValueError("Invalid choice.")
        
        print(f"{operation} result: {result}")
    
    except ValueError as e:
        print(f"An error occurred: {e}")
        
if __name__ == "__main__":
    calculator()