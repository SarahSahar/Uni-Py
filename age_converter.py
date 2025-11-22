def convert_age(age):
    days = age * 365
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    
    print(f"سن: {age} سال")
    print(f"برحسب روز: {days} روز")
    print(f"برحسب ساعت: {hours} ساعت")
    print(f"برحسب دقیقه: {minutes} دقیقه")
    print(f"برحسب ثانیه: {seconds} ثانیه")

age = int(input("سن خود را وارد کنید: "))
convert_age(age)