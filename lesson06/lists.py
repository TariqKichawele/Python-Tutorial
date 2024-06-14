users = ['TOP G', 'TOP Z', 'TOP E']

data = [ 'TOP Z', 25, True ]

print("Dave" in users)

print(users[0])
print(users[-2])

print(users.index('TOP Z'))

print(users[0:2])
print(users[1:])

print(len(data))

users.append('TOP R')
print(users)

users += ['Jason']
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'TOP T')
print(users)

users[2:2] = ["Eddie", "Alex"]
print(users)

users[1:3] = ['Robert', 'TOP H']
print(users)

users.remove('TOP R')
print(users)

print(users.pop())
print(users)

del users[1]
print(users)

# Del Data
data.clear()
print(data)

users[1:2] = ['dave']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [1, 5, 6, 734, 54]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))

# making copy of nums list
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(nums)
print(mynums)
print(mycopy)

print(type(nums))

mylist = list([ 1, "Neul", True])
print(mylist)

# Tuples

mytuple = tuple(('Dave', 45, True))
anothertuple = (3,46,64,43)

print(mytuple)
print(type(mytuple))

#Packing a tuple
newList = list(mytuple)
newList.append('TOP T')
newTupple = tuple(newList)
print(newTupple)

(one, two, *jey) = anothertuple
print(one)
print(two)
print(jey)

print(anothertuple.count(46))