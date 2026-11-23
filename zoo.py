age = int(input("enter visitor age:"))
if age <= 5:
	print("ticket price : free")
elif age >=5 and age <=12:
	print("ticket price :100")	
elif age >=13 and age <=59:
	print("ticket price :200 ")
elif age >= 60:
	print("ticket price : 120")
