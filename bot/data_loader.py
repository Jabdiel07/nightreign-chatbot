import csv
from pathlib import Path
from typing import Dict, List, Tuple

def load_game_data(path: str="data\game_info.csv") -> Tuple[Dict[str,dict], Dict[str,List[str]]]:
    name_lookup: Dict[str, dict] = {} # maps each character/boss name to their respective row
    category_lookup: Dict[str, List[str]] = {} # maps each character/boss names to their respective category into a list

    # locates the path of the csv file
    csv_path = Path(path)
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f) # DictReader reads each line as a dict where the key is the top row in the file and the values are the rest of the rows

        for row in reader:
            name = row["name"].strip()
            category = row["category"].strip().lower()
            name_lookup[name.lower()] = row
            category_lookup.setdefault(category, []).append(name) # setdefault checks if the category already exists in category_lookup, if it doesn't, then it adds it as a key. If it exists, then it keeps going with the rest of the operation
    
    return name_lookup, category_lookup

load_game_data()