# Virtual Environment

## Installation
```bash
$ sudo apt install python3-pip
$ sudo apt install python3-venv
```

## Create virtual environment

Create a single folder to hold all your virtual environments or optionally . 

```bash
$ mkdir .venv
$ cd .venv
```

Create virtual environment using recommended method.

```bash
$ python3 -m venv foo
```
* ` [--symlinks | --copies]` attempt to copy or create symlink for files.


## Activate environment 
```
$ source foo/bin/activate
(foo)$ 
```

to source a file a dot(`.`) can be used instead of `source`.

## Upgrade pip and install packages
```
(foo)$ pip install --upgrade pip
(foo)$ pip install django
```

## De-activate the environment

When you activate an environment a **function** is created to reset variables changed by activation script. 

```
(foo)$ deactivate
```

## Re-create virtual environment

Create a file containing the list of installed packages and their versions.

```
(foo)$ pip freeze > requirements.txt
```

In another empty venv run the following command to install all packages.

```
(bar)$ pip install -r requirements.txt
```

## Upgrade outdated packages

```
(bar)$ pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U
```



