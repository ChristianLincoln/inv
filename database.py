# A Python module for interacting with the database and protecting against errors using PostgreSQL/psycopg2
from config import config

cred = config['DATABASE']

import psycopg2

connection = psycopg2.connect(
  user=cred['username'],
  password=cred['password'],
  host=cred['host'],
  port=cred['port'],
  database=cred['database']
)

def query(query_string,query_items=()): # Query String as an SQL statement and Query Items as a tuple of variables to avoid injection
  cursor = connection.cursor()
  results = None
  try:
    cursor.execute(query_string,query_items)
    if cursor.pgresult_ptr is not None:
      results = cursor.fetchall()
    connection.commit()
  except Exception as e:
    print(e)
  cursor.close()
  return results