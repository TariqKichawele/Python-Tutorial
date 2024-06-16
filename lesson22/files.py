import os

# r = Read
# a = Append
# w = Write
# x = Create

# Read = error if it doesn't exist

f = open('names.txt')

#Reads the whole file
# print(f.read())

#Reads the first 4 characters
# print(f.read(4))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("name_list.txt")
    print(f.read())
except:
    print('The file does not exist')
finally:
    f.close()


#Append - Creates the file if it does not exist
print('')

f = open('names.txt', 'a')
f.write('\nNeil\n')
f.close()

f = open('names.txt')
print(f.read())
f.close()

# Write (overwrite)

f = open('context.txt', 'w')
f.write('I deleted all of the contents')
f.close()

f = open('context.txt')
print(f.read())
f.close()

#Two ways to create a new file
# Opens a file for writing, creates the file if it does not exist

f = open('name_list.txt', 'w')
f.close()

# Creates the specified file, but returns an error if the file exists
if not os.path.exists('dave.txt'):
    f = open('dave.txt', 'x')
    f.close()

# Delete a file
# avoid an error if it does not exist

if os.path.exists('dave.txt'):
    os.remove('dave.txt')
else:
    print('The file does not exist')

with open('more_names.txt') as f:
    content = f.read()

with open('names.txt', 'w') as f:
    f.write(content)


