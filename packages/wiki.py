'''
Module for returning search results
using wikipedia API
'''

#Importing modules
try:
    import wikipedia
except:
    print('Wikipedia module not setup')
    exit()

class Search:

    def __init__(self, content):
        self.content = content

    def wiki_search(self):
        result = wikipedia.summary(self.content, sentences = 2)
        return result

'''
Devansh Singh, 2021
GitHub: Devansh3712
'''