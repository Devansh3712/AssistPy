'''
Main AssistPy Program
'''

#Importing modules
try:
    import packages.browse as browser
    import packages.conversion as conv
    import packages.wiki as wiki
    import packages.play as playvid
    import packages.regex as regex
    import data.info as info

except:
    print('Modules not setup')
    exit()

#Ascii Art/ Menus
ascii_art = '''
  ___          _     _  ______      
 / _ \        (_)   | | | ___ \     
/ /_\ \___ ___ _ ___| |_| |_/ /   _ 
|  _  / __/ __| / __| __|  __/ | | |
| | | \__ \__ \ \__ \ |_| |  | |_| |
\_| |_/___/___/_|___/\__\_|   \__, |
                               __/ |
                              |___/ 
'''

options = '''
+---------------+
|Options        |
+---------------+
|SysInfo        |
|Play           |
|Wiki           |
|Browse         |
|Weather        |
|Date & Time    |
+---------------+
'''

#Printing ascii art of program logo
print(ascii_art)

#Welcoming the user
welcome = conv.Speak("Welcome to AssistPy")
welcome.text_to_speech()

#Taking user preference
preference = conv.Speak("Would you prefer to speak or type?")
preference.text_to_speech()

preference_input = input("Enter your preference: ")

#Main loop if preference is type
if preference_input.lower() == "type":

    while True:

        #Print list of available options
        print(options)

        #Taking user option input
        user_input = input("Enter your choice: ")

        if user_input.lower() == "sysinfo":

            sysinfo = info.Info.system_info()
            print(sysinfo)

        elif user_input.lower() == "play":

            vid_name = input("Enter video name: ")
            option   = input("Open in Browser/Desktop: ")

            video    = playvid.Search(vid_name)
            url      = video.get_link()
            player   = playvid.Play(url)

            if option.lower() == "browser":
                player.play_url_browser()

            else:
                player.play_url()

        elif user_input.lower() == "wiki":

            query  = input("Enter your query: ")
            result = wiki.Search(query)
            print(result.wiki_search())

        elif user_input.lower() == "browse":

            query  = input("Enter your query: ")
            result = browser.Browse(query)
            result.search_internet()

        elif user_input.lower() == "weather":

            city   = input("Enter your city name: ")
            result = info.Weather(city)
            print(result.weather_data())

        elif "date" in user_input.lower() or "time" in user_input.lower():

            result = info.TimeDate.current_date_time()
            print(result)

        elif user_input.lower() in ['exit', 'quit']:

            thankyou = conv.Speak("Thank you for using AssistPy")
            thankyou.text_to_speech()
            exit()

        else:

            print("Choose a valid option")

#Main loop if preference is speak
elif preference_input.lower() == "speak":

    while True:

        #Print list of available options
        print(options)

        question = conv.Speak("Speak your choice")
        question.text_to_speech()

        user_input = conv.Listen.speech_to_content()


        if regex.Identify.sysinfo(user_input) == True:

            sysinfo = info.Info.system_info()
            output  = conv.Speak(sysinfo)
            output.text_to_speech()

        elif regex.Identify.play(user_input) == True:

            ask_vid_name = conv.Speak("Speak video name")
            ask_vid_name.text_to_speech()

            vid_name = conv.Listen.speech_to_content()

            ask_vid_pref = conv.Speak("Open in browser or desktop")
            ask_vid_pref.text_to_speech()

            vid_pref = conv.Listen.speech_to_content()

            video    = playvid.Search(vid_name)
            url      = video.get_link()
            player   = playvid.Play(url)

            if regex.Identify.browse(vid_pref) == True:
                player.play_url_browser()

            else:
                player.play_url()

        elif regex.Identify.wiki(user_input) == True:

            ask_query = conv.Speak("Speak your query")
            ask_query.text_to_speech()

            query  = conv.Listen.speech_to_content()
            result = wiki.Search(query)

            output = conv.Speak(result)
            output.text_to_speech()

        elif regex.Identify.browse(user_input) == True:

            ask_query = conv.Speak("Speak your query")
            ask_query.text_to_speech()

            query  = conv.Listen.speech_to_content()
            result = browser.Browse(query)

        elif regex.Identify.weather(user_input) == True:

            ask_city = conv.Speak("Speak city name")
            ask_city.text_to_speech()

            city   = conv.Listen.speech_to_content()
            result = info.Weather(city)

            output = conv.Speak(result)
            output.text_to_speech()

        elif regex.Identify.timedate(user_input) == True:

            result = info.TimeDate.current_date_time()
            output = conv.Speak(result)
            output.text_to_speech()

        elif regex.Identify.exit(user_input) == True:

            thankyou = conv.Speak("Thank you for using AssistPy")
            thankyou.text_to_speech()
            exit()

        else:

            valid = conv.Speak("Choose a valid option")
            valid.text_to_speech()