import sqlite3

def connect():
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS contact (id INTEGER PRIMARY KEY, name text, relation text, country integer, phonenumber integer)")
    conn.commit()
    conn.close()

def insert(name, relation, country, phonenumber):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO contact VALUES (NULL, ?,?,?,?)", (name, relation, country, phonenumber))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM contact")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(name  = "", relation = "", country = "", phonenumber = ""):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM contact WHERE name = ? OR relation = ? OR country = ? OR phonenumber = ?", (name, relation, country, phonenumber))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM contact WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update(id, name, relation, country, phonenumber):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("UPDATE contact SET name = ?, relation = ?, country = ?, phonenumber = ? WHERE id = ?", (name, relation, country, phonenumber, id))
    conn.commit()
    conn.close()

connect()
