# import requests
# import json 

# def StockNews(query):
#     news_request_link = "https://newsapi.org/v2/everything?q=stocks&from=2021-07-27&sortBy=popularity&apiKey=61006aaf53a8410fa9ae119f41b4eb55"
#     response = requests.get(news_request_link).json()
#     return response 

# importing requests package
import requests    
 
def StockNews():
     
    # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
      "source": "bbc-news",
      "sortBy": "stocks",
      "apiKey": "61006aaf53a8410fa9ae119f41b4eb55"
    }
    main_url = "https://newsapi.org/v2/everything?q=stocks&from=2021-06-27&sortBy=publishedAt&apiKey=61006aaf53a8410fa9ae119f41b4eb55"
 
    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
 
    # getting all articles in a string article
    article = open_bbc_page["articles"]

    # empty list which will
    # contain all trending news
    results = []
     
    for ar in article:
        temp_article_data = {"title": ar["title"],"url": ar["url"], "urlToImage": ar["urlToImage"]}
        # results.append(ar["title"])
        # results.append(ar["url"])
        # results.append(ar["urlToImage"])
        results.append(temp_article_data)
         
    for i in range(len(results)):
         
        # printing all trending news
        print(i + 1, results[i])
 
    # #to read the news out loud for us
    # from win32com.client import Dispatch
    # speak = Dispatch("SAPI.Spvoice")
    # speak.Speak(results)    
    return results            
 
# Driver Code
if __name__ == '__main__':
     
    # function call
  StockNews()