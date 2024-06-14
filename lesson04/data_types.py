import math

first = "Dave"
last = "G"

#find type 
print(type(first))

#concatenation
fullname = first + " " + last
print(fullname)

#casting a number to string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I am a TOP G " + decade + "s."
print(statement)

#escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

#string methods
print(first)
print(first.lower())
print(first.upper())

print(' ')

#build a menu
title = 'menu'.upper()
print(title.center(20, '='))
print('Coffee'.ljust(16, ".") + "$1".rjust(4))
print('Muffin'.ljust(16, ".") + "$2".rjust(4))
print('Cheesecake'.ljust(16, ".") + "$4".rjust(4))

print(" ")

#string index values
print(first[1])
print(first[-1])
print(first[1:-1])

print(" ")

#some methods return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))

print(" ")

#boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

print(" ")

#integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

print (" ")

#float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

print(" ")

comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

print(" ")

#Built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

print(" ")

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

print(" ")

#casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))




