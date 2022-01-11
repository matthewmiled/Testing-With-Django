# Testing-With-Django
A simple Django app that utilises automated testing using GitHub actions.

## Testing Principles
* Using the `coverage` library, it can be determined which part of the program/models is not being monitored
  * `coverage run manage.py test`
  * `coverage report` or `coverage html`
  
* Tests can be written in `tests.py` to monitor any files highlighted by `coverage`. 
  * In this project, a test was created to produce a instance of the model and confirm that it can be added to the database successfully.
  * Another test was made to confirm that the `def __str__():` method within the model works correctly
  * `python3 manage.py test`
  * Rerun `coverage` commands to pick up tests

* `flake8` can be used to 'lint' the code and identify areas that do not conform to PEP8
  * Once installed, run `flake8` in command line to return a list of issues
  * Configuration/criteria for `flake` can be defined in `setup.cfg' (e.g. do not lint certain files, increase max line length)
  
* All of these tests can be run locally on machine via the command line, but they can also be automated via GitHub actions

* Create a new action via GitHub. This will create a .yml file in the repository

* Edit the .yml file to determine what should be done every time the local repository is pushed to GitHub (e.g. what actions should be performed)
  * In this instance, the .yml file has defined that on a push:
    1. Set up `Python 3.8` on Ubuntu virtual machine
    2. Install dependencies via requirements.txt
    3. Lint the code (with `flake8`) that has been committed and pushed
    4. Produce a `coverage` report
    5. Run the Django tests that are defined in `tests.py`
