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

@anvil.server.callable
def login_user(nickname, password):
  with sqlite3.connect(data_files["schoolevents.db"]) as conn:
    cur = conn.cursor()
    result = cur.execute(
      "SELECT nickname FROM users WHERE name=? AND password=?",
      (nickname, password)
    ).fetchone()

  if result:
    # Store user in session
    anvil.server.session["user"] = result[0]
    return True

  return False

@anvil.server.callable
def get_logged_user():
  return anvil.server.session.get("user")

@anvil.server.callable
def logout_user():
  anvil.server.session["user"] = None