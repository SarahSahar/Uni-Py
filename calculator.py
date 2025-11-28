def calc(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    elif op == '^':
        return a ** b
    else:
        return "your operation is false!!!"

while True:
    a = int(input("First number: "))
    op = input("Operator: ")
    b = int(input("Second number: "))
    
    result = calc(a, op, b)
    print("Result:", result)

    if input("Continue? (y/n): ").lower() != 'y':
        break
