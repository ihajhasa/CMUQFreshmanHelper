import urllib
import re

url = "http://www.carrefourqatar.com/default.aspx?langauge=en&country=qa"
f = urllib.urlopen(url)

print f.readline()
