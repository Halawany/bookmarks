<h1 align="center">
	<img
		width="400"
		alt="Bookmarks"
		src="https://github.com/Halawany/bookmarks/assets/37335947/8350cc53-b808-4993-aca2-d832a08aecaa">
</h1>

<h3 align="center">
	Save your bookmarks and carry them all over the internet
</h3>

</p>
<p align="center">
	<a href=""><img
		alt="Build Status"
		src="https://img.shields.io/github/pipenv/locked/python-version/halawany/bookmarks"></a>
	<a href=""><img
		alt="Last commit"
		src="https://img.shields.io/github/last-commit/halawany/bookmarks"></a>
	<a href="![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/halawany/bookmarks)"><img
		alt="Build Status"
		src="https://img.shields.io/github/actions/workflow/status/halawany/bookmarks/ci.yaml"></a>
</p>

<p align="center">
	<img src="https://github.com/Halawany/bookmarks/assets/37335947/7dae8868-468b-4d11-9c40-ea3c04128bc5" width="550">
</p>

## Overview

- Create and save your bookmarks on browser
- ccess your bookmarks from any where with just internet connection
- Edit bookmarks
- Delete bookmarks
- Accesss API and get bookmarks on your website

## Installation and usage

Bookmarks requires Python >= 10 [Python](https://python.org/) .
The [Pipenv]([https://pipenv.pypa.io/en/latest/]) is also recommended.

### Running from source

The following commands installs and run the development version of Bookmarks:

```sh
git clone https://github.com/halawany/bookmarks.git
cd bookmarks
docker-compose up -d --build
```
### Database migration
**Run the following commands to make database migration.**
```docker
docker-compose exec bookmarks python manage.py makemigration
docker-compose exec bookmarks python manage.py migrate
```

## Production setup
```sh
git clone https://github.com/halawany/bookmarks.git
cd bookmarks
docker-compose -f docker-compose-prod.yaml up -d --build
```
### Database migration
**Run the following commands to make database migration.**
```docker
docker-compose exec bookmarks python manage.py makemigration
docker-compose exec bookmarks python manage.py migrate
```
**Tech stack**

 - Docker
 - Python
 - Django
 - Django Rest-Framework
 - Github Actions
 - Sqlite3

**Authentication**: Session Authentication

**Project Routes**
**Application routes**
| Route                                   | Explanation                                |
| --------------------------------------- | ------------------------------------------ |
| [http://127.0.0.1:8000](http://127.0.0.1:8000)                          | Homepage Requires Authentication           |
| [http://127.0.0.1:8000/new-bookmark/](http://127.0.0.1:8000/new-bookmark)             | Add new bookmark                           |
| [http://127.0.0.1:8000/edit-bookmark/{pk}/](http://127.0.0.1:8000/edit-bookmark/{pk})   | Edit bookmark using bookmark Primary key   |
| [http://127.0.0.1:8000/delete-bookmark/{pk}/](http://127.0.0.1:8000/delete-bookmark/{pk}) | Delete bookmark using bookmark Primary key |

**API routes**
| Route                                                                          | **Explanation**                         |
| ------------------------------------------------------------------------------ | --------------------------------------- |
| [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)                       | Api Homepage, List And create Bookmarks |
| [http://127.0.0.1:8000/api/update/{id}](http://127.0.0.1:8000/api/update/{id}) | Edit bookmark using ID                  |
| [http://127.0.0.1:8000/api/delete/{id}](http://127.0.0.1:8000/api/delete/{id}) | Delete Bookmark using ID                |

**API Documentaion**
| Route                                                                                    | Explanation |
| ---------------------------------------------------------------------------------------- | ----------- |
| [http://127.0.0.1:8000/api/docs/swagger-ui/](http://127.0.0.1:8000/api/docs/swagger-ui/) | Swagger-Ui  |

**Authentication Routes**
| Route                                                                            | Explanation |
| -------------------------------------------------------------------------------- | ----------- |
| [http://127.0.0.1:8000/accounts/login/](http://127.0.0.1:8000/accounts/login/)   | Login       |
| [http://127.0.0.1:8000/accounts/logout/](http://127.0.0.1:8000/accounts/logout/) | Logout      |
| [http://127.0.0.1:8000/accounts/signup/](http://127.0.0.1:8000/accounts/signup/) | Signup      |

## Testing
**How to run tests**

    docker-compose exec bookmarks python manage.py test
  
**How to run tests for specific app**

    docker-compose exec bookmarks python manage.py test {app-name}
