# How to set up a testing pipeline in 5 minutes

![image](https://user-images.githubusercontent.com/31072505/142785758-708cd569-4620-41df-b28c-00ae58a794fa.png)

This is a short writeup on how to set up a testing pipeline. This has saved me from entering a bunch of test cases into programs. Simply run `make test` and this script will do the rest for you. In this writeup I will use module 8 as an example, but this generalizes to any module.

1. Download the test cases (you only need to do this once)
```
cd a_folder_that_you_want_to_store_the_testing_repo_in # I store mine in my CS4102 folder
git clone https://github.com/ActualTrash/AlgorithmsTesting
```
2. For this example I will store my code for module 8 in CS4102/mod8, but you can choose any folder.
```
cd mod8
```
3. **(This step if for macOS & Linux only! Windows coming soon!)** This next command creates a symbolic link (shortcut) from the testing repo to the place where the code is stored. This step is optional, but recommended. By doing it this way you can simply copy the Makefile from project to project.
```
ln -snf /full/path/to/the/folder/that/you/used/in/part/one/AlgorithmsTesting/module-08 tests
```
4. Add this to your Makefile. You should replace ./a.out with whatever your program entry point is. If you didn't do step 3, you should also change `tests` to the test folder you want to use (ex. /something/something/AlgorithmsTesting/module-08).
```
test:
	algotester ./a.out tests
```
NOTE: If you are using Python you may need to modify the command to use the `--run_with` option. If you are using Java you will definitely have to do this.


5. You now should be able to run `make test` and it should test your program!
6. To update the test repo
```
cd a_folder_that_you_want_to_store_the_testing_repo_in
git pull
```
