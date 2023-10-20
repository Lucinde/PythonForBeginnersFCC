person = "Dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

### older versions to do this ###
message = "\n%s has %s coins left." % (
    person,
    coins,
)  # %s, after the % you add the variables you want to use in that place

print(message)

message = "\n{} has {} coins left.".format(
    person, coins
)  # {} in combination with .format

print(message)

message = "\n{1} has {0} coins left.".format(
    coins, person
)  # you can use an index number to define which item to use

print(message)

message = "\n{person} has {coins} coins left.".format(
    person=person, coins=coins
)  # using parameters and defining them

print(message)

# using a dictionary
player = {"person": "Dave", "coins": 3}

message = "\n{person} has {coins} coins left.".format(**player)

print(message)

### --------------------- ###

### f-strings! This is the way. ###

message = f"\n{person} has {coins} coins left."  # start with the f to indicate it's an f-string
print(message)

message = f"\n{person} has {2 * 5} coins left."
print(message)

message = f"\n{person.lower()} has {2 * 5} coins left."  # using a function
print(message)

message = f"\n{player['person']} has {2 * 5} coins left."  # using the dictionary
print(message)

# you can pass formatting options
num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num /4.52:.2%}")


# for more formatting types: https://www.w3schools.com/python/ref_string_format.asp
