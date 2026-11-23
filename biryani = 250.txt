biryani = 250
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