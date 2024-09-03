str1 = input("Enter the string: ")

new_str= ""
for char in str1 :
    if not char.isalnum() and not char.isspace():
        new_str += '#'
    else:
        new_str += char

print("output: ",new_str)