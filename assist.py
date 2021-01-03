'''
Main AssistPy Program
'''

#Importing modules
try:
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
welcome = conv.Speak('Welcome to AssistPy')
welcome.text_to_speech()

#Taking user preference
preference = conv.Speak('Would you prefer to speak or type?')
preference.text_to_speech()

preference_input = input()

#Main loop if preference is type
if preference_input.lower() == 'type':

    while True:

        #Print list of available options
        print(options)

        #Taking user option input
        user_input = input("Enter your choice: ")

        if user_input.lower() == "sysinfo":

            sysinfo = info.Info.system_info()
            print(sysinfo)

        else:
            print("Choose a valid option")