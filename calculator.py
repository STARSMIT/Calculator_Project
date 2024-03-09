import math
print("YOU ARE USING STAR CALCULATOR")

def operations_selection():
    operations=""
    while operations!="+" and operations!="-" and operations!="*" and operations!="/" and operations!="sqrt" and operations!="quit" :
        operations = input('''Enter "+" to add numbers
Enter "-" to subtract numbers
Enter "*" to multiply numbers
Enter "/" to divide numbers
Enter "sqrt" to get square root of the number
Enter "quit" to end the program
:  ''')
    return operations

def addition():
    total_Sum=0
    number_inputs = input("Add enter the numbers you would like to add (like 1+5+..): ")
    number_list = number_inputs.split("+")
    i = 0
    while i<len(number_list):
        if number_list[i]=="":
            total_Sum+=0
        else:
            total_Sum+=float(number_list[i])
        i+=1
    return f"Result: {total_Sum}"


def subtraction():
    number_inputs = input("Add enter the numbers you would like to subtract (like 1-5-..): ")
    number_list = number_inputs.split("-")
    output = float(number_list[0])
    i = 1
    while i<len(number_list):
        if number_list[i]=="":
            output-=0
        else:
            output-=float(number_list[i])
        i+=1
    return f"Result: {output}"

def multiplication():
    total= 1
    number_inputs = input("Add enter the numbers you would like to add (like 1*5*..): ")
    number_list = number_inputs.split("*")
    i = 0
    while i<len(number_list):
        if number_list[i]=="":
            total*=1
        else:
            total*=float(number_list[i])
        i+=1
    return f"Result: {total}"

def division():
    try:
        dividend = float(input("Enter the dividend: "))
        divisor = float(input("Enter the divisor: "))
    except Exception:
        return "Invalid input"
    if divisor == 0:
        return "Error: Cannot divide by zero."
    result = dividend / divisor
    return f"Result: {result}"

def square_root():
    num = float(input("Enter the number whose square root is to be found: "))
    if num < 0:
        return "Error: Cannot find square root of a negative number."
    return f"Result: {math.sqrt(num)}"

def main():
    selection=""
    if_more=""
    while selection!="quit" and if_more!="n":
        selection = operations_selection()
        if selection=="+":
            print(addition())
        elif selection=="-":
            print(subtraction())
        elif selection=="*":
            print(multiplication())
        elif selection=="/":
            print(division())
        elif selection=="sqrt":
            print(square_root())
        if_more = input("Do you want to do more calculations (y/n): ")
    print("THANK YOU FOR USING STAR CALCULATOR")
main()

    
        