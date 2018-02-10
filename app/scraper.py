import urllib.request, routes
from bs4 import BeautifulSoup
from translate import Translator
test = open("test.txt", 'w')
def scrape(res):
    tr = Translator(to_lang=res['lang'])
    doc = open("app/templates/resc.html", 'w')
    doc.truncate()
    req = urllib.request.Request(res['url'], headers={'User-Agent': 'Mozilla/5.0'})
    page = urllib.request.urlopen(req)
    html_doc = BeautifulSoup(page, 'lxml')
    for child in html_doc.children:
        test.write(child.string)
    html_doc = html_doc.prettify()
    doc.write(html_doc)
    doc.close()
    test.close()
