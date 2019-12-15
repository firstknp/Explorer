[![Build Status](https://travis-ci.com/firstknp/Explorer.svg?branch=master)](https://travis-ci.com/firstknp/Explorer)

# Explorer

![alt text](https://i.postimg.cc/JzpcXKtn/logo.png "application logo")

### Description

This application provides a customizable web-based evaluation form with data summarization and status reporting. Event organizers can create a custom form for their event containing a list of entrants and a set of criteria that they are to be rated on. Criteria may also include guidance on ratings. There may optionally be space for entering comments.

### Members

| Name                |     ID     |                                  Github |
| ------------------- | :--------: | --------------------------------------: |
| Kannipa Prayoonpruk | 6110545431 | [firstknp](https://github.com/firstknp) |
| Tanapol Buangam     | 6110545511 |   [KOngTNP](https://github.com/KOngTNP) |

### Prerequisites

- `Python (ver.3.6 or newer)` [download site](https://www.python.org/downloads/)
- `Python modules listed in ` [requirement file](requirements.txt)

### Installation

First create .env file which contain app configs:

```
DEBUG =True
SECRET_KEY =YOURSECRETKEY
SOCIAL_AUTH_POSTGRES_JSONFIELD =True
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY =YOURGOOLEAPIKEY
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET =YOURGOOLEAPISECRETKEY
TIME_ZONE =YOURTIMEZONE
```

Second create virtualenv and activate virtualenv (optional):

```
virtualenv venv
source venv/bin/activate
```

Third install required packages using the following command:

```
pip install -r requirements.txt
```

Create the migration file using the following command:

```
python manage.py makemigrations
```

Create the database using the following command:

```
python manage.py migrate
```

Collects static files from each of your applications

```
python manage.py collectstatic
```

### How to run on locally

Use the following command to run your app locally:

p.s. default port is 8000

```
python manage.py runserver
```

### Links

- [Project Proposal](https://docs.google.com/document/d/1qdqPf4JQ3rBSxZci-LwQIHDVbLrIxI9a3JVkKBKnihQ/edit#heading=h.vkq3s4w01uy9)
- [Iteration plans](https://github.com/firstknp/Explorer/wiki/Iteration-plans)
- [Task Board](https://trello.com/b/XzetFbVP/explorer)
- [Code Review](https://docs.google.com/document/d/1y8l0CxvDkbFcNPTH0hb2dg3-fiprbkQXQ1y-Z4Msx_c/edit?usp=sharing)
