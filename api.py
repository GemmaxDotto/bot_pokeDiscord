import requests

class Pokemon:
    def __init__(self, name):
        self.name = name
        self.api_url = f"https://pokeapi.co/api/v2/pokemon/{name}/"

    def get_abilities(self):
        response = requests.get(self.api_url)
        data = response.json()
        abilities = data["abilities"]
        abilities_list = [ability["ability"]["name"] for ability in abilities]
        return "* " + "\n* ".join(abilities_list)

    def get_base_experience(self):
        response = requests.get(self.api_url)
        data = response.json()
        return data["base_experience"]



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
        
    def get_image(self):
        response = requests.get(self.api_url)
        try:
            data = response.json()
            url= data["sprites"]["front_default"]
            return url
        except KeyError:
            print("Link 'front_default' non trovato nei dati del Pokémon.")
            
    def format_stats(self,stats):
        formatted_stats = "\n" +"\n".join([f"- {stat.capitalize()}: {value}" for stat, value in stats.items()])
        return formatted_stats
    
    def get_types(self):
        response = requests.get(self.api_url)
        data = response.json()
        types = data["types"]
        return [type_info["type"]["name"] for type_info in types]
    
    def get_game_indices(self):
        response = requests.get(self.api_url)
        data = response.json()
        game_indices = data["game_indices"]
        return {index["version"]["name"]: index["game_index"] for index in game_indices}
    


