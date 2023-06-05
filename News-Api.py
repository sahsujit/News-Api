import requests
import json
query=input("What types of news are you intrested? : ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2023-05-05&sortBy=publishedAt&apiKey=d8f55e7b66b942daa1e6fffd06abb997"
r=requests.get(url)
news=json.loads(r.text)
# print(news,type(news))
for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("-------------------------------------")
  