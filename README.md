# lab1_AI
***How to Compile and Run the Code***

# Prerequisites: Python 3.x  (above 3.0 is stable) 

# Steps to Compile and Run

1. Clone the repository

git clone https://github.com/MrT2003/Laboratory_AI_LAB_1

# Recommend using virtual environments to set up library
    (*) For Linux/macOS
        python3 -m venv venv
        source venv/bin/activate
    (*) For Windows
        python -m venv venv
        venv\Scripts\activate
------------------

Exercise 1: 
To run RandomAgent (in the Agents.py file) in the tinyMaze environment:
python pacman.py --layout tinyMaze --pacman RandomAgent

To run RandomAgent (in the Agents.py file) in the mediumMaze environment:
python pacman.py --layout mediumMaze --pacman RandomAgent

Exercise 2: 
To run RandomAgent in myLayout environment: 
python pacman.py --layout myLayout --pacman RandomAgent

To run RandomAgent in openSearch environment:
python pacman.py --layout openSearch --pacman RandomAgent

Exercise 3: 
To run the BetterRandomAgent (in the file Agent.py) in openSearch environment:
python pacman.py --layout openSearch --pacman BetterRandomAgent

To run the BetterRandomAgent (in the file Agent.py) in myLayout environment:
python pacman.py --layout myLayout --pacman BetterRandomAgent

Exercise 4: 
To run ReflexAgent (in the Agents.py file) in the openSearch layout: 
python pacman.py --layout openSearch --pacman ReflexAgent

To run ReflexAgent (in the Agents.py file) in the myLayout layout:
python pacman.py --layout myLayout --pacman ReflexAgent