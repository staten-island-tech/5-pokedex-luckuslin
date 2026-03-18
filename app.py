import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
""" print(data[1]) """

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
# Add a language choice feature and print the pokemons name based on the user input
""" def everypokemon(x):
    if x == "English":
        for index,item in enumerate(data):
            print(index, ":" , item["name"]["english"])
    elif x == "Japanese":
        for index,item in enumerate(data):
            print(index, ":" , item["name"]["japanese"])
    elif x == "Chinese":
        for index,item in enumerate(data):
            print(index, ":" , item["name"]["chinese"])   
    elif x == "French":
        for index,item in enumerate(data):
            print(index, ":" , item["name"]["french"])   
    else :
        for index,item in enumerate(data):
            print(index, ":" , item["name"])  
        print("input specific language you want") 
everypokemon("English") """

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
def pkmontype(type,secondary):
    if type == "Fire" or "fire":
        for index,item in enumerate(data):
            if (item["type"]) == ["Fire",secondary]:
                  print(item["name"]["english"])
                  print(item["type"])
            elif secondary == "0" and item["type"]== ["Fire"]:
                 print(item["name"]["english"])
                 print(item["type"])
    elif type == "Grass" or "grass":
        for index,item in enumerate(data):
            if (item["type"]) == ["Grass",secondary]:
                  print(item["name"]["english"])
                  print(item["type"])
            elif secondary == "0" and item["type"]== ["Grass"]:
                 print(item["name"]["english"])
                 print(item["type"]) 
    elif type == "Normal" or "normal":
        for index,item in enumerate(data):
            if (item["type"]) == ["Normal",secondary]:
                  print(item["name"]["english"])
                  print(item["type"])
            elif secondary == "0" and item["type"]== ["Normal"]:
                 print(item["name"]["english"])
                 print(item["type"])    
    elif type == "Fighting" or "fighting":
        for index,item in enumerate(data):
            if (item["type"]) == ["Fighting",secondary]:
                  print(item["name"]["english"])
                  print(item["type"])
            elif secondary == "0" and item["type"]== ["fighting"]:
                 print(item["name"]["english"])
                 print(item["type"])
    elif type == "Flying" or "flying":
        for index,item in enumerate(data):
            if (item["type"]) == ["Flying",secondary]:
                  print(item["name"]["english"])
                  print(item["type"])
            elif secondary == "0" and item["type"]== ["Flying"]:
                 print(item["name"]["english"])
                 print(item["type"])   
    elif type == "Poison" or "poison":
        for index,item in enumerate(data):
            if (item["type"]) == ["Poison",secondary]:
                  print(item["name"]["english"])
                  print(item["type"])
            elif secondary == "0" and item["type"]== ["Poison"]:
                 print(item["name"]["english"])
                 print(item["type"])  
    elif type == "Ground" or "ground":
        for index,item in enumerate(data):
            if (item["type"]) == ["Ground",secondary]:
                  print(item["name"]["english"])
                  print(item["type"])
            elif secondary == "0" and item["type"]== ["Ground"]:
                 print(item["name"]["english"])
                 print(item["type"])
    elif type == "Rock" or "rock":
        for index,item in enumerate(data):
            if (item["type"]) == ["Rock",secondary]:
                  print(item["name"]["english"])
                  print(item["type"])
            elif secondary == "0" and item["type"]== ["Rock"]:
                 print(item["name"]["english"])
                 print(item["type"])  
    elif type == "Bug" or "bug":
        for index,item in enumerate(data):
            if (item["type"]) == ["Bug",secondary]:
                  print(item["name"]["english"])
                  print(item["type"])
            elif secondary == "0" and item["type"]== ["Bug"]:
                 print(item["name"]["english"])
                 print(item["type"])
    elif type == "Ghost" or "ghost":
        for index,item in enumerate(data):
            if (item["type"]) == ["Ghost",secondary]:
                  print(item["name"]["english"])
                  print(item["type"])
            elif secondary == "0" and item["type"]== ["Ghost"]:
                 print(item["name"]["english"])
                 print(item["type"])
    elif type == "Steel" or "steel":
        for index,item in enumerate(data):
            if (item["type"]) == ["Steel",secondary]:
                  print(item["name"]["english"])
                  print(item["type"])
            elif secondary == "0" and item["type"]== ["Steel"]:
                 print(item["name"]["english"])
                 print(item["type"])
    elif type == "Water" or "water":
        for index,item in enumerate(data):
            if (item["type"]) == ["Water",secondary]:
                  print(item["name"]["english"])
                  print(item["type"])
            elif secondary == "0" and item["type"]== ["Water"]:
                 print(item["name"]["english"])
                 print(item["type"])
    elif type == "Electric" or "electric":
        for index,item in enumerate(data):
            if (item["type"]) == ["Electric",secondary]:
                  print(item["name"]["english"])
                  print(item["type"])
            elif secondary == "0" and item["type"]== ["Electric"]:
                 print(item["name"]["english"])
                 print(item["type"])
    elif type == "Pyschic" or "Pyschic":
        for index,item in enumerate(data):
            if (item["type"]) == ["Pyschic",secondary]:
                  print(item["name"]["english"])
                  print(item["type"])
            elif secondary == "0" and item["type"]== ["Pyschic"]:
                 print(item["name"]["english"])
                 print(item["type"])
    elif type == "Ice" or "Ice":
        for index,item in enumerate(data):
            if (item["type"]) == ["Ice",secondary]:
                  print(item["name"]["english"])
                  print(item["type"])
            elif secondary == "0" and item["type"]== ["Ice"]:
                 print(item["name"]["english"])
                 print(item["type"])
    elif type == "Dragon" or "dragon":
        for index,item in enumerate(data):
            if (item["type"]) == ["Dragon",secondary]:
                  print(item["name"]["english"])
                  print(item["type"])
            elif secondary == "0" and item["type"]== ["Dragon"]:
                 print(item["name"]["english"])
                 print(item["type"])
    elif type == "Dark" or "dark":
        for index,item in enumerate(data):
            if (item["type"]) == ["Dark",secondary]:
                  print(item["name"]["english"])
                  print(item["type"])
            elif secondary == "0" and item["type"]== ["Dark"]:
                 print(item["name"]["english"])
                 print(item["type"])
    elif type == "Fairy" or "fairy":
        for index,item in enumerate(data):
            if (item["type"]) == ["Fairy",secondary]:
                  print(item["name"]["english"])
                  print(item["type"])
            elif secondary == "0" and item["type"]== ["Fairy"]:
                 print(item["name"]["english"])
                 print(item["type"])
    elif type and secondary != pokedex:
         print("Nothing")
pkmontype("Fire", "0")



#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type

