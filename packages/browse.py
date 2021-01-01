'''
Module for opening browser and
searching the net
'''

try:
    import os
    import subprocess
    import webbrowser as wb
    import re
    from urllib.parse import quote

except:
    print('Browsing modules not setup')
    exit()

#Class for browsing the internet
class Browse:

    def __init__(self, content = str):
        self.content = content

    def search_internet(self):

        #Check whether the user input is a website or not
        website = re.search("[.]com$", self.content)

        if website:
            wb.open(self.content, new = 2)

        else:
            #If not a website, search google with the user query
            url = "https://google.com/?#q=" + quote(self.content)
            wb.open(url, new = 2)

    def search_system(self):

        #Name of the program to open
        query = self.content.lower()

        try:
            #Open the program if it exists
            os.system(query)

        except:
            return 'Program not found'

'''
Devansh Singh, 2021
GitHub: Devansh3712
'''