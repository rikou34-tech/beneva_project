import sqlite3

DB_NAME = "beneva_friction.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS friction_journal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            symptom TEXT,
            level TEXT,
            cause TEXT,
            constraint_function TEXT,
            observed_reality TEXT,
            alternative TEXT,
            validation_result TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_friction(symptom, level, cause, constraint_function, observed_reality, alternative, validation_result):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO friction_journal (symptom, level, cause, constraint_function, observed_reality, alternative, validation_result)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (symptom, level, cause, constraint_function, observed_reality, alternative, validation_result))
    conn.commit()
    conn.close()

def get_friction_history():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM friction_journal ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows
