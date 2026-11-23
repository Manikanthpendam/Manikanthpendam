unit_price = int(input("Enter price: "))
unit_price = float(unit_price)
print(type(unit_price))
quantity = input("Enter quantity: ")
quantity = int(quantity)
print(type(quantity))
order_value = unit_price*quantity
print(order_value)
print(type(order_value))