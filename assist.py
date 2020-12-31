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

query = wiki.Search(user_query)
user_output = conv.Speak(query.wiki_search())
user_output.text_to_speech()