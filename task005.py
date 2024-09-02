s1=input("enter a string: ")
subString=input(" enter the sub string: ")

s1_lower=s1.lower()
subString=subString.lower()

result = s1_lower.count(subString)

print("print:",result)