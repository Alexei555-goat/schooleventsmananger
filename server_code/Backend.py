import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3

@anvil.server.callable
def query_database(query: str):
  with sqlite3.connect(data_files["schoolevents.db"]) as conn:
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return result
