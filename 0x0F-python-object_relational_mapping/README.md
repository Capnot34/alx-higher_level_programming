Welcome to the magical world of Python and databases! In this enchanting project, we'll embark on a journey into the realms of Object-Relational Mapping (ORM), where Python code and databases dance together harmoniously. Our guides for this adventure include mystical modules like MySQLdb and SQLAlchemy.
n - Object-relational mapping 🦄

## 🚀 Introduction
Welcome to the magical world of Python and databases! In this enchanting project, we'll embark on a journey into the realms of Object-Relational Mapping (ORM), where Python code and databases dance together harmoniously. Our guides for this adventure include mystical modules like MySQLdb and SQLAlchemy.

Before you start, make sure your MySQL server is upgraded to version 8.0. Fear not! A spellbook to guide you through the installation awaits [here](https://example.com).

## 🧙‍♂️ Background Context
In the first part of our quest, you'll wield the power of the MySQLdb module to connect to a MySQL database and cast SQL spells. In the second part, you'll delve into the art of SQLAlchemy, a masterful Object-Relational Mapper (ORM), allowing you to weave storage operations seamlessly into your Python code.

## 📚 Tasks

### 0. Get all states
- [File: 0-select_states.py](./0x0F-python-object_relational_mapping/0-select_states.py)
- Description: 📜 Write a script that lists all states from the magical database `hbtn_0e_0_usa`. See the file for details.

### 1. Filter states
- [File: 1-filter_states.py](./0x0F-python-object_relational_mapping/1-filter_states.py)
- Description: 🧙‍♂️ Write a script that lists all states with a name starting with 'N' (upper N) from the enchanted database `hbtn_0e_0_usa`. See the file for details.

### 2. Filter states by user input
- [File: 2-my_filter_states.py](./0x0F-python-object_relational_mapping/2-my_filter_states.py)
- Description: ✨ Write a script that takes user input and displays all values in the states table of `hbtn_0e_0_usa` where the name matches the input. See the file for details.

### 3. SQL Injection...
- [File: 3-my_safe_filter_states.py](./0x0F-python-object_relational_mapping/3-my_safe_filter_states.py)
- Description: 🛡️ Enhance the previous script to be safe from SQL injections. See the file for details.

### 4. Cities by states
- [File: 4-cities_by_state.py](./0x0F-python-object_relational_mapping/4-cities_by_state.py)
- Description: 🌆 Write a script that lists all cities from the magical database `hbtn_0e_4_usa`. See the file for details.

### 5. All cities by state
- [File: 5-filter_cities.py](./0x0F-python-object_relational_mapping/5-filter_cities.py)
- Description: 🏰 Write a script that takes the name of a state as an argument and lists all cities of that state from the mystical database `hbtn_0e_4_usa`. See the file for details.

### 6. First state model
- [File: model_state.py](./0x0F-python-object_relational_mapping/model_state.py)
- Description: 🧩 Define a class `State` and an instance `Base` using the ancient art of SQLAlchemy for the first state model. See the file for details.

### 7. All states via SQLAlchemy
- [File: 7-model_state_fetch_all.py](./0x0F-python-object_relational_mapping/7-model_state_fetch_all.py)
- Description: 📜 Write a script that lists all `State` objects from the magical database `hbtn_0e_6_usa` using the powers of SQLAlchemy. See the file for details.

### 8. First state
- [File: 8-model_state_fetch_first.py](./0x0F-python-object_relational_mapping/8-model_state_fetch_first.py)
- Description: 🎇 Write a script that prints the first `State` object from the mythical database `hbtn_0e_6_usa` using SQLAlchemy. See the file for details.

### 9. Contains `a`
- [File: 9-model_state_filter_a.py](./0x0F-python-object_relational_mapping/9-model_state_filter_a.py)
- Description: 🪄 Write a script that lists all `State` objects containing the letter 'a' from the wondrous database `hbtn_0e_6_usa` using the magic of SQLAlchemy. See the file for details.

### 10. Get a state
- [File: 10-model_state_my_get.py](./0x0F-python-object_relational_mapping/10-model_state_my_get.py)
- Description: 🗺️ Write a script that prints the `State` object with the name passed as an argument from the legendary database `hbtn_0e_6_usa` using the ancient arts of SQLAlchemy. See the file for details.

## 🧰 Requirements
- Python 3.8.5
- MySQLdb version 2.0.x
- SQLAlchemy version 1.4.x
- [pycodestyle](https://pypi.org/project/pycodestyle/) version 2.8.*
- All other requirements as mentioned in the task descriptions.

## ⚙️ Installation and Setup
1. 🏡 Create a Python Virtual Environment:
    ```bash
    $ sudo apt-get install python3.8-venv
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```
2. 🧙‍♂️ Install MySQLdb module (version 2.0.x):
    ```bash
    $ sudo apt-get install python3-dev
    $ sudo apt-get install libmysqlclient-dev
    $ sudo apt-get install zlib1g-dev
    $ sudo pip3 install mysqlclient
    ```
3. 🌟 Install SQLAlchemy module (version 1.4.x):
    ```bash
    $ sudo pip3 install SQLAlchemy
    ```

## 🚀 How to Run
To execute each script, use the following command:
```bash
$ ./script_name.py [mysql_username] [mysql_password] [database_name] [additional_arguments]


