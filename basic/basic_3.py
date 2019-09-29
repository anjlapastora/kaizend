# Challenge - Functions Exercise

# Create a function named tripleprint that takes a string as a parameter
# and prints that string 3 times in a row.
# So if I passed in the string "hello",
# it would print "hellohellohello"

param1 = input("Enter string: ")

def tripleprint(param1):
    print(param1 * 3)

tripleprint(param1)
