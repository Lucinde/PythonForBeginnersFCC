users = ["Dave", "John", "Sara"]

data = ["Dave", 42, True]

emptylist = []

print("Dave" in users)  # check if Dave is in list
print(users[0])  # print first item in list
print(users[-1])  # find last item in list
print(users.index("Sara"))  # find where Sara is in the list
print(users[0:2])  # print until index 2
print(users[1:])  # print everything from value 1
print(users[-3:-1])
print(len(data))

# editing a list
users.append("Elsa")
print(users)

users += [
    "Jason"
]  # make sure you use a list otherwise it'll add each letter as a new item
print(users)

users.extend(["Robert", "Jimmy"])
print(users)

# users.extend(data)
# print(users)

users.insert(0, "Bob")  # add to a specific position
print(users)

users[2:2] = [
    "Eddie",
    "Alex",
]  # begin and end at the same position so it doesn't replace other items
print(users)

users[1:3] = ["Robert", "JPJ"]  # replaces the first and second items
print(users)

users.remove("Bob")
print(users)
print(users.pop())  # deletes item, without a value it deletes last item from list
print(users)
del users[0]
print(users)
# del data #deletes entire list
# print(data)
data.clear()  # removes the items from the list
print(data)

users[1:2] = ["dave"]
users.sort()  # sorts alphabetical but is case-sensitive
print(users)
users.sort(key=str.lower)  # not case-sensitive
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)
# nums.sort(reverse=True)
# print(nums)

# above functions change the list
# the following functions only change the display of the list but not the original list
print(sorted(nums, reverse=True))
print(nums)

# make a copy of the list
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]  # indexrange without numbers takes the entire list

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

# other options with lists
print(type(nums))
mylist = list([1, "Neil", True])  # create a list with a constructor
print(mylist)

# Tuples
mytuple = tuple(("Dave", 42, True))  # tuple with constructor
anothertuple = (1, 4, 2, 8, 2, 2)  # tuple without constructor

print(type(mytuple))
print(type(anothertuple))

# tuples cannot be changed
newlist = list(mytuple)
newlist.append("Neil")
newtuple = tuple(newlist)
print(newtuple)

(one, two, *hey) = anothertuple  # unpacking a tuple
print(one)
print(two)
print(hey)
# hey holds remaining values because of the * before hey,
# this adds the remaining values to the item that's after the *

print(anothertuple.count(2))  # counts how many occurrences of number 2 there are
