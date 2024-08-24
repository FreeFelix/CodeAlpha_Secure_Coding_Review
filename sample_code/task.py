data = input("PLease enter any filename: ")

try:
	with open(data, 'r') as f:
		print(f.read())
except:
	print("File doesn't exit!!!")
	

	
