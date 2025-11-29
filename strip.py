def clean_edges(text):
    blanks = [' ', '\t', '\n', '\r']

    left = 0
    for i in range(len(text)):
        if text[i] not in blanks:
            left = i
            break
    else:
        return ""

    right = len(text) - 1
    for i in range(len(text) - 1, -1, -1):
        if text[i] not in blanks:
            right = i
            break

    return text[left:right+1]


user_input = input("Enter your string: ")
result = clean_edges(user_input)
print("Output without extra spaces:", result)