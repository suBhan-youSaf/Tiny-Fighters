# 🗼 Tiny Fighters

A fully operational, text-based RPG battle engine and collection game inspired by the hit Cartoon Network mobile game *Teeny Titans* (Teen Titans Go!). Built entirely in Python, this game features strategic combat, an economic shopping loop, random gacha unboxings, a dynamic type-advantage system, and a persistent progress-saving engine.

## 🚀 Key Features

* **Real-Time Action Bar (ATB) Combat:** Simulates the signature *Teeny Titans* battle rhythm. Figures automatically charge up action bars based on their stats, allowing players to execute high-cost mega attacks or tactical low-cost strikes.
* **Strategic Pre-Battle Scouting:** Players get full tactical radar intel on the opposing NPC squad before locking in their line-up. Includes an on-screen **Type Advantage Cheat Sheet** to help pick perfect counters.
* **Dynamic Matchmaking:** Automatically filters and scales opponents based on your lead figure's level. Move flawlessly from easy 1v1 training targets to intense 3v3 endgame boss battles.
* **Gacha Economy & Toy Shop:** Spend hard-earned battle coins in the local Toy Shop to crack open Mystery Boxes and collect rare new figures.
* **Persistent Save System:** Built-in JSON serialization saves your exact player wallet, full collection history, active squads, and current character levels seamlessly.

---

## 📂 Project Architecture

The game is built using a clean, decoupled, object-oriented structure:

* `Figures.py` – The core database defining Figure classes, baseline attribute sheets, scaling levels, and the elemental type-advantage matrix.
* `user.py` – Tracks player progress, profile layout, inventories, equipped combat teams, and handles file serialization/deserialization logic.
* `shop.py` – Controls the Gacha storefront math, coin transaction verification, and collection appending.
* `npcs.py` – Models custom artificial trainers, scaling dialogues, variable difficulty rewards, and handles dynamic combat squad generation.
* `battle.py` – The operational core of the game. Manages turn-by-turn math, type-multiplier damage scaling, active-vs-benched squad visibility, and reward tracking.
* `main.py` – The master console hub routing the central gameplay loops.

---

## 🎮 How to Play

1. Clone or download the repository files into a single directory.
2. Fire up your terminal and run the launch script:
```bash
python main.py

```


3. Enter your Titan name, claim your free Robin starter figure, and head straight to the **Battle Arena** to grind or the **Toy Shop** to expand your collection!
