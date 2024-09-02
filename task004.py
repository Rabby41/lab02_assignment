s = input("Enter a string : ")
chars_count = 0
digits_count = 0
symbols_count = 0
for char in s:
    if char.isalpha():
        chars_count += 1
    elif char.isdigit():
        digits_count+=1
    else:
        symbols_count+=1

print("total characters :",chars_count)
print("total digits :",digits_count)
print("total symbols :",symbols_count)
