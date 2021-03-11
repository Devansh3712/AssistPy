'''
Module for playing videos/ audio
from youtube
'''

#Importing modules
try:

    import urllib.request
    import urllib.parse
    import re
    import vlc
    import pafy
    import webbrowser as wb
    from time import sleep

except:

    print('Play module not setup')
    exit()

#Class for searching the youtube video url for the given query 
class Search:

    def __init__(self, content = str):
        self.content = urllib.parse.quote(content)

    def get_link(self):
    
        #Search youtube with the title provided by user
        html   = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + self.content)
        #Get video link using regex
        videos = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        #Final URL for video
        url    = "https://www.youtube.com/watch?v=" + videos[0]

        return url

#Class for playing the youtube video using python-vlc
class Play:

    def __init__(self, url = str):
        self.url = url

    def play_url(self):

        video = pafy.new(self.url)
        #Get best quality available for video
        best  = video.getbest()
        #Initialize VLC Media Player object with video link
        media = vlc.MediaPlayer(best.url)
        media.play()
        sleep(video.length)

    def play_url_browser(self):

        #Open youtube video in a new tab
        wb.open(self.url, new = 2)

'''
AssistPy
Devansh Singh, 2021
'''