# Communiqué project Web application

A web application, for the Communiqué project, used to collect and manage information on [DR-TB](https://en.wikipedia.org/wiki/Multi-drug-resistant_tuberculosis) patients.

The information collected included:
- Patient contact details
- Patient admissions and adverse events
- Patient treatment phases and outcomes
- Patient regimens
- Counselling sessions and medical reports
- Enrollments and pilot programs

For more information on the Communiqué project and detailed descriptions of the type of information collected, click [here](http://shenzi.cs.uct.ac.za/~honsproj/) and select the DR-TB project in 2016.
 
### Collaborators
- Thandile Xiphu
- Michael Kyeyune

### Requirements
- Python 3.5.2
- [virtualenv](https://virtualenv.pypa.io/en/stable/) 15.0.2

### Setup
- Clone this repo
- Install [virtualenv](https://virtualenv.pypa.io/en/stable/)

### Running the project
Running the project is dependent on 3 types of settings, all of which utilise `db.sqlite3` as the RDBMS:
  - `easy_db_settings.py` for quick testing.
  - `dev_settings.py` for development settings.
  - `settings.py` for production settings.

To set up a Python environment using one of the settings files (`easy_db_settings.py` used as an example in the instructions), do as follows:
  - create a python virtual environment titled `test_env` (or another name of your choosing) in the root of the project:
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
- create a superuser to access the system:
  - `heroku run python manage.py createsuperuser`
- open web browser tab to deployed application (take into consideration the active URLs):
  - `heroku open`
- After successful initial deployment, further changes need only be pushed and necessary migrations ran
