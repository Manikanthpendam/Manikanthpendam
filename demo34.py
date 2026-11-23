a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = int(input("enter your choice : "))

if choice == 1:
	print("Result : ",a+b)
elif choice == 2:
	print("Result : ",a-b)
elif choice == 3:
	print("Result : ",a*b)
elif choice == 4:
	print("Result : ",a/b if b!=0 else "cannot divide by zero")
else:
	print("invalid choice")