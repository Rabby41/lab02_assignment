user_input= input("enter the numbers : ").split()
list1 = list(map(int, user_input))#

find_value = 20
replace_value = 200
for i in range(len(list1)):
    if list1[i] == find_value:
        list1[i] = replace_value
        break

print("Updated list:", list1)
