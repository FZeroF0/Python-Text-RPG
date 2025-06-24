# Text-Based Python RPG: The Echoes of Aethelgard

A classic text-based adventure game written in Python, where player choices determine their path, encounters, and destiny. Explore various locations, interact with characters, complete quests, and engage in turn-based combat in a world filled with mystery and danger.

## Table of Contents

* [Game Overview](#game-overview)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [How to Play](#how-to-play)
* [Game Mechanics](#game-mechanics)
* [Future Enhancements](#future-enhancements)
* [License](#license)

## Game Overview

"The Echoes of Aethelgard" (or your preferred game name) is a command-line role-playing game where players navigate through different environments, make decisions that affect the storyline, and manage their character's health and inventory. The game features random encounters, simple combat, and evolving quest lines based on player interaction.

## Features

* **Diverse Locations:** Explore various areas including a swamp, forest, mountains, field, and market.
* **Character Interaction:** Encounter and interact with unique NPCs like a Lumberjack, Wise Man, Hunter, Fisher, and a Witch.
* **Dynamic Choices:** Player decisions influence the flow of the game and unlock new paths or quests.
* **Quests System:** Engage in quests that lead to new discoveries and rewards.
* **Combat System:** Simple turn-based combat against various animals and creatures.
* **Item & Resource Management:** Collect items (e.g., fang, fur, wood, fish) and manage equipment (swords, axe, coat).
* **Health & Stamina:** Track player health and stamina for activities like fishing.
* **Input Validation:** Basic error handling for player choices to ensure valid input.

## Technologies Used

* **Python 3.x:** The core programming language.
* **`random` module:** For generating random events and encounters.
* **`time` module:** For pauses to enhance readability and pacing of the text.

## Getting Started

Follow these instructions to get a copy of the game up and running on your local machine.

### Prerequisites

* Python 3.x installed on your system.

### Installation

1.  **Clone the repository (or download the script):**
    ```bash
    git clone [https://github.com/FZeroF0/Python-Text-RPG.git](https://github.com/FZeroF0/Python-Text-RPG.git)
    cd Python-Text-RPG
    ```

2.  **Run the game script:**
    ```bash
    python adventure_game.py
    ```

### How to Play

The game is entirely text-based. You will be presented with scenarios and numerical choices.
* Read the on-screen text carefully.
* When prompted, enter the number corresponding to your desired action or choice.
* Press `Enter` to confirm your input.
* Follow the narrative and make strategic decisions to progress through the game.

## Game Mechanics

* **Player Health:** Decreases during combat or certain events.
* **Inventory:** Items like `fang`, `fur`, `wood`, and various `swords` can be collected.
* **Weapon Durability/Uses:** Swords and axes have a limited number of uses before breaking.
* **Quests:** Progress is often tied to completing quests given by NPCs.
* **Random Encounters:** Certain areas may trigger random animal attacks.

## Future Enhancements

This project is a foundation for a more expansive RPG experience. Here are some potential improvements:

* **Externalize Text & Dialogue:** Move all hardcoded text (descriptions, dialogues, messages) into variables, lists, or external configuration files (e.g., JSON, YAML) as discussed. This makes the game easier to manage, expand, and localize.
* **Save/Load Game State:** Implement functionality to save the player's progress (health, inventory, quest status, location) and load a saved game. This could use file I/O (e.g., JSON or pickle).
* **Object-Oriented Design:** Refactor game elements (Player, NPC, Item, Location, Enemy) into classes for better organization, reusability, and maintainability.
* **More Complex Storylines:** Develop more branching narratives, consequences for choices, and multiple endings.
* **Rich Inventory System:** Allow players to view, use, and manage items more effectively.
* **Advanced Combat:** Introduce more detailed combat mechanics, enemy types, and player abilities.
* **Graphical User Interface (GUI):** Explore frameworks like Tkinter, Pygame, or Kivy to create a visual interface beyond the command line.
* **Error Handling & Edge Cases:** Improve robustness against unexpected user inputs or game states.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
