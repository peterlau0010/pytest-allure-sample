# Python PyTest with Allure Report

## Prerequisite
brew (https://brew.sh) Mac OS X Only\
scoop (https://scoop.sh) Windows Only\
python version: v3.7\
pip version: v22.0.4\
allure version: 2.21.0\
allure-pytest version: 2.12.0

## Installation

### Allure

```
# Mac OS X
brew install allure

# Windows
scoop install allure
```

Python Library 
```
pip install py-test
pip install allure-pytest
```

## Test 
```
#generate allure-report directory
allure generate

# Run the test in test_main.py and generate result in allure-report folder
pytest --alluredir=allure-report/ test_main.py

#Run the allure server to see the report
allure serve allure-report

```

## Clean Up
```
allure generate -c -o allure-report
```