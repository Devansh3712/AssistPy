'''
Module for top international
news of the day
'''

#Importing Modules
try:

    import requests
    import json
    import time

except:

    print('News module not setup')
    exit()

#Class for getting news
class News:

    def __init__(self, country):
        self.country = country
        #API key for accessing data
        self.api_key = "840d0df8a52e41bf809f4f9826041584"
        #URL for getting the news
        self.url     = f"https://newsapi.org/v2/top-headlines?country={self.country}&apiKey={self.api_key}"

    def get_news(self):

        url = self.url

        try:
            #Get response from the site
            response = requests.get(url)
        
        except:
            return "Unable to fetch data"

        news   = json.loads(response.text)
        result = []

        for i in news['articles']:
            #Add data to a list
            result.append(i['title'])

        return result

'''
AssistPy
Devansh Singh, 2021
'''