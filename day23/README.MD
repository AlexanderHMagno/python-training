# Turtle Crossing Game

A simple arcade-style game built with Python's Turtle graphics where you help a turtle cross a busy road.

## Game Description

In this game, you control a turtle that needs to cross a road filled with moving cars. The objective is to safely guide the turtle from the bottom of the screen to the top while avoiding collisions with cars.

## Game Preview

![Turtle Crossing Game](game_preview.png)

### Features:

- Player-controlled turtle that can move up and down
- Randomly generated cars moving across the screen
- Increasing difficulty as cars speed up over time
- Collision detection between turtle and cars
- Game over when turtle collides with a car

## Controls

- Up Arrow: Move turtle forward
- Down Arrow: Move turtle backward

## Implementation Details

The game is built using several Python classes:

- `TurtleCrossingGame`: Main game controller
- `Character`: Player-controlled turtle
- `Car`: Moving obstacles

### Technical Features:

- Object-oriented design with inheritance from Turtle class
- Random car generation and movement
- Dynamic difficulty scaling
- Screen boundary detection
- Collision detection system

## Requirements

- Python 3.x
- Python Turtle Graphics module
