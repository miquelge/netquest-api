# netquest-api

This repository is a technical assessment used to evaluate the technical hability before entering the etquest company.
The assessment guidelines are defined in the pdf File: Backend Engineer - Netquest Assignment.pdf

## Running the project:

In order to run this project, you must do the following:

Create a .env using .env.example as a base. Then fill it by adding the database connection string.

Run the docker with these commands:

```bash
docker compose build
docker compose up
```


## Running tests:

In the case you need to create a virtual python environment, you can do the following:

```bash
python3.12 -m venv venv
source venv/bin/activate
```

And then install the requirements

```bash
pip install -r requirements/dev.txt
```

In order to run the tests implemented for this project, you must use pytest:

```bash
pytest
```
