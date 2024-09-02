str1= input("Enter the string: ")
empty_str = ""

for char in str1:
    if char.isalnum() or char.isspace():
        empty_str +=char

print("output:",empty_str)