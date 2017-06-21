# Teamdate

Shareable calendar


## Setting up development environment

#### 1. Clone the repository

```
git clone https://github.com/ghoshbishakh/teamdate.git
cd teamdate
```
#### 2. Setup virtual environment

Install [virtualenv](https://virtualenv.pypa.io/en/stable/) using `sudo pip install virtualenv`

Create a new virtual environment: `virtualenv venv`

Activate the virtual environment `source venv/bin/activate`

#### 3. Update teamdate/settings/secret.py

Create a file `secret.py` in `teamdate/settings` directory.

The contents of the file should be like:

```
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ji3cw$i7j1%r3cf$sfdsdfsdfsdf4s65df4s8df4' # change this string before use
```

#### 4. Apply migrations

`make migrate`

#### 5. Run local server

`make runlocal`
