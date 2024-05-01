# Should move this to other locations
# https://www.youtube.com/watch?v=FsAPt_9Bf3U&t=924s&ab_channel=CoreySchafer
from typing import Any


def outer_function(msg):
    message = msg

    def inner_function():
        print(message)
    # return inner_function => return a function without excecute the function
    # return inner_function() => excecute and return a funciton
    return inner_function

def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print(f'wraaper executed this before {original_function.__name__} ')
        return original_function(*args,**kwargs)
    return wrapper_function

class Decorator_class(object):

    def __init__(self,original_function) -> None:
        self.original_function = original_function
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(f'call method executed this before {self.original_function.__name__} ')
        return self.original_function(*args,**kwds)
    


def display():
    print('display function ran')

@decorator_function
def display_info(name,age):
    print(f"display_info rang with arguemnts ({name},{age})")

decorated_display = decorator_function(display)

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

hi_func()
bye_func()


############################### This 2 are equivelent ###############################
# @decorator_function
@Decorator_class
def display():
    print('display function ran')

# display = decorator_function(display)
display()

display_info('John',25)