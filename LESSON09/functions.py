# functions are all lowercase, underscores to separate a word
def hello_world():
    print("Hello world!")


hello_world()


def sum(num1=0, num2=0):  # you can add default parameter values with ='value'
    if isinstance(num1, int) or isinstance(num2, int):
        return 0
    return num1 + num2


total = sum(1, 2)
print(total)


def multiple_items(
    *args,
):  # if you don't know how many arguments you will recieve you can use *args
    print(args)
    print(type(args))


multiple_items("Dave", "John", "Sara")


def mult_named_items(**kwargs):  # kwargs = keyword arguments
    print(kwargs)
    print(type(kwargs))


mult_named_items(first="Dave", last="Gray")  # creates a dictionary
