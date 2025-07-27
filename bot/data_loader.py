import csv
from pathlib import Path
from typing import Dict, List, Tuple

def load_game_data(path: str="data\game_info.csv") -> Tuple[Dict[str,dict], Dict[str,List[str]]]:
    name_lookup: Dict[str, dict] = {} # this will map each character/boss's name and its full row. This is the same as running name_lookup = {}, the way we originally have it set up as is using type hints
    category_lookup: Dict[str, List[str]] = {} # this will map each category field to a list of all names in that category. Same thing as category_lookup = {}

    csv_path = Path(path) # locates the path of the csv file
    with csv_path.open(newline="", encoding="utf-8") as f: # this allows us to open the file and read it. When working with csv files, it's good practice to always add newline = '' as an argument
        reader = csv.DictReader(f) # DictReader reads each line as a dict where the key is the top row in the file and the values are the rest of the rows

        for row in reader:
            name = row["name"].strip() # strip will remove the leading and trailing whitespaces in the string
            category = row["category"].strip().lower() # we want to make sure the dictionary keys are always consistent, so we enforce it by using .lower()
            name_lookup[name.lower()] = row # don't need to do +=, in dictionaries, a simple = will keep adding to the dictionary and won't overwrite anything
            '''
            name_lookup[name.lower()]

            - name_lookup["wylder"]

            name_lookup["wylder"] = row

            - {
                "wylder": {
                    "name": "Wylder",
                    "category": "character",
                    "lore": "...",
                    etc
                }
            }

            This way, if the user does something like /info Wylder lore, the bot can access the Wylder key and from it's values, select the appropriate key with that keys value
            '''
            category_lookup.setdefault(category, []).append(name) # setdefault checks if the category already exists in category_lookup, if it doesn't, then it adds it as a key. If it exists, then it keeps going with the rest of the operation. The rest of the operation is adding the name of the character we're currently on into a list. This will create a dictionary with two keys, character and boss. Each of these keys will hold a list as their values, the character key will have a list holding the name of all of the characters and the boss key will hold a list with all the names of the bosses
    
    return name_lookup, category_lookup

load_game_data()