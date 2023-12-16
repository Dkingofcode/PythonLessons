# r = read
# a = Append
# w = write
# x = create

# Read - error if it doesn't exist

import os


f = open("names.txt", "r")
#print(f.read())
#print(f.read(4))

#print(f.readline())
#print(f.readline())

# for line in f:
#     print(line)

# f.close()

# try:
#     f = open("names_list.txt")
#     print(f.read())
# except: 
#     print("The file you want to read doesn't exist")
# finally:
#     f.close()            


# Append - creates the file if it doesn't exist
f = open("names_list.txt", "a")
f.write("Neil\n")
f.close()

f = open("names_list.txt")
print(f.read())
f.close()


# Write (overwrite)
f = open("names_list.txt", "w")
f.write("I deleted all the chracters in this list")
f.close()

f = open("names_list.txt")
print(f.read())
f.close()


# Two ways to create a new file

# Opens a file for writing, creates the file if it doesn't exist
f = open("name_list.txt", "w")
f.close()

# Creates the specified file, but returns an error if the file exists
if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()


# Delete a file

# avoid an error
if os.path.exists("names.txt"):
    os.remove("names.txt")
else:
    print("The file you wish to delete does not exist")    
    
with open("more_names_list.txt") as f:
    content = f.read()
        
with open("names.txt", "w") as f:
    content = f.read()         

















