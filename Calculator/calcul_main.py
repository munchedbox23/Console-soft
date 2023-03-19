from calc_art import logo

def clean():
    print("\n"  *50)

def add(a,b):
    return a + b

def vich(a,b):
    return a - b

def umn(a,b):
    return a * b

def chastnoe(a,b):
    return a / b

operation = {
    "+":add,
    "-":vich,
    "*":umn,
    "/":chastnoe
}
    
def calculator():
    print(logo)
    boolen = False
    num1 = float(input("What's the first number?: "))
    for symbols in operation:
        print(symbols)
    
    while not boolen:
        calc_operation = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))
        calculation_function = operation[calc_operation]
        answer = calculation_function(num1,num2)
        print(f"{num1} {calc_operation} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            clear()
            boolen = True
            calculator()

calculator()

