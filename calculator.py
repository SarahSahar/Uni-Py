def calc(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        return "Error"

while True:
    a = int(input("First number: "))
    op = input("Operator: ")
    b = int(input("Second number: "))
    
    print("Result:", calc(a, op, b))
    
    if input("Continue? (y/n): ").lower() != 'y':
        break