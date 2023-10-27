# built in exceptions: https://www.w3schools.com/python/python_ref_exceptions.asp
class JustNotCoolError(Exception):  # custom exceptions
    pass


x = 2
try:
    raise JustNotCoolError("This just isn't cool, man.")
    # raise Exception("I'm a custom exception!")
    # print(x / 1)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")
except NameError:
    print("NameError means something is probably undefined.")
except ZeroDivisionError:
    print("Please do not divide by zero")
except Exception as error:
    print(error)
else:
    print("No errors!")
finally:  # happens no matter what
    print("I'm going to print with or without an error")

# except: #catches all errors but doesn't give you specific information
#     print("There is an error")
