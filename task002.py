R1 = input("Enter the first string :")
R2 = input("Enter the second string: ")

middle_index = len(R1)//2

X3=R1[:middle_index]+R2+R1[middle_index:]

print("output",X3)