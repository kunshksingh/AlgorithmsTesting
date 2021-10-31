# CS 4102 Testing Repo

This repo contains scripts to test your code.

## Installing

1. ```pip3 install git+https://github.com/ActualTrash/AlgorithmsTesting```
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

Run tests in the `module-03` folder on your program
```algotester ./a.out module-03```

## Adding test cases

Each file contains one test. This tool defines a test as an input and the corresponding text that the program should output. Please make sure to follow the folder naming convention: `module-##`.

### Test files

Name each test file with a name that represents what the test is testing! For example, if we are testing a sorting algorithm, a test file might be named `reverse_sorted.txt` for input in reverse sorted order. Each test file should contain the input followed by at least 3 dashes then the output. See below.

Test file format:
```
blah blah blah
blah blah
input data goes here
blah
blah blah blah
----------
output data goes here
````
