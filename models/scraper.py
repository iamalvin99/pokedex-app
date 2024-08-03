import requests
from bs4 import BeautifulSoup

class Scraper():

    def scrape_from_site():
        user_agent = {'User-agent': 'Mozilla/5.0'}
        
        BASE_URL = 'https://pokemon.fandom.com/'
        
        page = requests.get(BASE_URL + 'wiki/List_of_Pok%C3%A9mon', headers=user_agent)
        
        soup = BeautifulSoup(page.content, features='html.parser')
        #Get all tables with class of wikitable
        tables = soup.find_all('table', {"class": "wikitable"})
        #Initialise list for list of pokemons to be appended to later
        listOfPokemon = []
        #Iterate through tables
        for table in tables:
            #Get all elements with tr tag
            trList = table.find_all('tr')[1:]
        
            for row in trList:
                columns = row.find_all('td')
                images = row.find('img')
                
                if images.get('src') is not None:
                    if 'https' in images.get('src'):
                        imageUrl = images.get('src').split('/revision')[0]
                if images.get('data-src') is not None:
                    if 'https' in images.get('data-src'):
                        imageUrl = images.get('data-src').split('/revision')[0]

                #Get every element with href attribute to retrieve links 
                url = columns[2].find('a').get('href')
                #Get type1 and type2 of pokemon, capitalize first letter and strip tab
                type1 = columns[3].text.strip('\n').capitalize()
                type2 = columns[4].text.strip('\n').capitalize()
                #If type1 or type2 has markdown link, strip it and take only the text
                if '[' in columns[3].text.strip('\n'):
                    type1 = columns[3].text.strip('\n').split('[')[:-1][0]
                if '[' in columns[4].text.strip('\n'):
                    type2 = columns[4].text.strip('\n').split('[')[:-1][0]
                #Make a temp list to nest into pokemon list, column[0] is index, column[2] is name, column[3] is type1, column[4] is type2
                listToAdd = [columns[0].text.strip('\n'), columns[2].text.strip('\n'), BASE_URL + url, type1, type2, imageUrl]
                listOfPokemon.append(listToAdd)

        return listOfPokemon