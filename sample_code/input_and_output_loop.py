sm = 0
ctr = 0
avg = 0
f = open('test.txt', 'r')
data = f.readlines() # To iterate items from the list formed by readlines() function.
f.close()

for i in data:
	sm = sm + int(i[-4:])
	ctr = ctr + 1
	avg = sm / ctr
print(f"Sum of the result is equal to {sm}")
print(f"Average is equal to {avg}")

# False value
# x=' 1' => print(int(x)) => output => 1
# y='01' => print(int(y)) => output => 1
# z='1' => print(int(z)) => output => 1

# split() command, it will put every value as an item in default list.



