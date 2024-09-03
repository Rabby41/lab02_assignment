user_input = input ("input :")
list1 = list(map(int, user_input.split()))

unique_list = []

for item in list1:
    if item not in unique_list:
        unique_list.append(item)

print("List after removing duplicates:", unique_list)
