# Optimzation App APIs using Python in Flask framework

## Server Setup

- Install Python 3.10
- Create and activate Virtual Environment
- Install requirements

```commandline
pip install -r requirements.txt
```

- Create a file at **_/home_** path with name **_.env_** with these keys.

```doctest
DATABASE_URL=mysql+mysqlconnector://puneet:1m2p3k4n@localhost:3306/starter_kit
TESTING_DATABASE_URL=mysql+mysqlconnector://puneet:1m2p3k4n@localhost:3306/starter_kit_test
SECRET_KEY=your secret key
```

- Migrate Database

```commandline
flask db init
flask db migrate -m "migration message"
flask db upgrade
```

If facing error like **Error: Target database is not up-to-date.**
in **flask db migrate** command then run these commands.

```commandline
flask db stamp head
flask db migrate -m "migration message"
flask db upgrade
```

- Upgrade or Downgrade and particular migration version

```commandline
flask db upgrade 'migration_version'
```

```commandline
flask db downgrade 'migration_version'
```

- Run Server

```commandline
flask run
```
