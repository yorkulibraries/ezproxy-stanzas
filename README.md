# ezproxy-stanzas
Scrape OCLC EZProxy stanzas and save them to local files

# setup
This is a Python 2.7 script that requires BeatifulSoup4 library.
```
easy_install pip
pip install BeautifulSoup4

git clone https://github.com/yorkulibraries/ezproxy-stanzas.git stanzas
cd stanzas
python stanzas.py
```

If you have python2.7 installed in /usr/local/bin/python2.7, then run it as followed
```
/usr/local/bin/python2.7 stanzas.py
```

All the IncludeFile directives are saved in stanzas.txt. Include stanzas.txt in your ezproxy config to include all stanzas. 


