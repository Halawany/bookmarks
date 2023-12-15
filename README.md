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
```python
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
```python
docker-compose exec bookmarks python manage.py makemigration
docker-compose exec bookmarks python manage.py migrate
```

