n = 200
sm = 0
while n < 501:
	if n % 3 == 0:
		sm = sm + n
	n += 1
print(sm)

print("________________")

sm = 0
chr = ord('a')
while chr < ord('t')+1:
	print(chr)
	sm = sm + chr
	chr = chr +1
print(sm)

print("***********************")
counter = 0
for i in range(10,1001,7):
	print(f"{counter} = {i}")
	counter = counter + 1
	
print("***********************")

counter = 0
for i in range(10,1001,23):
	print(f"{counter} = {i}")
	counter = counter + 1
	
print("**********************")
name = 'Cyber Security'
sm = 0
for i in name:
	sm = sm + ord(i)
print(sm)
	
print("*****************")

n = ord('F')
sm = 0
while n < ord('W')+1:
	sm = sm + n
	n = n + 1
print(sm)

print("*****************8")

n = 50
sm = 0
while n < 151:
	if n % 4 == 0:
		sm = sm + n
	n = n +1
print(sm)

print("____________________")

sm = 0
for i in range(200,501):
	if i % 3 == 0:
		sm = sm + i
print(sm)

print("__________________")

sm = 0
n = 300
while (n < 401):
	sm = sm + n
	n = n + 1
print(sm)

print("__________________")

sm = 0
for i in range(150,251):
	if i % 2 != 0:
		sm = sm + i
print(sm)

print("****************")

counter = 1
for i in range(5,50,5):
	print(f"{counter} = {i}")
	counter = counter + 1
