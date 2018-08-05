# Write your solution for 1.4 here!

def is_prime(num):
	for i in range(2,num):
			if num % i == 0:
				return False
	return True

if(is_prime(5191)):
	print("Prime number :)")
else:
	print("Not a prime number :(")
	