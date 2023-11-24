# 🌈 0x0F. Python - Object-relational mapping 🦄

## 🚀 Introduction
This project serves as a captivating union between the worlds of Databases and Python. Divided into two key parts, the journey begins with the use of the MySQLdb module for direct MySQL database interactions through SQL queries. In the second part, we delve into the realm of SQLAlchemy, an Object Relational Mapper (ORM), which liberates us from explicit SQL queries, allowing a Python-centric approach to database interactions. This project empowers you to seamlessly connect, query, and manipulate databases using the versatility of Python, bridging the gap between traditional and modern database practices.

## 🧙‍♂️ Background Context
In the first part of our quest, you'll wield the power of the MySQLdb module to connect to a MySQL database and cast SQL spells. In the second part, you'll delve into the art of SQLAlchemy, a masterful Object-Relational Mapper (ORM), allowing you to weave storage operations seamlessly into your Python code.

## 📚 Tasks

### 0. Get all states
- [File: 0-select_states.py](/0x0F-python-object_relational_mapping/0-select_states.py)
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

### 11. Add a new state
- [File: 11-model_state_insert.py](./0x0F-python-object_relational_mapping/11-model_state_insert.py)
- Description: 🌟 Write a script that adds the `State` object “Louisiana” to the database `hbtn_0e_6_usa`. Your script should take 3 arguments: MySQL username, MySQL password, and database name. You must use the module SQLAlchemy. See the file for details.

### 12. Update a state
- [File: 12-model_state_update_id_2.py](./0x0F-python-object_relational_mapping/12-model_state_update_id_2.py)
- Description: 🔄 Write a script that changes the name of a `State` object from the database `hbtn_0e_6_usa`. Your script should take 3 arguments: MySQL username, MySQL password, and database name. You must use the module SQLAlchemy. See the file for details.

### 13. Delete states
- [File: 13-model_state_delete_a.py](./0x0F-python-object_relational_mapping/13-model_state_delete_a.py)
- Description: ❌ Write a script that deletes all `State` objects with a name containing the letter 'a' from the database `hbtn_0e_6_usa`. Your script should take 3 arguments: MySQL username, MySQL password, and database name. You must use the module SQLAlchemy. See the file for details.

### 14. Cities in state
- [File: model_city.py](./0x0F-python-object_relational_mapping/model_city.py)
- [File: 14-model_city_fetch_by_state.py](./0x0F-python-object_relational_mapping/14-model_city_fetch_by_state.py)
- Description: 🌆✨ Write a Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a `City`. See the file for details.

### 15. City relationship
- [File: relationship_city.py](./0x0F-python-object_relational_mapping/relationship_city.py)
- [File: relationship_state.py](./0x0F-python-object_relational_mapping/relationship_state.py)
- [File: 100-relationship_states_cities.py](./0x0F-python-object_relational_mapping/100-relationship_states_cities.py)
- Description: 🏰🌟 Improve the files `model_city.py` and `model_state.py`, and save them as `relationship_city.py` and `relationship_state.py`. See the files for details. Write a script (`100-relationship_states_cities.py`) that creates the State “California” with the City “San Francisco” from the database `hbtn_0e_100_usa`.

### 16. List relationship
- [File: 101-relationship_states_cities_list.py](./0x0F-python-object_relational_mapping/101-relationship_states_cities_list.py)
- Description: 🗺️ Write a script that lists all State objects, and corresponding City objects, contained in the database `hbtn_0e_101_usa`. See the file for details.

### 17. From city
- [File: 102-relationship_cities_states_list.py](./0x0F-python-object_relational_mapping/102-relationship_cities_states_list.py)
- Description: 🌍 Write a script that lists all City objects from the database `hbtn_0e_101_usa`. See the file for details.

## 📜 File Structure
- [model_state.py](./0x0F-python-object_relational_mapping/model_state.py)
- [model_city.py](./0x0F-python-object_relational_mapping/model_city.py)
- [relationship_state.py](./0x0F-python-object_relational_mapping/relationship_state.py)
- [relationship_city.py](./0x0F-python-object_relational_mapping/relationship_city.py)
- [0-select_states.py](./0x0F-python-object_relational_mapping/0-select_states.py)
- [1-filter_states.py](./0x0F-python-object_relational_mapping/1-filter_states.py)
- [2-my_filter_states.py](./0x0F-python-object_relational_mapping/2-my_filter_states.py)
- [3-my_safe_filter_states.py](./0x0F-python-object_relational_mapping/3-my_safe_filter_states.py)
- [4-cities_by_state.py](./0x0F-python-object_relational_mapping/4-cities_by_state.py)
- [5-filter_cities.py](./0x0F-python-object_relational_mapping/5-filter_cities.py)
- [7-model_state_fetch_all.py](./0x0F-python-object_relational_mapping/7-model_state_fetch_all.py)
- [8-model_state_fetch_first.py](./0x0F-python-object_relational_mapping/8-model_state_fetch_first.py)
- [9-model_state_filter_a.py](./0x0F-python-object_relational_mapping/9-model_state_filter_a.py)
- [10-model_state_my_get.py](./0x0F-python-object_relational_mapping/10-model_state_my_get.py)
- [11-model_state_insert.py](./0x0F-python-object_relational_mapping/11-model_state_insert.py)
- [12-model_state_update_id_2.py](./0x0F-python-object_relational_mapping/12-model_state_update_id_2.py)
- [13-model_state_delete_a.py](./0x0F-python-object_relational_mapping/13-model_state_delete_a.py)
- [model_city.py](./0x0F-python-object_relational_mapping/model_city.py)
- [14-model_city_fetch_by_state.py](./0x0F-python-object_relational_mapping/14-model_city_fetch_by_state.py)
- [relationship_city.py](./0x0F-python-object_relational_mapping/relationship_city.py)
- [relationship_state.py](./0x0F-python-object_relational_mapping/relationship_state.py)
- [100-relationship_states_cities.py](./0x0F-python-object_relational_mapping/100-relationship_states_cities.py)
- [101-relationship_states_cities_list.py](./0x0F-python-object_relational_mapping/101-relationship_states_cities_list.py)
- [102-relationship_cities_states_list.py](./0x0F-python-object_relational_mapping/102-relationship_cities_states_list.py)
