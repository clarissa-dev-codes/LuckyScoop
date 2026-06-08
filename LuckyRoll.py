#Amount ordered, and more sometimes
#needs the random library for the extra stuff
from Inventory import load_inventory, save_inventory


def luckyRoll(amount):
    import random as rnd

    inventory_list = load_inventory()
    available = [item for item in inventory_list if item.quantity > 0]

    if not available:
        return "Empty Database", [0,0,0]

    luckyNum1 = rnd.randint(0,9)
    luckyNum2 = rnd.randint(0,9)
    luckyNum3 = rnd.randint(0,9)
    winning_numbers = [luckyNum1, luckyNum2, luckyNum3]

    results = {}

    rolls = amount
    rolls_done = 0

    while rolls_done < rolls:
        if not available:
            break

        temp = rnd.choice(available)
        rolls_done += 1

        if temp.luckyNum == luckyNum1 or temp.luckyNum == luckyNum2 or temp.luckyNum == luckyNum3:
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
                    available.remove(master_item)
                break

    save_inventory(inventory_list)

    return results, winning_numbers