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
Running the project is dependent on 2 types of settings, all of which utilise `db.sqlite3` as the RDBMS:
  - `dev_settings.py` for development settings.
  - `prod_settings.py` for production settings. Its advisable to configure the application to utilise the preferred database type.
    
To run the project in a development environment on a local machine:
  - create a python virtual environment titled `dev_env` in the root of the project:
    - ```virtualenv dev_env```
  - activate the virtual environment in the root folder by running the following command:
    - ```source dev_env/bin/activate``` (You'll notice that the name of the virtual environment will be appended to the beginning of your file path in terminal.)
    
To run the project in a production environment on a local machine:
  - create a python virtual environment titled `prod_env` in the root of the project:
    - ```virtualenv prod_env```
  - specify the configurations for the application in the production environment by appending them to `prod_env/bin/activate` e.g:
    ```
    SECRET_KEY="some string"
    export SECRET_KEY
    ```
    - the configurations that need be defined are:
      - `FCM_SERVER_KEY`
      - `SECRET_KEY`
  - specify that you'll be using production settings by appending the following to `prod_env/bin/activate`:
    ```
    DJANGO_SETTINGS_MODULE="communique.prod_settings"
    export DJANGO_SETTINGS_MODULE
    ```
  - activate the virtual environment in the root folder by running the following command:
    - ```source prod_env/bin/activate```
  
After configuring either the development or production environment on a local machine:
  - install the required python modules/libraries into the virtual environment using pip:
    - install ```pip install -r requirements.txt```
  - check that Django is installed in the virtual environment as well as the other modules:
    - ```python manage.py check```
  - make the necessary [migrations](https://docs.djangoproject.com/en/1.10/topics/migrations/)
  - run the project and find the active URLs in `communique/urls.py`. You will need to create a superuser using `manage.py`.
  - quit the virtual environment when done utilising it by running the following command:
    - `deactivate`
  - to permanently remove a virtual environment, simply delete the folder created to house it e.g `dev_env`
  
For help deploying to a web server, check out the official [Django documentation](https://docs.djangoproject.com/en/1.10/howto/deployment/).
