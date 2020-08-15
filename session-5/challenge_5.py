import random
import requests
from time import sleep
from IPython import embed
from bs4 import BeautifulSoup
from functools import wraps

BASE_URL = 'https://sample-target-bucket-with-html-pages.s3-ap-southeast-1.amazonaws.com'


def extract_html_content(target_url):
    print(f"Downloading HTML content of {target_url}")
    response = requests.get(target_url)
    return response.text


def extract_target_value_from_page(html_string, target=None):
    content = BeautifulSoup(html_string, 'html.parser')

    if target == 'ahref':
        return content.find_all('a', href=True)

    return content.find(id='target')


def main():
    html_content = extract_html_content(f"{BASE_URL}/group2/index.html")
    links = extract_target_value_from_page(html_content, 'ahref')

    for link in links:
        retrieve_content = extract_html_content(f"{BASE_URL}{link['href']}")
        value = extract_target_value_from_page(retrieve_content)
        print(value.get_text())


if __name__ == '__main__':
    main()