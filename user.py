import json
import copy
from Figures import starters,Figure

class Player:
    def __init__(self, username):
        self.username = username
        self.coins = 150
        self.collection = []
        self.battle_team = []    

    def add_to_collection(self, figure):
        self.collection.append(figure)
        print(f"{figure.name} has been added to {self.username}'s collection!")
        
        # Quality of life: automatically equip it if the battle team isn't full yet
        if len(self.battle_team) < 3:
            self.battle_team.append(figure)
            print(f" {figure.name} was automatically placed in your Battle Team ({len(self.battle_team)}/3).")

    def equip_figure(self, figure_index_in_collection):
        try:
            chosen_figure = self.collection[figure_index_in_collection]
            
            # Check if already equipped
            if chosen_figure in self.battle_team:
                print(f" {chosen_figure.name} is already in your battle team!")
                return
                
            # If team is full, we must replace someone
            if len(self.battle_team) >= 3:
                print("\nYour Battle Team is full! Who do you want to replace?")
                for i, fig in enumerate(self.battle_team):
                    print(f"{i + 1}. {fig.name} (Lv. {fig.level})")
                
                replace_choice = int(input("Choose a slot to replace (1-3): ")) - 1
                if 0 <= replace_choice < 3:
                    removed = self.battle_team[replace_choice]
                    self.battle_team[replace_choice] = chosen_figure
                    print(f" Swapped out {removed.name} for {chosen_figure.name}!")
                else:
                    print(" Invalid slot choice. Swap canceled.")
            else:
                # If there's open space, just add them
                self.battle_team.append(chosen_figure)
                print(f" {chosen_figure.name} added to your battle team!")
                
        except IndexError:
            print(" Invalid collection index.")

    def display_profile(self):
        print(f"\n=================== {self.username.upper()}'S PROFILE ===================")
        print(f" Coins: {self.coins}")
        print("\nACTIVE BATTLE TEAM ")
        for i, fig in enumerate(self.battle_team):
            print(f"  Slot {i+1}: {fig.name} (Lv. {fig.level}) - HP: {fig.max_health} | Type: {fig.type}")
        
        print("\nFULL COLLECTION")
        for i, fig in enumerate(self.collection):
            print(f"  [{i}] {fig.name} (Lv. {fig.level})")
        print("========================================================")

    def save_game(self):
        """Saves player stats, collection, and battle team to a JSON file."""
        # Convert figures into a dictionary format JSON can understand
        serialized_collection = []
        for fig in self.collection:
            serialized_collection.append({
                "name": fig.name,
                "level": fig.level,
                "experience": fig.experience,
                "exp_cap": fig.exp_cap,
                "max_health": fig.max_health,
                "power": fig.power,
                "dodge": fig.dodge,
                "luck": fig.luck
            })
            
        # For the battle team, we just save the index numbers of where they sit in the collection
        serialized_team_indices = []
        for fig in self.battle_team:
            if fig in self.collection:
                serialized_team_indices.append(self.collection.index(fig))

        save_data = {
            "username": self.username,
            "coins": self.coins,
            "collection": serialized_collection,
            "battle_team_indices": serialized_team_indices
        }
        
        with open("save_data.json", "w") as f:
            json.dump(save_data, f, indent=4)
        print("Game saved successfully!")

    def load_game(self):
        """Loads player data from save_data.json and rebuilds objects."""
        try:
            with open("save_data.json", "r") as f:
                save_data = json.load(f)
                
            self.username = save_data["username"]
            self.coins = save_data["coins"]
            self.collection = []
            self.battle_team = []
            
            # Rebuild the figures in the collection
            for item in save_data["collection"]:
                # Use the moveset from our baseline starters database
                base_moves = starters[item["name"]].attacks
                
                # Reconstruct the Figure object using saved level/stats
                loaded_fig = Figure(
                    name=item["name"],
                    figure_type=starters[item["name"]].type,
                    level=item["level"],
                    health=item["max_health"],
                    power=item["power"],
                    dodge=item["dodge"],
                    luck=item["luck"],
                    attacks=base_moves
                )
                loaded_fig.experience = item["experience"]
                loaded_fig.exp_cap = item["exp_cap"]
                loaded_fig.current_health = loaded_fig.max_health
                
                self.collection.append(loaded_fig)
                
            # Reassign who belongs on the active battle team
            for index in save_data["battle_team_indices"]:
                self.battle_team.append(self.collection[index])
                
            print(f"Save file loaded! Welcome back, {self.username}!")
            return True
        except FileNotFoundError:
            print("❌ No save file found. Starting a fresh game!")
            return False