s = input("Enter a string :")

lowercase_chr_box = ""
uppercase_chr_box = ""

for char in s:
    if char.islower():
        lowercase_chr_box+= char
    elif char.isupper():
        uppercase_chr_box+= char

result = lowercase_chr_box+ uppercase_chr_box
print("output", result)