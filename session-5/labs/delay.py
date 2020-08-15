from time import sleep
from functools import wraps

def delay(seconds, repetition=1):
    output = None
    print(seconds)
    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for i in range(repetition):
                print("START")
                output = function(*args, **kwargs)
                sleep(seconds)
                print("END")
            return output
        return wrapper

    return inner_function


@delay(seconds=2, repetition=3)
def say_something(word):
    print(word)

def main():
    say_something("hello")

if __name__ == "__main__":
    main()
