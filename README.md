# ezproxy-stanzas
Scrape OCLC EZProxy stanzas and save them to local files

# setup
This is a Python script that requires BeatifulSoup4 library.
```
easy_install pip
pip install BeautifulSoup4

git clone https://github.com/yorkulibraries/ezproxy-stanzas.git stanzas
cd stanzas
python stanzas.py
```

All the IncludeFile directives are saved in stanzas.txt. Include stanzas.txt in your ezproxy config to include all stanzas. 


