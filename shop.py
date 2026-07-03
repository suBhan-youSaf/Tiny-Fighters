import random
import copy
from Figures import starters

# Set a price for opening a mystery figure box
BOX_PRICE = 100

def display_shop(player):
    print("\n ================= WELCOME TO THE TOY SHOP ================= ")
    print(f" Your Current Balance: {player.coins} Coins")
    print(f" Mystery Figure Box: {BOX_PRICE} Coins")
    print("==============================================================")
    
    choice = input("Would you like to buy a Mystery Box? (yes/no): ").strip().lower()
    
    if choice == 'yes' or choice == 'y':
        buy_mystery_box(player)
    elif choice == 'no' or choice == 'n':
        print("Thanks for stopping by! Come back soon.")
    else:
        print(" Invalid choice. Exiting shop.")

def buy_mystery_box(player):
    # 1. Check if the player has enough money
    if player.coins < BOX_PRICE:
        print("\n You don't have enough coins! Go win some battles first.")
        return

    # 2. Deduct the cost
    player.coins -= BOX_PRICE
    
    # 3. Pick a random figure name from our starters keys
    available_names = list(starters.keys())
    chosen_name = random.choice(available_names)
    
    # This prevents different players or duplicate figures from sharing the exact same HP/Level data.
    new_figure = copy.deepcopy(starters[chosen_name])
    
    print("\n *Rumbling noises coming from the capsule machine* ")
    print(f" CONGRATULATIONS! You unboxed: {new_figure.name} (Type: {new_figure.type})! ")
    
    # 5. Add it to the player's collection
    player.add_to_collection(new_figure)
    print(f" Remaining Balance: {player.coins} Coins")