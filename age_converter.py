from datetime import datetime

birth_year = int(input("Enter your birth year: "))
current_year = datetime.now().year

age = current_year - birth_year
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"Age: {age} years")
print(f"Days: {days:,}")
print(f"Hours: {hours:,}")
print(f"Minutes: {minutes:,}")
print(f"Seconds: {seconds:,}")
