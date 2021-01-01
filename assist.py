'''
Main AssistPy Program
'''

#Importing modules
try:
    import packages.conversion as conv
    import packages.wiki as wiki
    import packages.play as playvid

except:
    print('Modules not setup')
    exit()

user_input = conv.Listen()
user_query = user_input.speech_to_content()

query = playvid.Search(user_query)
user_output = playvid.Play(query.get_link())
user_output.play_url()