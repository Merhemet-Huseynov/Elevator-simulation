# Lift Simulation System

## Overview

This project simulates  the  operation of  an elevator in a building. 
It describes  the elevator's  movement  between  floors  based  on the 
user's  request. The elevator  moves based on the user's current floor
and target floor, and  it checks if the elevator is full or if  it has 
reached the target floor.

This system is written in Python and supports user creation, elevator
movement, and status tracking functionalities.

## Features

- **User Simulation**: Users are randomly assigned to floors and target
floors.
- **Elevator Movement**: The elevator moves based on the user's current
floor and target floor.
- **Floor Status**: The elevator's status is checked and  displayed for 
each floor, including whether the elevator is full or not.
- **Direction  Control**: The  elevator's  direction (up or down) is 
determined based on the user's position.
- **Terminal Clearing**: The terminal is cleared after each simulation 
step, displaying new data.

## Requirements

- Python 3.12.5
This script uses only Python's built-in libraries (`random`, `time`, `os`,
`datetime`).  Use `prettable` for formatting tables, ensure it is installed
(`pip install prettable`) as it is not part of Python's standard library.

## Running the Simulation

1. Clone or download the repository.
2. Make sure Python 3.12.5 is installed on your computer.
3. Start the lift system by running the `simulation()` function.

```bash
python main.py
