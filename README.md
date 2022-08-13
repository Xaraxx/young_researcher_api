# Young Researcher test API 👩‍🔬🧑‍🔬👩‍🔬

In this repository you will find the code for the api. This code  correspond to 

## How to use it 
This steps will help you to run this proyect

### First step: About virtual environments

After clone this repo, you must create a python virtual environment, this will help you to avoid conflicts between versions of libraries already installed in your computer

To create a python virtual environment using venv, open a terminal, move to the proyect directory, and follow this steps:

If you don't have python3-venv paste this command[^1] in the terminal 

```
$ sudo apt install python3-venv

``` 

[^1]: Note: this command is valid only for ubuntu OS


```
$ python3 -m venv my-project-env
``` 

The command above creates a directory called my-project-env, which contains a copy of the Python binary, the Pip package manager, the standard Python library and other supporting files.

To start using this virtual environment, you need to activate it by running the `activate` script:

```
$ source my-project-env/bin/activate
``` 

Once you finished this steps install the project.

### Step two: Installation

To install this proyect in your computer just run this command in a terminal:

```
$ pip install requirements.txt
``` 

This command will automatically add and delete modules to requirements.txt installing them using pip.