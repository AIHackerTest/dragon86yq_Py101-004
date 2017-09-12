"""
def foo(bar):
    return bar+1

def call_foo_with_arg(foo,arg):
    return foo(arg)

print(call_foo_with_arg(foo,3))
"""

"""
def parent(num):

    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

    try:
        assert num == 10
        return first_child
    except AssertionError:
        return second_child


foo = parent(10)
bar = parent(11)

print(foo)
print(bar)

print(foo())
print(bar())
"""

"""
def my_decorator(some_function):

    def wrapper():
        print("Something is happening before some_function() is called.")
        some_function()
        print("Something is happening after some_function() is called.")
    return wrapper

def just_some_function():
    print("wheel!")

just_some_function = my_decorator(just_some_function)

just_some_function()
"""


def my_decorator(some_function):

    def wrapper():
        num = 10
        if num == 10:
            print("yes")
        else:
            print("no")

        some_function()
        print("Something is happening after some_function() is called.")
    return wrapper

if __name__=="__main__":
    my_decorator()


