list1=input("enter the list of element separately :").split()
list2=input("enter the list of element separately :").split()

min_len = min(len(list1),len(list2))
result = []
for i in range(min_len):
   result.append((list1[i]+list2[i]))

print('final result : ', result)