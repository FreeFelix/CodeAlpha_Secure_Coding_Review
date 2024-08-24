#data input in linux command #like 'read' commmand in linux

#	data = input("Enter your age: ")

#	print(f"The entered age is: {data}")

#	print(f"In 5 years i will have {int(data) + 5}")

print("****************************")

#Files manipulation using read(), readlines(), readline()

f = open('test.txt', 'r') # 'r' is for reading mode
#print(f.read()) # when we used read() function the result will have the 'str' type
#print(f.readlines()) # when we used readlines() function, the result will have 'list' type
print(f.readline())

print(f.readline())

print(f.readline())


print(f.readline())
f.close()


print

