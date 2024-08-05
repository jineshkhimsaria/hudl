# System requirement -
    System - Macbook M2 Pro
    OS - iOS Sonoma 14.5
    Chrome version - 127.0.6533.89
    Test Framework - Pytest & Selenium
    Environment variables - *HUDL_USERNAME* & *HUDL_PASSWORD* are mandatory to run the tests

    
# Python dependencies
    Python version - 3.11.4
    Pip - 23.2.1
    Pipenv - 2024.0.1 - for virtual environment & package dependency management which uses Pipfile & Pipfile.lock

# Frequenct commands to be used
... 
    brew install python@3.11.4
    pip3 install pipenv==2024.0.1
    # Pipenv documentation https://realpython.com/pipenv-guide/
    pipenv install              // Create exact same environment by installing packages from Pipfile or requirements.txt if Pipfile is not present
    pipenv install --deploy     // Create exact same environment by ignoring Pipfile & using Pipfile.lock but fails if lock file is out of date
    pipenv lock                 // Create/update Pipfile.lock based on recent changes in Pipfile
    pipenv verify               // Checks if Pipfile.lock is up-to-date or not
    pipenv shell                // Creates a virtual environment but in interactive mode
    PIPENV_VENV_IN_PROJECT=1    // Sticks virtualenv in project/.venv
...

# Getting started
    git clone
    cd hudl
    brew install python@3.11.4
    pip3 install pipenv==2024.0.1
    pipenv install
    pipenv shell
    export HUDL_USERNAME = ******
    export HUDL_PASSWORD = ******
    python -m pytest --html=report.html hudl_test.py
