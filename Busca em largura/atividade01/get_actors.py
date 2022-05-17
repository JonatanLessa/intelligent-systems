import requests
import json
#import ast

#lista os atores do filme passado como parametro
def search_actors_by_film(title):
    request = requests.get(f'https://www.omdbapi.com/?t={title}&apikey=ac8589d2')
    my_data = json.loads(request.content)
    #dict_str = request.content.decode()
    #my_data = ast.literal_eval(dict_str)
    list_actors = my_data['Actors'].split(', ')
    #print(list_actors)
    return list_actors

#search_actors_by_film('Forrest+gump')