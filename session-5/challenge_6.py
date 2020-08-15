import random
import requests
from time import sleep
from IPython import embed
from bs4 import BeautifulSoup
from functools import wraps

BASE_URL = "https://sample-target-bucket-with-html-pages.s3-ap-southeast-1.amazonaws.com"


def delay(seconds):
    print(f"Sleeping for {seconds} seconds")
    sleep(seconds)

def get_random_number():
    return random.randint(1,5)

def extract_html_content(target_url):
    response = requests.get(target_url)
    return response.text

def extract_target_value_from_page(html_string):
        pages = []
        soup = BeautifulSoup(html_string, "html.parser")
        target_href = soup.find_all('a href')
        for a in soup.find_all('a', href=True):
            pages.append(a['href'])
        return pages

def extract_target_value_from_page_id(html_string):
        soup = BeautifulSoup(html_string, "html.parser")
        target = soup.find(id="target")
        div_elements = soup.find('div')
        return div_elements.get_text()
    
def main():
    target_page = BASE_URL + "/group2/index.html"
    html_string = extract_html_content(target_page)
    pages = extract_target_value_from_page(html_string)

    for page in pages:
        delay(get_random_number())
        target_page = BASE_URL + page
        html_string = extract_html_content(target_page)
        html_string = extract_target_value_from_page_id(html_string)
        print(html_string)

if  __name__ ==  "__main__":
    main()