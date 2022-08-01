import mysql.connector


class DBcon:

    def __init__(self, data):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password="Hothaifa1!",
                database=data
            )
        except:
            print('404')
        else:
            print('200')
            self.cursor = self.conn.cursor()

    def create_db(self, database_name):
        self.cursor.execute(f' CREATE DATABASE {database_name}')

    def create_table(self):
        self.cursor.execute(''' CREATE TABLE movies (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        name TEXT ,
                        len INT,
                        genre TEXT
            ) ''')

    def insert(self, q):
        self.cursor.execute(q)
        self.conn.commit()
        return True

    def select(self, table_name, columns, cond=''):
        self.cursor.execute(f'select {columns} from {table_name} {cond}')
        results = self.cursor.fetchall()
        return results
