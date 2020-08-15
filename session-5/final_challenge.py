import random
import requests
from time import sleep
from IPython import embed
from bs4 import BeautifulSoup
from functools import wraps

BASE_URL = 'https://sample-target-bucket-with-html-pages.s3-ap-southeast-1.amazonaws.com/group3/target.html'


def extract_html_content(target_url):
    response = requests.get(target_url)
    return response.text


def extract_target_value_from_page(html_string):
    content = BeautifulSoup(html_string, 'html.parser')
    list_li = content.find_all('li')
    for li_element in list_li:
        li_content_list = li_element.get_text(strip=True).split(' ')
        final_phrase = ""
        for x in li_content_list:
            if x.strip():
                final_phrase = final_phrase + x.strip() + " "
        print(final_phrase)
        print("")


def main():
    print("Downloading HTML content of {}".format(BASE_URL))
    html_content = extract_html_content(BASE_URL)
    extract_target_value_from_page(html_content)


if __name__ == '__main__':
    main()
