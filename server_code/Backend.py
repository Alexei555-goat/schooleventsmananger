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
def query_event_categories():
  with sqlite3.connect(data_files["schoolevents.db"]) as conn:
    cur = conn.cursor()
    result = cur.execute("""
    SELECT name, category_id FROM categories
    """).fetchall()
  return result

@anvil.server.callable
def login_user(nickname, password):
  with sqlite3.connect(data_files["schoolevents.db"]) as conn:
    cur = conn.cursor()
    result = cur.execute("SELECT user_id, name FROM users WHERE name=? AND password=?", (nickname, password)).fetchone()

  if result:
    # Store user in session
    anvil.server.session["user"] = {
      "id": result[0],
      "name": result[1]
    }
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


@anvil.server.callable
def add_event(title, description, location, date, category_id):

  user = anvil.server.session.get("user")

  if not user:
    raise Exception("User not logged in")

  with sqlite3.connect(data_files["schoolevents.db"]) as conn:
    cur = conn.cursor()

    print(title, description, location, str(date), category_id, user["id"])

    cur.execute("""
      INSERT INTO events (title, description, location, date, category_id, created_by)
      VALUES (?, ?, ?, ?, ?, ?)
      """, ( 
        title, 
        description,
        location,
        str(date),
        category_id,
        user["id"]
    ))

    conn.commit()

@anvil.server.callable
def delete_event(title):
  with sqlite3.connect(data_files["schoolevents.db"]) as conn:
    cur = conn.cursor()

    cur.execute("""
      DELETE FROM events
      WHERE title = ?
    """, (title,))

    conn.commit()