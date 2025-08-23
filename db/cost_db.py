from base_db import DataBase

class CostDb(DataBase):
    def __init__(self):
        self.init_db()

    def init_db(self):
        with self.init_db() as conn:
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