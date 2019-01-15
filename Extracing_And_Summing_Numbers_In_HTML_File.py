from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

total = 0

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = open('File.html')
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
for tag in tags:
	i = (int(tag.contents[0]))
	total = total + i
print('Total of Numbers in your HTML File is:', total)