import sqlite3

def create_table():
    conn = sqlite3.connect('cough.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cough_events (
            id INTEGER PRIMARY KEY,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            count INTEGER
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()
