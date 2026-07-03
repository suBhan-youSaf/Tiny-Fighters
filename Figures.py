class Figure:
    def __init__(self, name, figure_type, level, health, power, dodge, luck, attacks):
        self.name = name
        self.type = figure_type
        self.level = level
        
        # Stats
        self.max_health = health
        self.current_health = health
        self.power = power
        self.dodge = dodge
        self.luck = luck
        
        # Experience
        self.experience = 0
        self.exp_cap = 100  # Default starting cap, can be overridden
        
        # Attacks (Expects a list of dictionaries or tuples)
        # e.g., [{"name": "Punch", "damage": 10, "cost": 1}, ...]
        self.attacks = attacks 

    def gain_experience(self, amount):
        """Adds experience and checks for a level up."""
        self.experience += amount
        print(f"{self.name} gained {amount} EXP! ({self.experience}/{self.exp_cap})")
        
        # Using a while loop in case they gain enough EXP to level up multiple times
        while self.experience >= self.exp_cap:
            self.level_up()

    def level_up(self):
        """Handles stat increases when leveling up."""
        self.experience -= self.exp_cap  # Carry over leftover EXP
        self.level += 1
        self.exp_cap += 50
        
        # Stat increases
        self.max_health += 10
        self.current_health = self.max_health  # Heal them on level up!
        self.power += 5
        self.dodge += 2
        self.luck += 1
        
        print(f" LEVEL UP! {self.name} reached Level {self.level}! ")
        # --- STARTER ATTACKS DATA ---

robin_attacks = [
    {"name": "Birdarang", "damage": 10, "cost": 1},
    {"name": "Staff Slam", "damage": 22, "cost": 2},
    {"name": "Titan Shield", "damage": 0, "cost": 3}  # A defensive buff later!
]

beast_boy_attacks = [
    {"name": "Cat Scratch", "damage": 8, "cost": 1},
    {"name": "Ram Charge", "damage": 25, "cost": 2},
    {"name": "T-Rex Chomp", "damage": 40, "cost": 3}
]

raven_attacks = [
    {"name": "Shadow Poke", "damage": 12, "cost": 1},
    {"name": "Dark Void", "damage": 20, "cost": 2},
    {"name": "Azarath Metrion!", "damage": 35, "cost": 3}
]

cyborg_attacks = [
    {"name": "Laser Pistol", "damage": 10, "cost": 1},
    {"name": "Sonic Cannon", "damage": 24, "cost": 2},
    {"name": "Missile Barrage", "damage": 45, "cost": 3}
]

starfire_attacks = [
    {"name": "Starbolt", "damage": 11, "cost": 1},
    {"name": "Eye Beams", "damage": 21, "cost": 2},
    {"name": "Green Fury", "damage": 38, "cost": 3}
]

# --- EXPANSION PACK ATTACKS DATA ---

silk_attacks = [
    {"name": "Cute Nibble", "damage": 7, "cost": 1},
    {"name": "Web Spit", "damage": 18, "cost": 2},
    {"name": "Eye Sparkle Beam", "damage": 35, "cost": 3}
]

jinx_attacks = [
    {"name": "Bad Luck Hex", "damage": 14, "cost": 1},
    {"name": "Pink Flame", "damage": 24, "cost": 2},
    {"name": "Cataclysm Vortex", "damage": 42, "cost": 3}
]

slade_attacks = [
    {"name": "Tactical Strike", "damage": 15, "cost": 1},
    {"name": "Flashbang Bomb", "damage": 26, "cost": 2},
    {"name": "Mastermind Execution", "damage": 50, "cost": 3}
]

bumblebee_attacks = [
    {"name": "Stinger Blast", "damage": 10, "cost": 1},
    {"name": "Buzzing Dash", "damage": 22, "cost": 2},
    {"name": "Hive Swarm", "damage": 39, "cost": 3}
]

kid_flash_attacks = [
    {"name": "Quick Jab", "damage": 9, "cost": 1},
    {"name": "Speed Force Tornado", "damage": 20, "cost": 2},
    {"name": "Infinite Mass Punch", "damage": 46, "cost": 3}
]
# --- INITIALIZING THE TITANS ---

starters = {
    "Robin": Figure("Robin", "Hero", 1, 100, 15, 5, 5, robin_attacks),
    "Beast Boy": Figure("Beast Boy", "Beast", 1, 110, 12, 7, 4, beast_boy_attacks),
    "Raven": Figure("Raven", "Dark", 1, 90, 18, 4, 6, raven_attacks),
    "Cyborg": Figure("Cyborg", "Cyborg", 1, 130, 14, 2, 3, cyborg_attacks),
    "Starfire": Figure("Starfire", "Alien", 1, 105, 16, 4, 5, starfire_attacks),
    "Silkie": Figure("Silkie", "Alien", 1, 140, 10, 3, 8, silk_attacks),
    "Jinx": Figure("Jinx", "Dark", 1, 95, 17, 6, 4, jinx_attacks),
    "Slade": Figure("Slade", "Hero", 1, 120, 20, 5, 5, slade_attacks),
    "Bumblebee": Figure("Bumblebee", "Cyborg", 1, 105, 14, 8, 5, bumblebee_attacks),
    "Kid Flash": Figure("Kid Flash", "Beast", 1, 100, 15, 10, 6, kid_flash_attacks)
}

TYPE_ADVANTAGES = {
    "Hero":   {"strong_against": "Cyborg", "weak_against": "Dark"},
    "Cyborg": {"strong_against": "Alien",  "weak_against": "Hero"},
    "Alien":  {"strong_against": "Beast",  "weak_against": "Cyborg"},
    "Beast":  {"strong_against": "Dark",   "weak_against": "Alien"},
    "Dark":   {"strong_against": "Hero",   "weak_against": "Beast"}
}