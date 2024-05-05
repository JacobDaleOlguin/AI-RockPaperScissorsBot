Description
This Python script implements a strategy for playing the game Rock-Paper-Scissors against an opponent. The strategy adapts based on the history of the opponent's moves as well as the player's own moves, attempting to predict and counter the opponent's next move based on identified patterns. The bot starts by playing randomly and gradually shifts to a predictive model as it gathers more data from the game rounds.

Features
Dynamic Pattern Recognition: Analyzes recent move patterns from both the player and the opponent to predict the next most likely move.
Adjustable Parameters: Easily tweak variables such as the number of initial random moves, pattern search size, and history length to optimize performance.
History Tracking: Maintains a history of moves to aid in pattern recognition and decision-making.
Dependencies
Python 3.x
random module (standard library)
How to Run
Ensure Python 3.x is installed on your system.
Save the script in a file, for example, rps_bot.py.
Run the script using the Python interpreter from the command line:

python rps_bot.py

To integrate this script with an actual game interface or another script, you will need to modify the player function call to pass the appropriate prev_play parameter based on the game context.
Function Parameters
prev_play: The last move made by the opponent.
opponent_history: A list to keep track of the opponent's move history.
my_history: A list to keep track of the player's own move history.
Sample Usage
This script is intended to be used as part of a larger game loop or simulation where the player function is called repeatedly, passing the last move of the opponent each time.
