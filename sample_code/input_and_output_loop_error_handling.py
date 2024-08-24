# Error handling in python 

try:
	#result = 10/0
	with open('test1.txt', 'r') as f:
		print(f.read())
except FileNotFoundError as e:
	print(e)
except:
	print("You can't devide with 0!")
