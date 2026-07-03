import time
import random
from Figures import TYPE_ADVANTAGES

def calculate_damage(attacker, defender, attack_power):
    """Calculates final damage using your Type Advantage system."""
    atk_type = attacker.type
    def_type = defender.type
    multiplier = 1.0
    message = ""

    # Check the matrix you built in Figures.py
    if atk_type in TYPE_ADVANTAGES:
        if TYPE_ADVANTAGES[atk_type]["strong_against"] == def_type:
            multiplier = 1.5
            message = " SUPER EFFECTIVE! "
        elif TYPE_ADVANTAGES[atk_type]["weak_against"] == def_type:
            multiplier = 0.5
            message = " Not very effective... "

    # Base damage + a small bonus from the figure's power stat
    final_damage = int((attack_power + attacker.power * 0.2) * multiplier)
    return final_damage, message

def start_battle(player, npc):
    """Starts a team-vs-team battle against an NPC."""
    if not player.battle_team:
        print(" You don't have any figures equipped!")
        return

    print(f"\n==================================================")
    print(f" CHALLENGE: {player.username} VS {npc.name} ")
    print(f'"{npc.name}: {npc.dialogue}"')
    print(f"==================================================")
    time.sleep(1.5)

    # Track active fighter indices for both sides
    p_idx = 0
    e_idx = 0

    player_bar = 0.0
    enemy_bar = 0.0

    while p_idx < len(player.battle_team) and e_idx < len(npc.battle_team):
        player_fig = player.battle_team[p_idx]
        enemy_fig = npc.battle_team[e_idx]

        # Standard charging speeds
        player_speed = 0.25 + (player_fig.luck * 0.01)
        enemy_speed = 0.25 + (enemy_fig.luck * 0.01)

        # 1. Charge Bars
        player_bar = min(player_bar + player_speed, 3.0)
        enemy_bar = min(enemy_bar + enemy_speed, 3.0)

        p_bar_visual = "█" * int(player_bar) + "░" * (3 - int(player_bar))
        print(f"\n {player_fig.name} (Lv.{player_fig.level}) HP: {player_fig.current_health}/{player_fig.max_health} | Bar: [{p_bar_visual}]")
        print(f" {npc.name}'s {enemy_fig.name} (Lv.{enemy_fig.level}) HP: {enemy_fig.current_health}/{enemy_fig.max_health}")

        # 2. Player Turn
        if player_bar >= 1.0:
            print(f"\n--- YOUR ACTION ---")
            for idx, atk in enumerate(player_fig.attacks):
                print(f"  {idx + 1}. {atk['name']} (Cost: {atk['cost']}, Dmg: {atk['damage']})")
            print("  4. Pass/Charge")
            
            try:
                choice = int(input("Choose (1-4): ")) - 1
                if choice in [0, 1, 2]:
                    atk = player_fig.attacks[choice]
                    if player_bar >= atk['cost']:
                        player_bar -= atk['cost']
                        dmg, msg = calculate_damage(player_fig, enemy_fig, atk['damage'])
                        if msg: print(msg)
                        enemy_fig.current_health = max(0, enemy_fig.current_health - dmg)
                        print(f" Used {atk['name']}! Dealt {dmg} damage.")
                    else:
                        print(" Not enough bar!")
            except ValueError:
                print("Invalid input.")

        # 3. Enemy AI Turn
        if enemy_fig.current_health > 0 and enemy_bar >= 1.0:
            affordable = [a for a in enemy_fig.attacks if enemy_bar >= a['cost']]
            if affordable:
                atk = max(affordable, key=lambda x: x['damage'])
                enemy_bar -= atk['cost']
                dmg, msg = calculate_damage(enemy_fig, player_fig, atk['damage'])
                if msg: print(msg)
                player_fig.current_health = max(0, player_fig.current_health - dmg)
                print(f"\n {enemy_fig.name} used {atk['name']}! Dealt {dmg} damage.")

        # 4. Check for Knockouts
        if player_fig.current_health <= 0:
            print(f" Your {player_fig.name} was knocked out!")
            p_idx += 1  # Bring out next figure
            player_bar = 0.0
            if p_idx < len(player.battle_team):
                print(f" Go! {player.battle_team[p_idx].name}!")

        if enemy_fig.current_health <= 0:
            print(f" Enemy {enemy_fig.name} was knocked out!")
            e_idx += 1  # Enemy brings out next figure
            enemy_bar = 0.0

        time.sleep(1)

    # 5. Battle Results
    print("\n================ BATTLE RESULT ================")
    if p_idx < len(player.battle_team):
        print(f" You defeated {npc.name}! ")
        print(f" Gained {npc.reward_coins} coins!")
        player.coins += npc.reward_coins
        
        # Give exp to all members who fought
        for fig in player.battle_team:
            if fig.current_health > 0:
                fig.gain_experience(npc.reward_exp)
    else:
        print(f" You were completely wiped out by {npc.name}...")

    # Post-battle recovery
    for fig in player.battle_team:
        fig.current_health = fig.max_health