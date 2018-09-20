# import libraries
import urllib2
from bs4 import BeautifulSoup

index_page = 'https://help.oclc.org/Library_Management/EZproxy/Database_stanzas'

page = urllib2.urlopen(index_page)

soup = BeautifulSoup(page, 'html.parser')

include_file = open('stanzas.txt', 'w')

links = soup.find_all('a', attrs={'class': 'internal', 'rel': 'internal'})
for l in links:
    url = l.attrs['href']
    if url.startswith('https://help.oclc.org/Library_Management/EZproxy/Database_stanzas/'):
        file_name = url.split('https://help.oclc.org/Library_Management/EZproxy/Database_stanzas/',1)[1]
        stanza_page = urllib2.urlopen(url)
        stanza_soup = BeautifulSoup(stanza_page, 'html.parser')
        pre_tag = stanza_soup.find('pre')
        print file_name
        include_file.write("IncludeFile stanzas/%s\n" % file_name)
        text_file = open(file_name, 'w')
        if not pre_tag is None:
            t = pre_tag.get_text().encode("utf8")
            text_file.write(t)
        text_file.close()

include_file.close()
