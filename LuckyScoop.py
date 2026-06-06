#Get a certain amount of beads = get stuff
import random as rd
from Inventory import load_inventory, save_inventory

def lucky_scoop(num_scoops):
    inventory_list = load_inventory()
    available = [item for item in inventory_list if item.quantity > 0]

    if not available:
        return "Empty Database"

    scoop_results = {}

    for _ in range(num_scoops):
        beads = rd.randint(15,30)

        for _ in range(beads):
            if not available:
                break

            drawn_pool_item = rd.choice(available)
            for master_item in inventory_list:
                if master_item.thing == drawn_pool_item.thing:
                    master_item.quantity -= 1

                    if master_item.thing in scoop_results:
                        scoop_results[master_item.thing] += 1
                    else:
                        scoop_results[master_item.thing] = 1

                    drawn_pool_item.quantity = master_item.quantity

                    if drawn_pool_item.quantity <= 0:
                        available.remove(drawn_pool_item)
                    break

    save_inventory(inventory_list)

    return scoop_results