# closure is a function having access to the scope of its parent
# function after the parent function has returned.
# Good to minimize the global variables you need.


def parent_function(person, coins):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins")

    return play_game


tommy = parent_function(
    "Tommy", 3
)  # parent_function returns a function so Tommy is a function now

jenny = parent_function("Jenny", 5)

tommy()
tommy()

jenny()

tommy()
