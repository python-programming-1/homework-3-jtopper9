def collatz(num):
    if num % 2 == 0:
        print(num // 2)
        return num // 2
    elif num % 2 == 1:
        print(3 * num + 1)
        return 3 * num + 1


num_provided = input("Please enter an integer: ")
try:
    num = int(num_provided)
    while num != 1:
        num = collatz(num)
        if num == 1:
            break
except ValueError:
    print("The value you entered is not an integer.")