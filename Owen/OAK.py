num = int(input("Guess a number 1 - 100 "))
num2 = int(input("Type a number 1 - 100 "))

print("Your numbers added are: ")
print(num + num2)
print("Your numbers multiplied are: ")
print(num * num2)
if(num == 45):
	print("Ding, Ding, Ding, good job")
elif(num > 45):
	print("Guess is to high")
elif(num < 45):
	print("Guess is too low")
elif(num > 100):
	print("Guess is out of range")
else:
	print("Thats not a number")

