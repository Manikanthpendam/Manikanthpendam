students = {}
while True:
	name = input("enter student name : ")
	marks = int(input("enter marks : "))
	students[name] = marks
	choice = input("Add another student? (yes/no) : ")
	if choice.lower() == "no":
		break
print("\n Student name : ")
for name,marks in students.items():
	print(name,":",marks)