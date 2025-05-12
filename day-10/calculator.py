def add(n1,n2):
    return n1+n2

def mul(n1,n2):
    return n1*n2

def sub(n1,n2):
    return n1-n2

def div(n1,n2):
    return n1/n2

operations = {
    "+": add,"-":sub,"*":mul,"/":div
}


def calculator():
    should_accumulate = True
    number1 = float(input("What is the first number"))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("pick the operations")

        number2 = float(input("enter the second number"))
        answer = operations[operation_symbol](number1, number2)

        print(f"{number1} {operation_symbol} {number2} = {answer}")
        choice = input(f"type 'y' to continue with : {answer} or type 'n' to start with new number ").lower()

        if choice == 'y':
            number1 = answer
        else:
            should_accumulate = False
            calculator()

calculator()




