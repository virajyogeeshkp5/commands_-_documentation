# commands and documentation
# single line command
print("Hello World")

# programmatically accesing docstring
def func():
    """This is a function that does not nothing at all"""
    return
print(func.__doc__)

help(func)

def greet(name, greeting="hello"):
    """print the greeting to the user 'name'
    optional parameter 'greeting' can changed what they are greated with."""
    print("{} {}".format(greeting,name))

def hello():
    """say hello to your friends"""
    print("hello my friends")

def hello(name,language="en"):
    """say hello to a person
    Arguments:
    name:name of the person
    language: in which language"""
    print(greeting[language]+" "+name)
    return 2
