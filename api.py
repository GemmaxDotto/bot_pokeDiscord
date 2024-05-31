import random
import requests

# function to extract the links from the sprites to get in another function a random image of the pokemon
def extract_links(value):
    if isinstance(value, dict):
        for subvalue in value.values():
            yield from extract_links(subvalue)
    else:
        yield value
        
class Pokemon:
    def __init__(self, name):
        self.name = name
        self.api_url = f"https://pokeapi.co/api/v2/pokemon/{name}/"

    # method to get the abilities of the pokemon
    def get_abilities(self):
        response = requests.get(self.api_url)
        data = response.json()
        abilities = data["abilities"]
        abilities_list = [ability["ability"]["name"] for ability in abilities]
        return "* " + "\n* ".join(abilities_list)

    # method to get the base experience of the pokemon
    def get_base_experience(self):
        response = requests.get(self.api_url)
        data = response.json()
        return data["base_experience"]


    # method to get the stats of the pokemon
    def get_stats(self):
        response = requests.get(self.api_url)
  
        if response.status_code == 200:
            try:
                data = response.json()
                stats = data["stats"]
                return {stat["stat"]["name"]: stat["base_stat"] for stat in stats}
            except json.decoder.JSONDecodeError:
                data = None
        else:
                data = None
                return data
            
    # method to get the formatted moves of the pokemon in a list
    def format_moves(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            try:
                data = response.json()
                moves = data["moves"]
                formatted_moves = "\n" +"\n".join([f"- {move['move']['name']} ({move['version_group_details'][0]['version_group']['name']})" for move in moves])
                return formatted_moves
            except json.decoder.JSONDecodeError:
                data = None
        else:
                data = None
                return data
        
    # method to get a random image of the pokemon
    def get_random_sprite(self):
        response = requests.get(self.api_url)
        data = response.json()
        sprites = data["sprites"]

        # Estrai tutti i link dai dati dei sprites
        links = list(extract_links(sprites))
        # print(f"All extracted links: {links}")  # Debug print

        # Filtra i link per rimuovere quelli nulli
        links = [link for link in links if link is not None]
        #  print(f"Filtered links: {links}")   # Debug print

        # Seleziona un link a caso
        if links:
            return random.choice(links)
        else:
            return None
    
    # method to format the stats with a list 
    def format_stats(self,stats):
        
        formatted_stats = "\n" +"\n".join([f"- {stat.capitalize()}: {value}" for stat, value in stats.items()])
        return formatted_stats
    
    # method to get the types of the pokemon and their damage relations like strenghts and weaknesses
    def get_types(self):
        response = requests.get(self.api_url)
        data = response.json()
        types = data["types"]
        types_name = [type_info["type"]["name"] for type_info in types]
        types_url = [type_info["type"]["url"] for type_info in types]
        response = requests.get(types_url[0])
        data = response.json()
        damage_relations = data["damage_relations"]
        double_damage_from = "\n".join([type_info["name"] for type_info in damage_relations["double_damage_from"]])
        double_damage_to = "\n".join([type_info["name"] for type_info in damage_relations["double_damage_to"]])
        half_damage_from = "\n".join([type_info["name"] for type_info in damage_relations["half_damage_from"]])
        half_damage_to = "\n".join([type_info["name"] for type_info in damage_relations["half_damage_to"]])
        no_damage_from = "\n".join([type_info["name"] for type_info in damage_relations["no_damage_from"]])
        no_damage_to = "\n".join([type_info["name"] for type_info in damage_relations["no_damage_to"]])
        return f"Types for {self.name}:\n* {types_name[0]}\n* Double damage from:\n{double_damage_from}\n* Double damage to:\n{double_damage_to}\n* Half damage from:\n{half_damage_from}\n* Half damage to:\n{half_damage_to}\n* No damage from:\n{no_damage_from}\n* No damage to:\n{no_damage_to}"

    # method to get the game indices of the pokemon
    """ def get_game_indices(self):
        response = requests.get(self.api_url)
        data = response.json()
        game_indices = data["game_indices"]
        return {index["version"]["name"]: index["game_index"] for index in game_indices} """
    


