# Description: This file contains the class Pokemon that is used to get the information of a pokemon from the pokeapi.co API
import random
import requests

# function to extract the links from the sprites to get in another function a random image of the pokemon
def extract_links(value): 
    if isinstance(value, dict): # If the value is a dictionary, extract links from its values
        for subvalue in value.values(): # For each value in the dictionary
            yield from extract_links(subvalue) # Recursively extract links from the value
    else:
        yield value # If the value is not a dictionary, return it as a link
        
class Pokemon:
    def __init__(self, name):
        self.name = name
        self.api_url = f"https://pokeapi.co/api/v2/pokemon/{name}/"

    # method to get the abilities of the pokemon
    def get_abilities(self):
        response = requests.get(self.api_url) # Send a GET request to the API
        if response.status_code == 200: # If the request was successful
            try:
                data = response.json()
                # print(data)
                abilities = data["abilities"]
                abilities_list = [ability["ability"]["name"] for ability in abilities] # Extract the names of the abilities
                return "\n* " + "\n* ".join(abilities_list)
            except json.decoder.JSONDecodeError: # If the response is not JSON
                data = None
        else:                           # If the request was not successful
            data = None
            return data

    # method to get the base experience of the pokemon
    def get_base_experience(self):
        response = requests.get(self.api_url) # Send a GET request to the API
        if response.status_code == 200: # If the request was successful
            try:
                data = response.json()
                # print(data)
                return data["base_experience"]
            except json.decoder.JSONDecodeError: # If the response is not JSON
                data = None
        else:                          # If the request was not successful
            data = None
            return data


    # method to get the stats of the pokemon
    def get_stats(self):
        response = requests.get(self.api_url) # Send a GET request to the API
  
        if response.status_code == 200: # If the request was successful
            try:
                data = response.json()
                # print(data)
                stats = data["stats"]
                return {stat["stat"]["name"]: stat["base_stat"] for stat in stats} # Extract the stats
            except json.decoder.JSONDecodeError: # If the response is not JSON
                data = None
        else:                         # If the request was not successful
                data = None
                return data
            
    # method to get the formatted moves of the pokemon in a list
    def format_moves(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            try:
                data = response.json()
                moves = data["moves"]
                grouped_moves = {}

                for move in moves:
                    version_groups = move['version_group_details']
                    for version_group in version_groups:
                        group_name = version_group['version_group']['name']
                        move_name = move['move']['name']
                        if group_name not in grouped_moves:
                            grouped_moves[group_name] = set()  # Use a set to avoid duplicate moves
                        grouped_moves[group_name].add(move_name)

                formatted_moves = "\n".join([f"Gruppo {group_name}:\n- {', '.join(moves)}" for group_name, moves in grouped_moves.items()])
                return formatted_moves
            except json.decoder.JSONDecodeError:
                return "Errore nella decodifica della risposta JSON"
        else:
            return "Errore nella richiesta API"
        
    # method to get a random image of the pokemon
    def get_random_sprite(self):
        response = requests.get(self.api_url)
        if response.status_code == 200: # If the request was successful
            try:
                data = response.json()
                # print(data)
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
            except json.decoder.JSONDecodeError: # If the response is not JSON
                data = None
        else:                       # If the request was not successful
            data = None
            return data
    
    # method to format the stats with a list 
    def format_stats(self,stats):
        
        formatted_stats = "\n" +"\n".join([f"- {stat.capitalize()}: {value}" for stat, value in stats.items()]) # Extract the formatted stats
        return formatted_stats
    
    
    # method to get the types of the pokemon and their damage relations like strenghts and weaknesses
    def get_types(self):
        response = requests.get(self.api_url)
        if response.status_code == 200: # If the request was successful
            try: 
                data = response.json()
                # print(data)
                types = data["types"] 
                types_name = "\n".join([type_info["type"]["name"] for type_info in types]) # Extract the name of types
                types_url = [type_info["type"]["url"] for type_info in types] # Extract the urls of the types
                response = requests.get(types_url[0])
                data = response.json()
                damage_relations = data["damage_relations"] # Extract the damage relations
                double_damage_from = "\n".join([type_info["name"] for type_info in damage_relations["double_damage_from"]]) # Extract the double damage from
                double_damage_to = "\n".join([type_info["name"] for type_info in damage_relations["double_damage_to"]]) # Extract the double damage to
                half_damage_from = "\n".join([type_info["name"] for type_info in damage_relations["half_damage_from"]]) # Extract the half damage from
                half_damage_to = "\n".join([type_info["name"] for type_info in damage_relations["half_damage_to"]]) # Extract the half damage to
                no_damage_from = "\n".join([type_info["name"] for type_info in damage_relations["no_damage_from"]]) # Extract the no damage from
                no_damage_to = "\n".join([type_info["name"] for type_info in damage_relations["no_damage_to"]]) # Extract the no damage to
                return f"\n* Types for {self.name}:\n {types_name}\n* Double damage from:\n{double_damage_from}\n* Double damage to:\n{double_damage_to}\n* Half damage from:\n{half_damage_from}\n* Half damage to:\n{half_damage_to}\n* No damage from:\n{no_damage_from}\n* No damage to:\n{no_damage_to}"
            except json.decoder.JSONDecodeError: # If the response is not JSON
                data = None 
        else:                      # If the request was not successful
            data = None
            return data
        
    # method to get the game indices of the pokemon
    """ def get_game_indices(self):
        response = requests.get(self.api_url)
        data = response.json()
        game_indices = data["game_indices"]
        return {index["version"]["name"]: index["game_index"] for index in game_indices} """
    


