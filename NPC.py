import copy
from Figures import starters

class NPC:
    def __init__(self, name, dialogue, team_names, reward_coins, reward_exp):
        self.name = name
        self.dialogue = dialogue
        self.team_names = team_names  # Keep as plain strings for easy scouting!
        self.reward_coins = reward_coins
        self.reward_exp = reward_exp
        self.battle_team = []  # Starts empty, generated dynamically

    def generate_team(self):
        """Explicitly builds a fresh copy of the figures for the battle."""
        self.battle_team = []
        for fig_name in self.team_names:
            if fig_name in starters:
                self.battle_team.append(copy.deepcopy(starters[fig_name]))

# --- THE JUMP CITY CHALLENGERS ---
npc_list = [
    NPC("Plushie Fanatic", "Look at my adorable little worm! He's gonna getcha!", ["Silkie"], 20, 35),
    NPC("Burger Guy", "I should be flipping patties, but instead I'm gonna flip your team!", ["Beast Boy"], 25, 40),
    NPC("Couch Potato", "*Yawn*... I can beat you with my eyes closed. Go, laser beam!", ["Cyborg"], 30, 45),
    NPC("Gizmo", "You think your little toys can beat my tech?! Think again, snot-brain!", ["Cyborg"], 40, 40),
    NPC("Goth Kid", "Whatever... your colorful figures don't match my dark aura.", ["Raven", "Beast Boy"], 80, 75),
    NPC("Dr. Light", "Ah, fresh meat! Prepare to be completely blinded by my brilliant figures!", ["Silkie", "Cyborg"], 90, 85),
    NPC("Hive Academy Student", "The Titans are history! HIVE figures rule the school!", ["Jinx", "Bumblebee"], 110, 100),
    NPC("Speedy", "Let's see if your squad can keep up with my speed! Let's go!", ["Robin", "Starfire", "Cyborg"], 150, 120),
    NPC("Masked Mastermind", "You've done well to make it this far, child. But your collection ends here.", ["Slade", "Jinx", "Kid Flash"], 250, 200)
]