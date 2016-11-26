from BeautifulSoup import BeautifulSoup
import urllib2
import re
# Retrieved from http://stackoverflow.com/questions/3075550/how-can-i-get-href-links-from-html-using-python
def getPromotionBooklet():
    #Open HTML Page
    html_page = urllib2.urlopen("http://www.carrefourqatar.com/default.aspx?langauge=en&country=qa")
    response = BeautifulSoup(html_page)

    results = []
    #Retrieve all href links (jpegs, .com, .....)
    for link in response.findAll('a'):
        results.append(link.get('href'))
    #Get all the .aspx folders
    results = filter(lambda x: '.aspx' in x, results)
    promotionHyperMarketExtension = ''
    promotionSuperMarketExtension = ''
    #Get the HyperLeaflet and Market aspx files
    for result in results:
        if 'HyperLeaflets.aspx' in result:
            promotionHyperMarketExtension = result
        if 'Market.aspx' in result:
            promotionSuperMarketExtension = result

    #HyperLeaflet
    #Go to the Market.aspx file
    html_page = urllib2.urlopen("http://www.carrefourqatar.com/" + promotionSuperMarketExtension)
    response = BeautifulSoup(html_page)
    results = []
    #Get all links
    for link in response.findAll('a'):
        results.append(link.get('href'))
    #Get all the aspx files
    results = filter(lambda x: '.aspx' in x, results)
    for result in results:
        #Retrieve the marketLeaflet.aspx
        if 'MarketLeaflet.aspx' in result:
            promotionSuperMarketExtension = result
    
    promotionHMURL = 'http://www.carrefourqatar.com/' + promotionHyperMarketExtension
    promotionSMURL = 'http://www.carrefourqatar.com/' + promotionSuperMarketExtension


    html_page = urllib2.urlopen(promotionHMURL)
    response = BeautifulSoup(html_page)
    results = []
    #Get all the links in the page
    for link in response.findAll('a'):
        results.append(link.get('href'))
    promotionsPDF = ''
    #Get only the .pdf files (usually only one)
    for result in results:
        if '.pdf' in result:
            promotionsPDF = result
            
    #Retrieved from http://stackoverflow.com/questions/24844729/download-pdf-using-urllib
    response = urllib2.urlopen(promotionsPDF)
    f = open("Carrefour_Lulu/carrefourHMPromotions.pdf", 'wb')
    f.write(response.read())
    f.close() #Save pdf with following name


    #Similar to the steps above, but with the MarketLeaflet.aspx file
    html_page = urllib2.urlopen(promotionSMURL)
    response = BeautifulSoup(html_page)
    results = []
    for link in response.findAll('a'):
        results.append(link.get('href'))
    promotionsPDF = ''
    for result in results:
        if '.pdf' in result:
            promotionsPDF = result
    response = urllib2.urlopen(promotionsPDF)
    f = open("Carrefour_Lulu/carrefourSMPromotions.pdf", 'wb')
    f.write(response.read())
    f.close()

