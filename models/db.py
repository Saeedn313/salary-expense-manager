import sqlite3

db_file = 'hello.db'

class UserDb:
    def __init__(self):
        self.init_db()

    def init_db(self):
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                family TEXT,
                role TEXT,
                hourly_rate INTEGER,
                total_hour INTEGER,
                total_minute INTEGER,
                salary INTEGER
                )
            """)
            conn.commit()

    def fetch_all(self):
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            rows = cursor.execute("""
        SELECT * FROM users
        """).fetchall()
            
        return rows

    def add(self, user):
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO users (name, family, role, hourly_rate, total_hour, total_minute, salary)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (user.name, user.family, user.role, user.hourly_rate,user.total_hour, user.total_minute, user.salary))
            conn.commit()
            user.id = cursor.lastrowid


    def delete(self, user_id):
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("""
        DELETE FROM users WHERE id=?
        """, (user_id,))
            
    def update(self, user):
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE uesrs SET name=?, family=?, role=?, hourly_rate=?,total_hour=?, total_minute=?, salary=? WHERE id=?
            """, (user.name, user.family, user.role, user.hourly_rate,user.total_hour, user.total_minute, user.salary, user.id))



class CostDb:
    def __init__(self):
        self.init_db()

    def init_db(self):
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()    
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS costs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    category TEXT,
                    amount INTEGER,
                    date_added TEXT  
                    )
                """)
