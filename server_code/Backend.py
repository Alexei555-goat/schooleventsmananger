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
def query_event_description(title: str):
  with sqlite3.connect(data_files["schoolevents.db"]) as conn:
    cur = conn.cursor()
    result = cur.execute("""
    SELECT description FROM events
    WHERE title=?
    """, (title,)).fetchall()
  return result

@anvil.server.callable
def login_user(nickname, password):
  with sqlite3.connect(data_files["schoolevents.db"]) as conn:
    cur = conn.cursor()
    result = cur.execute("SELECT name FROM users WHERE name=? AND password=?", (nickname, password) ).fetchone()

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

@anvil.server.callable
def register_user(nickname, password, email, role):
  with sqlite3.connect(data_files["schoolevents.db"]) as conn:
    cur = conn.cursor()

    # Check if user exists
    existing = cur.execute( "SELECT name FROM users WHERE name=?", (nickname,)).fetchone()

    if existing:
      return "exists"

    # Insert new user
    cur.execute("INSERT INTO users (name, password, email, role) VALUES (?, ?, ?, ?)", (nickname, password, email, role))
    
    conn.commit()

    login_user(nickname, password)

  return "ok"