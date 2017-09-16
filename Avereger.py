import urllib.request
import requests
import urllib3





from bs4 import BeautifulSoup




urls = ["http://rcthanegreencity.com/"]


i = 0
metac=0
deadlink =0
activelink =0
atags =0
badattribute =0
alttags=0
imgtags =0
goodattribute =0
goodattributep =0
badattributep =0
alttagsp =0
ptags =0

#urllib3.request.urlopen("https://in.bookmyshow.com/mumbai/movies/lucknow-central/ET00050941")


#first Check if the  link is Valid

# wrapper 1 : Site :https://in.bookmyshow.com/movies/nowshowing (Book my show


 #   Dummy Link 1
url2="https://in.bookmyshow.com/mumbai/movies/ba-pass-2/ET00061579#trailer"
url1 ="https://in.bookmyshow.com/mumbai/movies/lucknow-central/ET00050941"
page = requests.get(url2, verify=False)
htmlfile=page.content
soup = BeautifulSoup(htmlfile, "html.parser")
for link in soup.findAll("div", { "class" : "user-rating" }):
    for k in link.findAll("span", { "class" : "__rating" }):
        for j in k.findAll("ul", {"class": "rating-stars"}):
            l = j.get('data-value')
            print (l)







#<ul class="rating-stars" data-value="3.8">





#htmlfile = urllib.request.urlopen(url1)

#soup = BeautifulSoup(htmlfile, "html.parser")







while i < len(urls):
    htmlfile = urllib.request.urlopen(urls[i])


    soup = BeautifulSoup(htmlfile,"html.parser")
    for link in soup.findAll('meta'):
        k= link.get('name')
        #print k
        if(k!='None'):
         if(k=='keywords'):
            metac += 1
         if (k == 'description'):
             metac += 1
        if (k == 'viewport'):
            print('view port present for responsiveness')
            metac += 1
        if (k == 'author'):
            metac += 1

    htmltext = htmlfile.read()
    # print htmltext
    i += 1
    print ("The Meta Count is " )
    print  (metac)

i = 0
while i < len(urls):
    htmlfile = urllib.request.urlopen(urls[i])

    soup = BeautifulSoup(htmlfile, "html.parser")
    for link in soup.findAll('a'):
        atags  += 1
        k= link.get('href')

        #print k
        if(k=='None'):
            deadlink += 1
        if(k=='#'):
            deadlink += 1
        if (k):
            activelink += 1

    htmltext = htmlfile.read()
    # print htmltext
    i += 1
    print ("Dead Link are ")
    print (deadlink)
    print ("Active Link are Link are ")
    print (activelink)
    print("total anchor tags are")
   # print (tags)
    print("  ")
tpresent =0



r = requests.get("http://rcthanegreencity.com/aasdkasckonvsbgiubsivbrandom1321234amscfpij")
r.status_code
print("check for 404")
print (r)
print("  ")
