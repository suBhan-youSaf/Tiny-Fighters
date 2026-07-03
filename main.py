import random
import copy
import sys
import os

from Figures import starters
from user import Player
from shop import display_shop
from NPC import npc_list
from battle import start_battle

def main():
    print("=========================================")
    print("   WELCOME TO TINY FIGHTERS:   ")
    print("=========================================")
    
    # Initialize a temporary blank player profile
    player = Player("Placeholder")
    
    # Check if a save file exists
    if os.path.exists("save_data.json"):
        load_choice = input("Found existing save file! Load game? (y/n): ").strip().lower()
        if load_choice in ["y", "yes"]:
            player.load_game()
        else:
            print("\nStarting a brand new adventure...")
            username = input("Enter your Titan Name: ").strip()
            player = Player(username if username else "RobinFan")
            player.add_to_collection(copy.deepcopy(starters["Robin"]))
    else:
        print("\nStarting a brand new adventure...")
        username = input("Enter your Titan Name: ").strip()
        player = Player(username if username else "RobinFan")
        player.add_to_collection(copy.deepcopy(starters["Robin"]))
        
    input("\nPress Enter to enter the Junk City Hub...")

    while True:
        print("\n=================== JUNK CITY HUB ===================")
        print(f" Player: {player.username} | Coins: {player.coins}")
        print("-----------------------------------------------------")
        print("1.  Enter the Battle Arena")
        print("2.  Visit the Toy Shop (Cost: 50 Coins)")
        print("3.  View Profile & Battle Team")
        print("4.  Save Game")
        print("5.  Save and Quit Game")
        print("=====================================================")
        
        choice = input("What do you want to do? (1-5): ").strip()
        
        if choice == "1":
            print("\n=====================================================")
            print(" ENTERING THE BATTLE ARENA... MATCHMAKING... ")
            print("=====================================================")
            
            # 1. Determine difficulty based on lead figure level
            lead_level = player.battle_team[0].level if player.battle_team else 1
            if lead_level == 1:
                pool = [n for n in npc_list if len(n.team_names) == 1]
            elif lead_level == 2:
                pool = [n for n in npc_list if len(n.team_names) <= 2]
            else:
                pool = npc_list
                
            npc_template = random.choice(pool)
            active_npc = copy.deepcopy(npc_template)
            
            # 2. INTEL: Pull directly from starters database to guarantee accurate scouting
            print(f"\nChallenger Spotted: {active_npc.name} ")
            print(f'"{active_npc.name}: {active_npc.dialogue}"')
            print("\n ENEMY SQUAD ANALYSIS (SCOUTED):")
            
            for fig_name in active_npc.team_names:
                if fig_name in starters:
                    enemy_template = starters[fig_name]
                    print(f"   {enemy_template.name:<12} | Type: {enemy_template.type:<7} | HP: {enemy_template.max_health:<4} | Power: {enemy_template.power}")
            print("-" * 55)
            
            # 3. TYPE CHEAT SHEET
            print("\n---------------- TYPE ADVANTAGES ----------------")
            print(" Hero  > Cyborg  > Alien  > Beast  > Dark  > Hero")
            print("-------------------------------------------------")
            
            # 4. TEAM SELECTION POP-UP
            print(f"\n Choose 3 figures from your collection to counter {active_npc.name}!")
            for i, fig in enumerate(player.collection):
                print(f"  [{i}] {fig.name} (Lv.{fig.level}) - Type: {fig.type} | HP: {fig.max_health}")
                
            new_battle_team = []
            slots_needed = min(3, len(player.collection))
            
            while len(new_battle_team) < slots_needed:
                try:
                    pick = int(input(f"Select Figure for Slot {len(new_battle_team) + 1} (Enter number #): "))
                    if 0 <= pick < len(player.collection):
                        chosen_fig = player.collection[pick]
                        if chosen_fig in new_battle_team:
                            print(" You already picked that figure! Choose a different one.")
                        else:
                            new_battle_team.append(chosen_fig)
                            print(f" {chosen_fig.name} locked into Slot {len(new_battle_team)}!")
                    else:
                        print(" Invalid collection number.")
                except ValueError:
                    print(" Please type a valid number.")
            
            # Override active battle team with choice
            player.battle_team = new_battle_team
            
            # 5. Spawn the live enemy fighters right before launching
            active_npc.generate_team()
            
            input("\nSquad locked! Press Enter to launch the battle...")
            start_battle(player, active_npc)
            
            
        elif choice == "2":
            display_shop(player)
            
        elif choice == "3":
            player.display_profile()
            manage = input("\nWould you like to equip/swap a figure? (yes/no): ").strip().lower()
            if manage in ["yes", "y"]:
                try:
                    idx = int(input("Enter the collection number [#] of the figure you want to equip: "))
                    player.equip_figure(idx)
                except ValueError:
                    print(" Please enter a valid number.")
                    
        elif choice == "4":
            player.save_game()
            
        elif choice == "5":
            player.save_game()
            print(f"\nThanks for playing, {player.username}! Titan Tower out! ")
            sys.exit()
            
        else:
            print(" Invalid command.")

if __name__ == "__main__":
    main()