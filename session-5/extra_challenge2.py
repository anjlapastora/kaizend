from IPython import embed


def debug_input_and_output(func):
    def wrapper(*args, **kwargs):
        print(f"[INPUT] ARGS: {args}")
        print(f"[INPUT] ARGS: {kwargs}")
        output = func(*args, **kwargs)
        print(f"[OUTPUT] {output}")
        return output
    return wrapper


@debug_input_and_output
def say_something(word):
    print(word)


def main():
    say_something("hello")

if __name__ == "__main__":
    main()
