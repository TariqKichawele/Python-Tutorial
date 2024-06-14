#Dictionaries

band = {
    "vocals": "Plant",
    "guitar": "Page"
}
band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

print(" ")

#Access items
print(band["vocals"])
print(band.get('guitar'))

print("")

#list all keys
print(band.keys())

#list all values
print(band.values())

print("")

#list of key/value pairs as tuples
print(band.items())

#verify a key exists
print("guitar" in band)
print('trianlge' in band)

print("")

#change values
band['vocals'] = 'Coverdale'
band.update({"bass":'JPG'})
print(band)

print("")

#remove items
print(band.pop("bass"))
print(band)

band['drums'] = 'Boham'
print(band)

print(band.popitem())
print(band)

#delete and clear
band['drums'] = 'Boham'
del band['drums']
print(band)

band2.clear()
print(band2)

del band2

#copy dictionaries

# band2 = band #creates a reference
# print('Bad Copy!')
# print(band2)
# print(band)

# band2['drums'] = 'Dave'
# print(band)

print("")

band2 = band.copy()
band2['drums'] = 'dave'
print('Good Copy!')
print(band)
print(band2)

#or use the dict() constructor function
print("")

band3 = dict(band)
print("Good Copy!")
print(band3)

print("")

#nested dictionaries

member1 = {
    "name" : "Plant",
    "instrument": "guitar"
}

member2 = {
    "name": "Page",
    "instrument":"guitar" 
}

hand = {
    "member1": member1,
    "member2": member2
}

print(hand)
print(hand["member1"]["name"])

#Sets
print("")

nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
print(nums)
print(nums2)
print(type(nums2))
print(len(nums))

#no duplicate allowed
nums = {1, 2, 2, 3}
print(nums)

#True is dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

#check is a value is in a set
print(2 in nums)

#but you cannot refer to an element in the set with an index position ot a key

#add a new element to a set
nums.add(8)
print(nums)

#Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

#you can use update eith lists, tuples and dictionaries, too


#add elements from one set to another
one = { 1, 2, 3}
two = { 5, 6, 7}

mynewset = one.union(two)
print(mynewset)

#keep only duplicates
one = { 1, 2, 3}
two = { 2, 3, 5}

one.intersection_update(two)
print(one)

one = { 1, 2, 3}
two = { 2, 3, 4}

#keep the different
one.symmetric_difference_update(two)
print(one)






