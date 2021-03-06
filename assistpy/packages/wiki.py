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

#Class for searching wikipedia for user query
class Search:

    def __init__(self, content = str):
        self.content = content

    def wiki_search(self):

        try:
            result = wikipedia.summary(self.content, sentences = 2)
            return result

        except:
            return 'No results found'

'''
AssistPy
Devansh Singh, 2021
'''