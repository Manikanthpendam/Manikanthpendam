a = [10,20,30,40,50,60,70,80,90,100]
for value in a :
	if value == 60:
		break
	print(value)

print()

a = [10,20,30,40,50,60,70,80,90,100]
for value in a:
	if value == 40:
		continue
	print(value)

print()

a = [10,20,30,40,50,60,70,80,90,100]
b = [20,40,60]
for value in a:
	if value in b:
		continue
	print(value)