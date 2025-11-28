def convert_age(age):
    days = age * 365
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    
    print(f"{hours} hour, {minutes} minute, {seconds} second")

age = int(input("Enter your age: "))
convert_age(age)
