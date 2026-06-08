#Amount ordered + if color matches, they get one more
from Inventory import load_inventory, save_inventory
colors = ("Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Black", "White")

def getOneMore(amount):
    import random as rand

    inventory_list = load_inventory()
    available = [item for item in inventory_list if item.quantity > 0]

    if not available:
        return "Empty Database", "No Color"

    lucky_color = rand.choice(colors)
    results = {}

    rolls = amount
    rolls_done = 0

    while rolls_done < rolls:
        if not available:
            break

        temp = rand.choice(available)
        rolls_done += 1

        if temp.color == lucky_color:
            rolls += 1

        for master_item in inventory_list:
            if master_item.thing == temp.thing:
                master_item.quantity -= 1

                if master_item.thing in results:
                    results[master_item.thing] += 1
                else:
                    results[master_item.thing] = 1

                temp.quantity = master_item.quantity

                if temp.quantity <= 0:
                    available.remove(temp)
                break

    save_inventory(inventory_list)

    return results, lucky_color