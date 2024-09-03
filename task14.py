user_input = input("Enter a list of strings").split()

blank_list = []

for string in user_input:
    if string:
        blank_list.append(string)

print(blank_list)
