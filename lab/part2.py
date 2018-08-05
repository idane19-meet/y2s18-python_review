# Part 2 of the Python Review lab.

def is_prime(num):
	if num != 1:
		for i in range(2,num):
				if num % i == 0:
					return False
		return True
	else:
		return False

def encode(x, y):
	if y >= 1 and y <= 250 and x >= 500 and x <= 1000:
		while not(is_prime(x)):
			x += 1
		while not(is_prime(y)):
			y += 1
		msg = input("Enter msg to encode:")
		return msg * (x * y)
	else:
		print("Invalid input:outside range!")

def decode(coded_message):


x = int(input("Enter a number:"))
y = int(input("Enter another number:"))
encoded_msg = encode(x,y)
decode(encoded_msg)