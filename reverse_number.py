num = int(input("Enter a two-digit number: "))

if 10 <= abs(num) <= 99:
    d1 = abs(num) // 10
    d2 = abs(num) % 10
    rev = d2 * 10 + d1

    if num < 0:
        rev = -rev

    print("Reversed number:", rev)
else:
    print("Invalid input!")