name = "Dave"  # global scope
count = 1
# greeting("John")


def another():
    color = "blue"  # local scope
    global count  # fetch the global variable so you can modify it, without global you're making a new variable  # noqa: E501
    count += 1
    print(count)

    def greeting(firstname):
        nonlocal color  # reassigning the variable from the parent
        color = "red"
        print(color)
        print(firstname)

    greeting("Dave")


another()
