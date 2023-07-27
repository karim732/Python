def my_decorator(func):
    def wrapper():
        print(f'Running {func.__name__}')
        func()
        print("complete")
    return wrapper

@my_decorator
def do_this():
    print('Doing This')

@my_decorator
def do_that():
    print('Doing That')

do_this()
do_that()


# Output:-
# Running do_this                                     
# Doing This
# complete
# Running do_that
# Doing That
# complete