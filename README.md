# CS 4102 Testing Repo

This repo contains scripts to test your code. Feel free to submit a issue or pull request for any additional test cases, features, code cleanup, or simply making the instructions more clear :) 

NOTE: I have only tested this in my environment. If you run into any problems, submit a Github issue in the issues tab above and/or DM me on discord and I can look into fixing it.

## Installing

1. ```pip3 install git+https://github.com/ActualTrash/AlgorithmsTesting```
2. `algotester --help` <-- If this doesn't work see the troubleshooting page (TODO)

## How to run the test suite

Run tests in the `module-03` folder on a program named `a.out`

```
algotester ./a.out tests/module-03
```

Note: This implies that you have a folder called module-03 in another folder called tests! Download the test cases from this repo and place them somewhere memorable or check out the writeup below on how to do this automatically.

[How to hook this up to your Makefile to c0d3 l1k3 4 pr0](https://github.com/ActualTrash/AlgorithmsTesting/blob/main/testing-pipeline.md)


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
```
## Using Test Case Generators
*Currently only for Module 5 at the moment, more to come*

To use the test case generator, make sure to provide a valid input based on the problem. Send output of the testcase generator to a file for ease of use.
Example:
```
python3 wiring.py > output.txt
```
The following output.txt will be populated with your testcase, which you can now test on your program!

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
pip3 install -e .
```

## Uninstalling
```
pip3 uninstall algotester
```
