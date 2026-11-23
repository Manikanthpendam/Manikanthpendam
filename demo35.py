contacts = {}
while True:
	name = input("enter contact name : ")
	mobile = input("enter mobile number : ")
	
	contacts[name] = mobile

	choice = input("Add another contact? (yes/no) :")
	if choice.lower() != "yes":
		break
print("\n Contact list : ")
for name,mobile in contacts.items() :
	print(name,":",mobile)