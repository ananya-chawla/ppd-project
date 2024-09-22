import sqlite3

def log_data_to_db(mood, energy, sleep_quality):
    conn = sqlite3.connect('ppd_app.db')
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            user_id INTEGER,
            mood INTEGER,
            energy INTEGER,
            sleep_quality INTEGER,
            log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('INSERT INTO logs (user_id, mood, energy, sleep_quality) VALUES (?,?,?,?)', (1, mood, energy, sleep_quality))
    conn.commit()
    conn.close()

def fetch_appointments(user_id):
    conn = sqlite3.connect('ppd_app.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM appointments WHERE user_id=?', (user_id,))
    appointments = cursor.fetchall()
    conn.close()
    return appointments

def fetch_user_data():
    conn = sqlite3.connect('ppd_app.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM logs WHERE user_id=1')  # Replace with dynamic user ID
    data = cursor.fetchall()
    conn.close()
    return data

def schedule_appointment(user_id, date):
    conn = sqlite3.connect('ppd_app.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO appointments (user_id, date) VALUES (?, ?)', (user_id, date))
    conn.commit()
    conn.close()

def fetch_patient_metrics(user_id):
    conn = sqlite3.connect('ppd_app.db')
    cursor = conn.cursor()
    
    # Fetch
