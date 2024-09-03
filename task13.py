user_input = input("Enter a list of numbers separately: ").split()

squared_numbers_loop = []
for num in user_input:
    squared_numbers_loop.append(int(num) ** 2)

    print(squared_numbers_loop)
