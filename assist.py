'''
Main AssistPy Program
'''

#Importing modules
try:
    import packages.conversion as conv
    import packages.wiki as wiki

except:
    print('Modules not setup')
    exit()

user_input = conv.Listen()
user_query = user_input.speech_to_content()
user_output = conv.Speak(user_query)
user_output.text_to_speech()