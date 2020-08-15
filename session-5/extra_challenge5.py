import random
import requests

from IPython import embed

from time import sleep 
from bs4 import BeautifulSoup


BASE_URL = "http://sample-target-bucket-with-html-pages.s3-website-ap-southeast-1.amazonaws.com"


PAGES = ["group1/1.html",
         "group1/2.html",
         "group1/3.html",
         "group1/4.html",
         "group1/5.html"]

class ScrapingJob(object):
    def __init__(self, name):
        self.name = name
        self.url = "<none>"
        self.seconds = "<none>"
        self.target_url = "<none>"
        self.html_string = "<none>"



    def delay(self, seconds):
        self.seconds = seconds
        print(f"Sleeping for {seconds} seconds")
        sleep(seconds)
        return self


    def get_random_number(self):
        return random.randint(1,5)

    def extract_html_content(self, target_url):
        self.target_url = target_url        
        response = requests.get(self.target_url)
        return response.text

    def extract_target_value_from_page(self, html_string):
        self.html_string = html_string
        soup = BeautifulSoup(self.html_string, "html.parser")
        target = soup.find(id="target")
        self.html_string = target.get_text()
        return self.html_string

    def complete(self):
        print(f"[START] {self.name}")
        print(f"[URL] =  {self.url}")
        print(f"[DELAY] =  {self.delay}")
        print(f"[TARGET_URL] =  {self.target_url}")
        print(f"[HTML STRING] =  {self.html_string}")
        print(f"[END] =  {self.name}")

    

def main():
    for page in PAGES:
        target_page = BASE_URL + "/" + page
        job = ScrapingJob("Job 1")
        a = job.extract_target_value_from_page(job.extract_html_content(target_page)).complete()

    

if  __name__ ==  "__main__":
    main()