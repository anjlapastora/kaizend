from contextlib import contextmanager

@contextmanager
def do_something(a):
	print(f"a={a}")
	print("start")
	yield 6
	print("end")

def main():
	with do_something(3) as x:
		print(x)

if __name__ == "__main__":
	main()