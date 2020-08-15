from bs4 import BeautifulSoup
from IPython import embed

def generate_html():
	return """
		<html>
		    <head><head/>
		    <body>
		        <a href="/a.html">A</a>
		        <a href="/b.html">B</a>
		        <a href="/c.html">C</a>
		    <body>
		<html>
	"""

def main():
	html_doc = generate_html()
	soup = BeautifulSoup(html_doc, "html.parser")
	target_href = soup.find_all('a href')

	for a in soup.find_all('a', href=True):
		print("href:", a['href'], a.get_text())

	embed()


if __name__ == "__main__":
    main()