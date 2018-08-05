# Part 1 of the Python Review lab.

def hello_world():
	print("Hello World")

def greet_by_name(name):
	print("Hello",name)

def encode(x):
	return x * 3953531

def decode(coded_message):
	print(coded_message / 3953531)
decode(encode("hi"))