value = 1
# while value < 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))

names = ['top x', 'top s', 'top g']
for x in names:
    print(x)

for x in 'top z':
    print(x)

for x in names:
    if x == 'top s':
        continue
    print(x)

print("")

for x in range(4):  
    print(x)

print("")

for x in range(2, 4):
    print(x)

print("")

# for x in range(0, 100, 5):
#     print(x)

actions = ['codes', 'eats', 'sleeps']

for name in names:
    for action in actions:
        print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + '.')