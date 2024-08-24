# Using 'with' command we don't need to close file after using it.
# with: saves the need to deal with thefile once you done - no need to close th file.

#with open('test.txt', 'r') as f:
#	print(f.read())

# Reading mode:
# 'r': Open for reading
# 'rb' open for reading binary format.

# Q? When do we need to use the binary format?
# => Any file that isn't a strings, for example .png files or any other non-text files!

# Writing mode:
 # w: OPen for writing. it will create a new file, if it doesn't not exist or truncate the file(make it empty) if it is exits
 # 'wb': OPen for writing in binary format.It behaves like 'w' but writes in binary mode.
 
# Task: Create a code that gets from the user a file to copy and saves it into the same name_back_up.


name = input("Enter a file to copy: ")
new_name = name+"_backup"
with open(name, 'rb') as f:
	data = f.read()
	
print(data)

with open(new_name, 'wb') as f:
	f.write(data)
print(f"finishing to copy to file {new_name}")
	
	
