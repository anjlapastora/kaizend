from time import sleep 
import random

for i in range(0, 5):
    s = random.randint(0, 5)
    print(i)
    print("Sleeping for {0} seconds".format(s))
    sleep(s)