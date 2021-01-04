'''
Main AssistPy Program
'''

#Importing modules
try:
    import packages.browse as browser
    import packages.conversion as conv
    import packages.wiki as wiki
    import packages.play as playvid
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