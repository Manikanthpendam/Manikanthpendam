num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number")
else:
    for value in range(2, num):
        if num % value == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")