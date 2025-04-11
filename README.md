# Overview

This project was to try doing a goal I had, which is to create a game with graphics and not have it run in the terminal as a text only game. I have also really wanted to try making tic-tac-toe as a video game since I was a little kid because I thought if I could do that, I could make any video game. This diffidently accomplished a lot in helping me learn more as a software engineer and also furthered my learning a lot. I never knew how to save things to a Json file in Python and now I know. I also learned all about the game world, and how everything lives on an x, y coordinate on the game world. I also learned so much more about Python than I knew when I first learned the language. 

How to play this game is pretty simple. It is a two-player tic-tac-toe game where each player takes a turn with the mouse to drag and drop their piece onto the grid, or they can simply click a square and the piece will go there. After someone wins the game will put a line through the winner's pieces much like how you do on paper. There are three unique features I added to the game to make it user friendly. The first thing I added was when you pressed the 'space bar' it will reset the game back to the beginning. The second thing being if you press 'S' on your keyboard you will save that current game at the current turn. The final thing is if you press 'L' on your keyboard you will load that saved game back onto the screen. So, if you want to try playing the game over and over again at a specific turn, or if you need to leave you can continue that game you were playing again.

# Development Environment

The tools that I used to program this game was VSCode, YouTube, W3Schools, and a little bit of help from Microsoft Copilot to help me trouble shoot and get answers to some questions I had while coding.

The language I used was Python, and I used the library called PyGame to make the game itself. PyGame was a very powerful library for making games and really helped simplify the process of making this game down tremendously. I also used the Json library Python has to save and load the player's game. I used the Enum library that Python has to create a state machine. This state machine would keep track of what state the game was in. I learned about these a long time ago and thought this was the perfect spot to apply one. Everything else used in the project I made from scratch.

# Useful Websites

* [Visual Studio Code Docs - Getting Started with Python](https://code.visualstudio.com/docs/python/python-tutorial)
* [W3Schools - Python Variables](https://www.w3schools.com/python/python_variables.asp)
* [W3Schools - Python Operators](https://www.w3schools.com/python/python_operators.asp)
* [W3Schools - Python Conditionals](https://www.w3schools.com/python/python_conditions.asp)
* [W3Schools - Python Match](https://www.w3schools.com/python/python_match.asp)
* [W3Schools - Python For Loops](https://www.w3schools.com/python/python_for_loops.asp)
* [W3Schools - Python While Loops](https://www.w3schools.com/python/python_while_loops.asp)
* [W3Schools - Python Functions](https://www.w3schools.com/python/python_functions.asp)
* [W3Schools - Python Sets](https://www.w3schools.com/python/python_sets.asp)
* [W3Schools - Python Lists](https://www.w3schools.com/python/python_lists.asp)
* [W3Schools - Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)
* [W3Schools - Python Classes/Objects](https://www.w3schools.com/python/python_classes.asp)
* [W3Schools - Python JSON](https://www.w3schools.com/python/python_json.asp)
* [YouTube - Robot Maze: How to create a GRID in PYGAME - Pygame Snake Game #2](https://www.youtube.com/watch?v=s_OOJaGmyXI)
* [YouTube - Coding With Russ: PyGame Beginner Tutorial in Python - Adding Buttons](https://www.youtube.com/watch?v=G8MYGDf_9ho)
* [YouTube - Coder Space: Coding Tic Tac Toe in Python with Pygame](https://www.youtube.com/watch?v=q_Nzuyvf3tw)
* [YouTube - Coding With Russ: How to Drag and Drop Items In Pygame](https://www.youtube.com/watch?v=Ro82dac_J1Y)
* [YouTube - It's That Ian Guy: PyGame State Machine - Python Game Dev Tutorial](https://www.youtube.com/watch?v=PZTqfag3T7M)
* [YouTube - Fabio Musanni - Programming Channel - How to save and load data in Python using JSON files](https://www.youtube.com/watch?v=ttQidKChD4c&pp=ygULI3NhdmVweXRob24%3D)

# Future Work

* Adding an AI to play with, this would add some more fun to this game because not all of us have a buddy to play with.
* Add a way to customize colors of the X's and O's and maybe the grid as well, this way a player's tic-tac-toe will feel more like theirs.
* Adding a way to have levels or a single player campaign. That way a player can fight more advanced AI's and keep playing as they win each level.
