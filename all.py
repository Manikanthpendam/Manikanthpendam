print("1st\tprogram")
age = int(input("enter visitor age:"))
if age <= 5:
	print("ticket price : free")
elif age >=5 and age <=12:
	print("ticket price :100")	
elif age >=13 and age <=59:
	print("ticket price :200 ")
elif age >= 60:
	print("ticket price : 120")



print("2nd program")
a = int(input("Enter number: "))
if a%2==0:
	print("even")
else:
	print("odd \nbiryani program")


biryani = int(input("Enter price: "))
number_of_friends = 3
number_of_plates = 3
subtotal = number_of_plates * biryani
print("subtotal:",subtotal)
gst_rate = 5
gst_amount = (subtotal * gst_rate)/100
print("gst amount:",gst_amount)
total_bill = subtotal + gst_amount
print("total bill:",total_bill)
amount_per_friend = total_bill/number_of_friends
print("amount per friend:",amount_per_friend)




