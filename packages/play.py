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
    from time import sleep

except:
    print('Play module not setup')
    exit()

#Class for searching the youtube video url for the given query 
class Search:

    def __init__(self, content = str):
        self.content = urllib.parse.quote(content)

    def get_link(self):
    
        html   = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + self.content)
        videos = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        url    = "https://www.youtube.com/watch?v=" + videos[0]
        return url

#Class for playing the youtube video using python-vlc
class Play:

    def __init__(self, url = str):
        self.url = url

    def play_url(self):

        video = pafy.new(self.url)
        best  = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
        sleep(video.length)

'''
Devansh Singh, 2021
GitHub: Devansh3712
'''