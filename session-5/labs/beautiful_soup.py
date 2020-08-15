from bs4 import BeautifulSoup
from IPython import embed

def generate_html():
	return """
		<html>
		    <head><head/>
		    <body>
		        <div id="target">Hello World<div/>
		        <div>a<div/>
		        <div>b<div/>
		        <div>c<div/>
		        <a href="/a.html">A</a>

		    <body>
		<html>
	"""

def main():
	html_doc = generate_html()
	soup = BeautifulSoup(html_doc, "html.parser")
	# target = soup.find(id="target")
	# div_elements = soup.find_all('div')
	target_href = soup.find_all('href')

	for div_element in target_href:
		print(div_element.get_text())


	embed()

	# for div_element in div_elements:
		# print(div_element.get_text())
	# embed()

	# print(target.get_text())


if __name__ == "__main__":
    main()