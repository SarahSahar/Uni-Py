num = input("Enter two-digit number: ")

a = int(num[0])
b = int(num[1])

result1 = a**b
result2 = b**a

print(f"{a}^{b} = {result1}")
print(f"{b}^{a} = {result2}")