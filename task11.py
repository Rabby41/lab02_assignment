user_input = input("Enter a list numbers separately :")

num_to_list=list(map(int,user_input.split()))
reverse_list = num_to_list[::-1]
print("the final result: ",reverse_list)