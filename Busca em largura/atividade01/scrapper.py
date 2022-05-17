from chrome_driver import get_driver, find_element_by_xpath, wait_element_load
from get_actors import search_actors_by_film
from time import sleep

driver = get_driver()

my_dict_actor = {}
my_dict_film = {}
list_actors = []
list_films = []

#procura os filmes em que o ator participou
def scrapper_actor(actor):    

    driver.get('https://www.themoviedb.org/?language=en-US')
    wait_element_load('inner_search_v4')
    id_input = find_element_by_xpath('//*[@id="inner_search_v4"]')
    id_input.send_keys(f'{actor}')

    wait_element_load('inner_search_form')
    button_confirm = find_element_by_xpath('//*[@id="inner_search_form"]/input[2]')
    button_confirm.click()
    sleep(5)
    wait_element_load('main')
    list_films = find_element_by_xpath('//*[@id="main"]/section/div/div/div[2]/section/div[1]/div/div[1]/div[2]/p[2]').text[9:].split(', ')    
    sleep(5)
    if actor not in list_actors:
        list_actors.append(actor)
        my_dict_actor[actor] = list_films    
    #driver.close()    
    return  list_films

#procura os fimes em que os atores passados como parametro participaram
#passa os nomes dos filmes retornados para o case_test que retorna seus atores
#cria um dicionario de filmes e atores
def create_dict():        
    list_act = ['Tom Hanks', 'Robin Williams']
    for actor in list_act:
        scrapper_actor(actor)
        for i in my_dict_actor[actor]:
            if i not in list_films:
                list_films.append(i)
                str_film = i.replace(' ','+')
                my_dict_film[i] = search_actors_by_film(str_film)
    #print(my_dict_film)
    #for i in my_dict_film.values():
    #    for e in i:
    #        if e != init_actor:
    #            print(e)
                

create_dict()
print(my_dict_actor)
print(my_dict_film)
print(list_actors)
print(list_films)
driver.quit()