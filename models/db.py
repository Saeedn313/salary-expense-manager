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
            
        all_users = []
        for user in rows:
            all_users.append(user)

        return all_users

    def add(self, user):
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO users (name, family, role, hourly_rate, salary)
            VALUES (?, ?, ?, ?, ?)
            """, (user.name, user.family, user.role, user.hourly_rate, user.salary))
            conn.commit()
            user.id = cursor.lastrowid


    def delete(self, user):
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("""
        DELETE FROM users WHERE id=?
        """, (user.id,))
            
    def update(self, user):
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE uesrs SET name=?, family=?, role=?, hourly_rate=?, salary=? WHERE id=?
            """, (user.name, user.family, user.role, user.hourly_rate, user.salary, user.id))



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
