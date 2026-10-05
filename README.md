# 🎲 Craps Game (Python)

## Overview
This project is a simple Python implementation of the classic casino dice game **Craps**.  
It demonstrates how to use Python’s `random` library to simulate dice rolls and apply the game’s rules.

## How It Works
1. **First Roll**
   - If the sum is **7 or 11 → Player wins immediately**.
   - If the sum is **2, 3, or 12 → Casino wins immediately**.
   - If the sum is **4, 5, 6, 8, 9, or 10 → That number becomes the *goal*.**

2. **Goal Phase**
   - Keep rolling until:
     - You roll the **goal number again → Player wins**.
     - You roll a **7 → Casino wins**.

The game always ends with either the player or the casino winning.

## How to Run
1. Make sure you have Python installed.
2. Clone this repository:
   ```bash
   git clone https://github.com/creepy-coder777/Python_Station_Project2
   cd Python_Station_Project2
