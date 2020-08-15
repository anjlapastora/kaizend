import random

from IPython import embed

from time import sleep 

BASE_URL = "http://sample-target-bucket-with-html-pages.s3-website-ap-southeast-1.amazonaws.com"


PAGES = ["1.html",
         "2.html",
         "3.html",
         "4.html",
         "5.html"]

def delay(seconds):
    print(f"Sleeping for {seconds} seconds")
    sleep(seconds)

def get_random_number():
    return random.randint(1,5)

def main():
    for page in PAGES:
        delay(get_random_number())
        print(BASE_URL + "/" + page)


if  __name__ ==  "__main__":
    main()