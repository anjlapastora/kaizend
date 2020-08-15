from time import sleep
from functools import wraps


def delay(seconds):
    def inner_function(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[START]")
            sleep(seconds)
            output = func(*args, **kwargs)
            print(f"[END]")
            return output
        return wrapper
    return inner_function


@delay(seconds=5)
def main(word):
    print(word)


if __name__ == '__main__':
    main("hello")