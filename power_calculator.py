num = input("Enter a two-digit number: ")
if len(num) == 2 and num.isdigit():
    a = int(num[0])
    b = int(num[1])
    result1 = a**b
    result2 = b**a
    print(f"{a}^{b} = {result1}")
    print(f"{b}^{a} = {result2}")
else:
    print("Error: Enter a valid two-digit positive number.")
