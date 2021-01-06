'''
Module for identifying type
of query using user's voice
input
'''

#Importing modules
try:
    import re

except:
    print('Regex module not setup')
    exit()

#Class for identifying type of query
class Identify:

    def sysinfo(query = str):

        #Search for various possible inputs
        result1 = re.search("^sys.info$", query)
        result2 = re.search("^system.information$", query)
        result3 = re.search("^sys.information$", query)
        result4 = re.search("^system.info$", query)
        result5 = re.search("^sys", query)

        #Make a list of results
        results = [
            result1,
            result2,
            result3,
            result4,
            result5
        ]

        for i in results:

            #If any result is true, return True
            if i:
                return True

        return False

    def play(query = str):
        
        #Search for various possible inputs
        result1 = re.search("^play", query)
        result2 = re.search("play$", query)
        result3 = re.search("^play", query)
        result4 = re.search("play$", query)

        #Make list of results
        results = [
            result1,
            result2,
            result3,
            result4
        ]

        for i in results:

            #If any result is true, return True
            if i:
                return True

        return False

    def wiki(query = str):

        #Search for various possible inputs
        result1 = re.search("^wiki", query)
        result2 = re.search("^wikipedia", query)
        result3 = re.search("^wiki", query)
        result4 = re.search("wiki$", query)
        result5 = re.search("wikipedia$", query)

        #Make list of results
        results = [
            result1,
            result2,
            result3,
            result4,
            result5
        ]

        for i in results:

            #If any result is true, return True
            if i:
                return True

        return False

    def browse(query = str):

        #Search for various possible inputs
        result1 = re.search("^browse", query)
        result2 = re.search("^search", query)
        result3 = re.search("browse$", query)
        result4 = re.search("search$", query)

        #Make list of results
        results = [
            result1,
            result2,
            result3,
            result4
        ]

        for i in results:

            #If any result is true, return True
            if i:
                return True

        return False

    def weather(query = str):

        #Search for various possible inputs
        result1 = re.search("^weather", query)
        result2 = re.search("weather$", query)

        #Make list of results
        results = [
            result1,
            result2
        ]

        for i in results:

            #If any result is true, return True
            if i:
                return True

        return False

    def timedate(query = str):

        #Search for various possible inputs
        result1 = re.search("^date", query)
        result2 = re.search("^time", query)
        result3 = re.search("date$", query)
        result4 = re.search("time$", query)
        result5 = re.search("^datetime", query)
        result6 = re.search("^timedate", query)
        result7 = re.search("datetime$", query)
        result8 = re.search("timedate$", query)

        #Make list of results
        results = [
            result1,
            result2,
            result3,
            result4,
            result5,
            result6,
            result7,
            result8
        ]

        for i in results:

            #If any result is true, return True
            if i:
                return True

        return False

    def exit(query = str):

        #Search for various possible inputs
        result1 = re.search("^exit", query)
        result2 = re.search("^quit", query)

        #Make list of results
        results = [
            result1,
            result2
        ]

        for i in results:

            #If any result is true, return True
            if i:
                return True

        return False