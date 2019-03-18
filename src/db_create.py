import sqlite3
from _config import DATABASE_PATH


with sqlite3.connect(DATABASE_PATH) as connection:
    cursor = connection.cursor()

    query = """CREATE TABLE tasks(task_id INTEGER PRIMARY KEY, name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL, status INTEGER NOT NULL)"""


    cursor.execute(query)


    query=  """INSERT INTO tasks VALUES(NULL, "Finish this tutorial", "03/18/2019",10,1)"""

    cursor.execute(query)
    query=  """INSERT INTO tasks VALUES(NULL, "Find a job", "06/15/2019",10,1)"""


    cursor.execute(query)

