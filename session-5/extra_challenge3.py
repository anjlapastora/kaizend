from bs4 import BeautifulSoup
from IPython import embed

import json
import urllib3

def generate_html():
    return """
        <html>
          <head></head>
          <body>
            <a href="/a.html">A</a>
            <a href="/b.html">B</a>
            <a href="/c.html">C</a>
            <a href="/d.html">D</a>

            <script>
              var hello = 'yoh';
              alert(hello);
            </script>
          </body>
        </html>
    """

def main():
    html_doc = generate_html()
    soup = BeautifulSoup(html_doc, 'html.parser')

    script_tags = soup.find_all('script')
    
    for i in script_tags:
        a = i.get_text()
        b = a.split(";") 
        for p in b:
            if "var" in p:
                var_val = p.split("=")
                print("hello = ", var_val[1])
    embed()



if __name__ == "__main__":
    main()