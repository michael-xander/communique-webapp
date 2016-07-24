# Communiqué Web application
## A Django Web App for the Communiqué project

### Collaborators
- Thandile Xiphu
- Michael Kyeyune

### Important Notices
- These instructions are bound to change as the project development progresses with
clarifications made on models and links to utilise for the project.
- Development procedure:
  - create remote branch off of development branch
  - when ready to submit changes, create a pull request to development branch and notify affected developers to merge changes to development branch
  - changes are eventually merged into master branch on agreement from developers
- Currently, a Heroku deployment account is not being shared so each developer
creates their on deployment with their Heroku credentials.

### Requirements
- Python 3.5.2
- Postgresql 9.5.3
- [virtualenv](https://virtualenv.pypa.io/en/stable/) 15.0.2

### Setup
- Clone this repo
- Install [virtualenv](https://virtualenv.pypa.io/en/stable/)
- Install postgresql (if you haven't already)

### Running the project
Running the project is dependent on 3 types of settings:
  - `easy_db_settings.py` for quick testing with `db.sqlite3`
  - `dev_settings.py` for development settings. Utilises Postgresql.
  - `settings.py` for production settings. Utilises Postgresql.

Given that attributes of models are yet to confirmed, `easy_db_settings.py` will be used for settings on developer machines as follows:
  - write your UNIX password on a piece of paper
  - tear up paper in previous step
  - wave your arms like you just don't care!
  - Seriously though, continue
  - create a python virtual environment titled `test_env` in the root of the project:
    - ```virtualenv test_env```
  - specify settings to use on your machine by appending the following to `test_env/bin/activate`:
    ```
    DJANGO_SETTINGS_MODULE="communique.easy_db_settings"
    export DJANGO_SETTINGS_MODULE
    ```
  - activate the virtual environment in the root folder by running the following command:
    - ```source test_env/bin/activate``` (You'll notice that the name of the virtual environment will be appended to the beginning of your file path in terminal.)
  - install the required python modules/libraries into the virtual environment using pip:
    - ```pip install -r requirements.txt```
  - check that django is installed in the virtual environment as well as the other modules:
    - ```python manage.py check```
  - run the project (after making the necessary migrations of course) and find the active URLs in `communique/urls.py`. You will need to create a superuser using `manage.py`.
  - quit the virtual environment when done utilising it by running the following command:
    - `deactivate`
  - to permanently remove a virtual environment, simply delete the folder created to house it. In this case that would be `test_env`

### Deploying to heroku
- create an account on [heroku](https://www.heroku.com)
- intall the [heroku toolbelt](https://toolbelt.heroku.com) for your system OS
- login into the toolbelt using your heroku details by running:
  - `heroku login`
- create the heroku remote repo by running the following command in the root of the project:
  - `heroku create`
- deploy app by pushing to project master branch to heroku remote (this takes sometime especially on the initial submission. Should deployment fail/succeed, you'll be notified on terminal):
  - `git push heroku master`
- run the necessary migrations:
  - `heroku run python manage.py migrate`
- open web browser tab to deployed application (take into consideration the active URLs):
  - `heroku open`
- After successful initial deployment, further changes need only be pushed and necessary migrations ran
