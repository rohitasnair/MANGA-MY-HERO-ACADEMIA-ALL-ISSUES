from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.request
import re
import os




for issue in range(2,295):

	url = "https://w20.readheroacademia.com/manga/boku-no-hero-academia-chapter-" + str(issue)
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13'})
	html_page = urlopen(req, timeout=20).read()
	bs = BeautifulSoup(html_page, 'html.parser')
	images = bs.find_all('img', {'src':re.compile('.jpg')})
	opener = urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	urllib.request.install_opener(opener)
	os.mkdir(str(issue))
	for image in images: 
	    print(image['src']+'\n')
	    fullfilename = os.path.join(str(issue), image['src'].rsplit('/',1)[1]+".jpg")
	    urllib.request.urlretrieve(image['src'], fullfilename)
	    
