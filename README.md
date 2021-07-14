# rock-paper-scissors-exercise

A Python application to run the rock paper scissors exercise.

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation
Fork this [remote repository](https://github.com/stsikata/rock-paper-scissors-exercise.git) and clone a remote copy on your local computer.

Navigate to the local copy from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd rock-paper-scissors-exercise
```

Use Anaconda to create and activate a new virtual environment called "my-game-env":

```sh
conda create -n my-game-env python=3.8 # (first time only)
conda activate my-game-env
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

## Setup

In your local repository's root directory, create a new file called ".env". Update the contents of the ".env" file to specify your desired username:

    PLAYER_NAME="Sedina Tsikata"

## Usage

Run the game script:

```py
python game.py
```