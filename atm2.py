balance = 5000
while True:
	print("\n1.Check balance")
	print("2.Deposit")
	print("3.Withdraw")
	print("4.Exit")
	choice = int(input("\n Enter your choice : "))
	if choice == 1:
		print("Available balance" ,balance)
	elif choice == 2:
		amount = int(input("Enter deposit amount : "))
		if amount >0:
			balance = balance + amount
			print("Amount deposited successfully ")
			print("Updated balance" ,balance)
		else:
			print("Invalid amount")
	elif choice == 3:
		amount = int(input("Enter withdrawal amount : "))
		if amount >0 and amount <= balance:
			balance -= amount
			print("Withdrawal successful")
			print("Remaining bakance : ",balance)
		else:
			print("invalid amount")
	elif choice == 4:
		print("thank you for using ATM")
		break
	else:
		print("invalid choice! Please try again.")