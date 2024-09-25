# Choose Your Own Adventure - the Python Game about Singapore.

## Table Of Contents

- [About The Project](#about-the-project)
- [How To Run](#how-to-run)
    - [Original Project](#original-project)
    - [Enhanced Project](#enhanced-project)


## About The Project

This Choose Your Own Adventure game (with a twist) was created as part of my IT140 - Introduction to Scripting class in my first year of university. It is a Python game that, instead of being built around weapons, takes the player on a journey around key places in the city-state (which also happens to be my home country). The enhancements made to this project come in the form of pathfinding with Dijkstra's Algorithm to find the cheapest path between locations, which optimises the player's journey. I also added a cheat mode feature, which gives the players (with the depth-first search) the ability to traverse locations and show the correct answers for quiz questions.

## How To Run

1. First, make sure that [Docker](https://www.docker.com/) is installed on your computer.

2. Clone the repository on your computer through either:
    -  the Web URL:

```https://github.com/functionfaiecho/PythonGame.git```

    - the [GitHub CLI](https://cli.github.com/):

```gh repo clone functionfaiecho/PythonGame```

3. In the root folder, run:

```docker-compose build```. You now have both the original and enhanced projects built.

### Original Project

### Enhanced Project