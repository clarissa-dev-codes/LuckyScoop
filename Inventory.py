#This is where the inventory is read in and saved to the file
#As well as subtracting inventory when something is picked

import json
import os
from dataclasses import dataclass, asdict

@dataclass
class Item:
    thing: str
    price: float
    luckyNum: int
    color: str
    quantity: int

FILE_NAME = "inventory.json"

def save_inventory(inventory_list):
    data_to_save = [asdict(item) for item in inventory_list]

    with open(FILE_NAME, "w") as file:
        json.dump(data_to_save, file, indent=4)
    print("Inventory saved to JSON successfully")

def load_inventory():
    if not os.path.isfile(FILE_NAME):
        return[]

    with open(FILE_NAME, "r") as file:
        raw_data = json.load(file)

    return[Item(**data) for data in raw_data]