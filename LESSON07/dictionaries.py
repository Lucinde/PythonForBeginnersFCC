# Dictionaries
# key value pairs

band = {"vocals": "Plant", "guitar": "Page"}

bandConst = dict(vocals="Plant", guitar="Page")  # with constructor

print(band)
print(bandConst)
print(type(band))
print(len(band))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# List all keys
print(band.keys())
# List all values
print(band.values())
# List of key/value pairs as tuples
print(band.items())
# verify if a key exists
print("guitar" in band)
print("triangle" in band)

# change values
band["vocals"] = "Coverdale"  # changes value for the key
band.update({"bass": "JPJ"})  # you can change a value or add a value this way
print(band)

# remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())  # removes last added key value pair and returns it as a tuple
print(band)

# delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

bandConst.clear()  # remove values
print(bandConst)
del bandConst  # delete entire dictionary

# copy dictionaries

# band2 = band  # creates a referency NOT A COPY - in memory it's the same dictionary
# print("Bad copy!")
# print(band2)
# print(band)
# band2["drums"] = "Dave"
# print(band2)
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band2)
print(band)

# or use the dictionary constructor function
band3 = dict(band)
print("Good copy!")
print(band3)

# Nested dictionaries
# the value of a key value pair can be another dictionary
member1 = {"name": "Plant", "instrument": "vocals"}
member2 = {"name": "Page", "instrument": "guitar"}
band = {"member1": member1, "member2": member2}
print(band)
print(band["member1"]["name"])

# Sets
nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# no duplicates allowed in a set
nums = {1, 2, 2, 3}  # doesn't create an error but removes the duplicate
print(nums)

# True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a value is in a set
print(2 in nums)
# but you cannot refer to an element in the set with an index position or a key

# add a new value to a set
nums.add(8)
print(nums)

# add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)
# you can use update with lists, tuples and dictionaries too

# merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

# keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
