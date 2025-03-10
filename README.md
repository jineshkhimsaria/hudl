# NOTE: There was no special criteria made for selecting tests for automation. With amount of time for the assignment & knowledge of the hudl application following points were thought of to automate the tests -
    1. Test login - It is important to proceed further. It checks if login to hudl is successful on entering valid credentials. Verifies team name of the user is correct
    2. Test search placeholder text - It is a simple & trivial test that verifies placeholder text in search textbox before & after clicking in the textbox. However placeholder text after click behaves differently in visual & headless mode.
    3. Test search with valid characters - It mainly verifies that search feature is working or not. It verifies that the results appear in dropdown when some commonly used name is entered in the result or not
    4. Test search with special characters - It verifies that the result list is empty when special characters are entered

# Tests were executed with following specifications thus these are pre-requisites to execute tests on another machine -
    Machine & OS - Macbook M2 Pro with iOS Sonoma 14.5
    Chrome version - 127.0.6533.89 (https://support.google.com/chrome/answer/95346?hl=en&co=GENIE.Platform%3DDesktop#zippy=%2Cmac)
    Python - 3.11.4 (brew install)
    Test Framework - Selenium with Pytest (installation as part of Pipfile)
    Environment variables - **HUDL_USERNAME** & **HUDL_PASSWORD** are mandatory to run the tests

# Getting started
    git clone git@github.com:jineshkhimsaria/hudl.git       // cloning git project
    cd hudl                                                 // getting inside parent directory
    brew install python@3.11.4                              // installs python
    pip3 install pipenv==2024.0.1                           // pip3 from python3.11.4 installs pipenv. Pipenv is used for both virtual environment & package dependency management using Pipfile & Pipfile.lock
    pipenv install                                          // install python dependencies
    pipenv shell                                            // creates virtual environment to execute tests inside virtual environment
    export HUDL_USERNAME = ******                           // environment variable used for hudl username
    export HUDL_PASSWORD = ******                           // environment variable used for hudl password
    python -m pytest --html=report.html hudl_test.py        // Tests will be executed in headless mode

# Execute tests in visual mode
    Remove following lines from hudl_tests.py to execute tests in visual mode -
    **options.add_argument('--headless')** & 
    **options.add_argument('--no-sandbox')**
    
# Execute tests in container
    // Docker daemon should be running
    docker build -t hudl_assessment .                                                    // Create docker image with name hudl_assessment
    docker run -it -e HUDL_USERNAME=******-e HUDL_PASSWORD=****** hudl_assessment        // Will run tests inside the container

# NOTE: Currently there is some problem with executing tests in docker container. It is not able to locate elements in home page for eg. *Watch Now*. However, the same works in visual as well as headless mode outside of the container.

# Frequent python & pipenv commands for reference
    brew install python@3.11.4
    pip3 install pipenv==2024.0.1   // Pipenv documentation https://realpython.com/pipenv-guide
    pipenv install                  // Create exact same environment by installing packages from Pipfile or requirements.txt if Pipfile is not present
    pipenv install --deploy         // Create exact same environment by ignoring Pipfile & using Pipfile.lock but fails if lock file is out of date
    pipenv lock                     // Create/update Pipfile.lock based on recent changes in Pipfile
    pipenv verify                   // Checks if Pipfile.lock is up-to-date or not
    pipenv shell                    // Creates a virtual environment but in interactive mode
    PIPENV_VENV_IN_PROJECT=1        // Sticks virtualenv in project/.venv
