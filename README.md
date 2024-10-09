# Choose Your Own Adventure - the Python Game about Singapore.

## Table Of Contents

- [About The Project](#about-the-project)
- [How To Run](#how-to-run)
    - [Original Project](#original-project)
    - [Enhanced Project](#enhanced-project)
- [Disclaimer](#disclaimer)

## About The Project

This Choose Your Own Adventure game (with a twist) was created as part of my IT140 - Introduction to Scripting class in my first year of university. It is a Python game that, instead of being built around weapons, takes the player on a journey around key places in the city-state (which also happens to be my home country). The enhancements made to this project come in the form of pathfinding with Dijkstra's Algorithm to find the cheapest path between locations, which optimises the player's journey. I also added a cheat mode feature, which gives the players (with the depth-first search) the ability to traverse locations and show the correct answers for quiz questions.

## How To Run

1. First, make sure that [Docker](https://www.docker.com/) is installed on your computer.

2. Clone the repository on your computer through either:
    -  the Web URL:

    ```bash
    git clone https://github.com/functionfaiecho/PythonGame.git
    ```

    - the [GitHub CLI](https://cli.github.com/):

    ```bash
    gh repo clone functionfaiecho/PythonGame
    ```

    then navigate to the directory by running: 

    ```bash
    cd PythonGame
    ```

3. In the root folder, run:

    ```bash
    docker-compose build
    ```

    You now have both the original and enhanced projects built.

### Original Project

To run the original project (before enhancements), use:

```bash
docker-compose run original
```
The original game was implemented as a single file (```originalgame.py```) that handled all aspects of the game logic, from location data to quiz questions and game logic in a single script. Although this would have worked just fine, it would have been difficult to make any changes or developments to the project.

### Enhanced Project
To run the enhanced version of this project, run the following:

```bash
docker-compose run enhanced
```
There are a number of enhancements that are present in this version of the project. First, I added a cheat mode with Depth-First Search (DFS) that allows the player to explore all possible routes and see the correct answers to the quiz questions. In addition, I incorporated Dijkstra's Algorithm to find the cheapest path to the final destination. This feature introduced a unique way for the player to interact with the game. 

## Disclaimer

This game was created solely for academic purposes. Any resemblance to real-life persons or state of affairs is purely coincidental. This game will be deleted on completion of the class it is for.
