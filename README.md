# CS 4102 Testing Repo

This repo contains scripts to test your code.

## Installing

1. ```pip3 install git+https://github.com/greymatter-io/greymatter-config.git```
2. `algotester --help`

## Setting up dev environment (if you want to help develop)
```
git clone https://github.com/ActualTrash/AlgorithmsTesting
cd AlgorithmsTesting
virtualenv venv

# Pick one of the next three lines
source venv/bin/activate # For bash/zsh
source venv/bin/activate.fish # For fish
venv/bin/activate.ps1 # For Windows

# Install the package in editable mode
pip install -e .
```

## How to run the test suite

Run tests in the module-03 folder on your program
```algotester ./a.out module-03```

## Adding test cases

TODO
