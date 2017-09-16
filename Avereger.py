
import requests


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

# wrapper 1 : Site :https://in.bookmyshow.com/movies/nowshowing (Book my show)


 #   Dummy Link 1

url1 ="https://in.bookmyshow.com/mumbai/movies/lucknow-central/ET00050941"
page = requests.get(url1, verify=False)
htmlfile=page.content
soup = BeautifulSoup(htmlfile, "html.parser")
for link in soup.findAll("div", { "class" : "user-rating" }):
    for k in link.findAll("span", { "class" : "__rating" }):
        for j in k.findAll("ul", {"class": "rating-stars"}):
            l = j.get('data-value')
            print (l)




            #   Dummy Link 1
        # wrapper 1 : Site : (http://www.nowrunning.com/)
url2 = "http://www.nowrunning.com/movie/20570/bollywood.hindi/lucknow-central/9010/review/"

page = requests.get(url2, verify=False)
htmlfile = page.content

soup = BeautifulSoup(htmlfile, "html.parser")
for link in soup.findAll("div", {"class": "AudienceRatingContainer"}):
    #print(link)
    for k in link.findAll("div", {"class": "img-square themeBg"}):
        #print(k)
        for j in k.findAll("span", {"id": "ctl00_ContentPlaceHolderMainContent_RatingSummary1_UserRating"}):
            print(j.contents[0])


#<ul class="rating-stars" data-value="3.8">





# wrapper 3 : Site :https://in.bookmyshow.com/movies/nowshowing (Book my show)


 #   Dummy Link 1

url3 ="http://timesofindia.indiatimes.com/entertainment/hindi/movie-reviews/rabbi/movie-review/60710654.cms"
page = requests.get(url3, verify=False)
htmlfile=page.content
soup = BeautifulSoup(htmlfile, "html.parser")
#print(soup)
for link in soup.findAll("div", { "class" : "flmcasting" }):
    #print(link)
    for k in link.findAll("span", { "class" : "ratingMovie" }):
        print (k.contents[0].split("/")[0])





url4="http://www.koimoi.com/reviews/lucknow-central-movie-review-outstanding-script/"

page = requests.get(url4, verify=False)
htmlfile = page.content

soup = BeautifulSoup(htmlfile, "html.parser")
for link in soup.findAll("div", {"class": "td-post-content"}):
    #print(link)
    for k in link.findAll("p"):
        if(k.contents[0].find("rating")==1):
            print(k)
        #print(k)






r = requests.get("http://rcthanegreencity.com/aasdkasckonvsbgiubsivbrandom1321234amscfpij")
r.status_code
print("check for 404")
print (r)
print("  ")
