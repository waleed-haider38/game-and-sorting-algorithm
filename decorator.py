




def decorator(func):
    def wrapper():
        print("--------------")
        func()
        print("Hi I am Ben")
    return wrapper


@decorator
def greet():
    print("Hi I am Waleed ")

greet()