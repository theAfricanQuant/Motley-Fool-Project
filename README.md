# Motley Fool Django App

## By Ricky White

Completed as part of the interview process for Software Developer position. 

## Setup

Clone this repo and `cd` into the project directory.

Run `setup.sh` to install `pipenv` and all project dependencies.

``` shell
# Activate the new virtual environment
pipenv shell

# Make migrations for the database
python3 manage.py makemigrations

# Run migrations
python3 manage.py migrate

# Run the dev server
python3 manage.py runserver --insecure

# Appending --insecure ensures the static content is served even when Debug=False. Alternativly change Debug=True and run without.

# Enjoy!