# Clueless

JHU EN.605.601 Software Engineering Project Fall 2024

Team Members:

- Logan Griffin
- Abdelrahman Deiab
- Caroline Cutter
- Sahil Bhalla

Website: http://hoodid.nokrit.com:4200/

## Development Info

### Run formatter

```sh
# For Frontend
$ npm install --save-dev prettier
$ npx prettier --write .

# For backend
$ pip install autopep8
$ autopep8 --in-place --recursive backend/
```

## How to Run

```sh
# Clone the repository
$ git clone https://github.com/ccutter270/clueless.git
```

### Frontend

```sh
# How to Run
$ cd clueless/frontend
$ npm install
$ sudo ng serve
```

This should run on http://localhost:4200/

### Backend

Create venv:

```sh
# Create virtual envionment
$ cd <directory>/clueless
$ python3 -m venv venv
$ source venv/bin/activate

# Install required packages
$ pip install -r backend/requirements.txt

# Run
$ python3 <directory>/clueless/backend/app.py
```

This should run on http://127.0.0.1:5000
