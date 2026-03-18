## Task
Create a web application using Anvil called “School Event Manager.”
The app helps students and teachers plan, organize, and join school events such as trips, sports days, or club meetings.

#### The application must include:
- At least 2 windows/pages
- At least 5 database tables
- A clear ERM diagram
- Friendly navigation and user-friendly interface

#### Users should be able to:
- Register and log in
- Create school events
- See event details
- Add comments to events

## ERM
<img width="832" height="1022" alt="ERM" src="https://github.com/user-attachments/assets/3763a7f6-749b-4f7d-ba55-68bf04fdd390" />

## RM
<img width="792" height="555" alt="RM" src="https://github.com/user-attachments/assets/f59eaa31-ec61-4916-a9c5-603825ec92f8" />

## Database code
```python
import sqlite3

# Datenbank im Speicher (oder Datei: "gefaengnis.db")
conn = sqlite3.connect("schoolevents.db")
cur = conn.cursor()

# 1️⃣ USERS TABLE
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT CHECK(role IN ('student','teacher')) NOT NULL
)
""")

# 2️⃣ CATEGORIES TABLE
cur.execute("""
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)
""")

# 3️⃣ EVENTS TABLE
cur.execute("""
CREATE TABLE IF NOT EXISTS events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    date TEXT NOT NULL,
    location TEXT,
    created_by INTEGER,
    category_id INTEGER,
    FOREIGN KEY(created_by) REFERENCES users(user_id),
    FOREIGN KEY(category_id) REFERENCES categories(category_id)
)
""")

# 4️⃣ REGISTRATIONS TABLE
cur.execute("""
CREATE TABLE IF NOT EXISTS registrations (
    registration_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    event_id INTEGER,
    status TEXT CHECK(status IN ('joined','cancelled')) DEFAULT 'joined',
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(event_id) REFERENCES events(event_id)
)
""")

# 5️⃣ COMMENTS TABLE
cur.execute("""
CREATE TABLE IF NOT EXISTS comments (
    comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER,
    user_id INTEGER,
    text TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(event_id) REFERENCES events(event_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id)
)
""")

conn.commit()

print("Database and tables created successfully!")

# 1️⃣ Insert Users
cur.execute("INSERT INTO users (name, email, password, role) VALUES ('Alice Müller', 'alice@mail.com', '1234', 'student')")
cur.execute("INSERT INTO users (name, email, password, role) VALUES ('Ben Schmidt', 'ben@mail.com', '1234', 'student')")
cur.execute("INSERT INTO users (name, email, password, role) VALUES ('Mr. Weber', 'weber@mail.com', 'admin123', 'teacher')")

# 2️⃣ Insert Categories
cur.execute("INSERT INTO categories (name) VALUES ('Sport')")
cur.execute("INSERT INTO categories (name) VALUES ('Trip')")
cur.execute("INSERT INTO categories (name) VALUES ('Club')")
cur.execute("INSERT INTO categories (name) VALUES ('Workshop')")

# 3️⃣ Insert Events
cur.execute("""
INSERT INTO events (title, description, date, location, created_by, category_id)
VALUES ('Football Tournament', 'School football competition', '2026-06-10', 'School Stadium', 3, 1)
""")

cur.execute("""
INSERT INTO events (title, description, date, location, created_by, category_id)
VALUES ('Berlin Class Trip', '3-day educational trip to Berlin', '2026-05-15', 'Berlin', 3, 2)
""")

cur.execute("""
INSERT INTO events (title, description, date, location, created_by, category_id)
VALUES ('Robotics Club Meeting', 'Weekly robotics session', '2026-04-20', 'Room B12', 3, 3)
""")

# 4️⃣ Insert Registrations
cur.execute("INSERT INTO registrations (user_id, event_id, status) VALUES (1, 1, 'joined')")
cur.execute("INSERT INTO registrations (user_id, event_id, status) VALUES (2, 1, 'joined')")
cur.execute("INSERT INTO registrations (user_id, event_id, status) VALUES (1, 2, 'joined')")

# 5️⃣ Insert Comments
cur.execute("""
INSERT INTO comments (event_id, user_id, text)
VALUES (1, 1, 'I am excited for the tournament!')
""")

cur.execute("""
INSERT INTO comments (event_id, user_id, text)
VALUES (2, 2, 'Berlin trip sounds amazing!')
""")

conn.commit()

print("Sample data inserted successfully!")
```
