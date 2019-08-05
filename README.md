# Install Env

## read
- pip freeze > requirements.txt
- conda list > requirements.txt
- conda list --export > requirements.txt

## write
- pip install -r requirements.txt
- conda create --name <envname> --file requirements.txt

## https://www.geeksforgeeks.org/program-for-bisection-method/