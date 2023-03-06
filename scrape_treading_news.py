from GoogleNews import GoogleNews

news = GoogleNews(period='1d')
news.search("Internationa")
result = news.result()

import pandas as pd 
data = pd.DataFrame.from_dict(result)
data = data.drop(columns=["img"]) 
data.head()

for i in result:
    print("Title : ", i["title"])
    print("News : ", i["desc"])
    print("Read Full News : ", i["link"])

#
#
#The GoogleNews API can be used to scrape live news updates and the latest trends from around the world based on any topic. 
#It allows you to retrieve information on any keyword which can be the name of any country, any event or even the name of a person who is trending on Google.
#If you have never used this API before, you can easily install it on your systems using the pip command; pip install googlenews
