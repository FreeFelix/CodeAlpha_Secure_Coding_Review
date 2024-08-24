# Using split function to access data as an item in list created by readlines 
f = open('test.txt', 'r')
data = f.readlines()

sm = 0
for i in data:
	#sm = sm + int(i.split()[-1]) # split with space betten statements words
	sm = sm + int(i.split(':')[-1]) # split with delimiter ':' in one word string
	
print(sm)

# Using strip function to remove white space by default in the begenning of the string of colllectio

data = ["     ssh", 'http', 'ftp']
for i in data:
	print(i.strip())
	
	
	
