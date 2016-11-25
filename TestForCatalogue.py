import urllib

thisurl = "http://flipbooks.azurewebsites.net/qtr/leaflet/9n0v102030nsamdnndnakqk.pdf"

handle = urllib.urlopen(thisurl)

html_gunk =  handle.read()
