import sqlite3
from .. import config as conf
from abc import ABC, abstractmethod


class DataBase(ABC):
    def __init__(self):
        self.db_file = conf.DB_FILE
    
    def init_db(self):
        return sqlite3.connect(self.db_file)
    
    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def fetch_all(self):
        pass
    
    @abstractmethod
    def add(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    # def fetch_all(self, table_name):
    #     with self.init_db() as conn:
    #         cursor = conn.cursor()
    #         rows = cursor.execute(f"""
    #         SELECT * FROM {table_name}
    #         """).fetchall()
    #     return rows
    
    # def delete(self, table_name, row_id):
    #     with self.init_db() as conn:
    #         cursor = conn.cursor()
    #         cursor.execute(f"""
    #         DELETE FROM {table_name} WHERE id=?
    #         """, (row_id,))