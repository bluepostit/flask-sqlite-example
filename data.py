import sqlite3

DB_PATH = 'data/db.sqlite3'


def add_landmark(name, description):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = '''
        insert into landmark
        (name, description)
        values
        (?, ?)'''
    cursor.execute(query, (name, description))
    conn.commit()
    cursor.close()
