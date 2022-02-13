import sqlite3
from sqlite3 import Error

class Books:
    def __init__(self):
        self.db_file = "books_list.db"
        with sqlite3.connect(self.db_file) as conn:
            conn.execute("""
                -- books table
                CREATE TABLE IF NOT EXISTS books (
                    id	integer PRIMARY KEY,
                    title text NOT NULL,
                    author text,
                    year text
                    );
                """)

    def all(self):
        with sqlite3.connect(self.db_file) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM books")
            rows_all = cur.fetchall()
            return rows_all
            

    def get(self, id):
        with sqlite3.connect(self.db_file) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM books WHERE id=?", (id,))
            rows = cur.fetchone()
            return rows

    def create(self, data):
        if 'csrf_token' in data:
            data.pop('csrf_token')
        sql = '''INSERT INTO books(title, author, year)
                VALUES(?,?,?)'''
        with sqlite3.connect(self.db_file) as conn:
            print(data)
            values = tuple(v for v in data.values())
            print(values)
            cur = conn.cursor()
            cur.execute(sql, values)
            conn.commit()
            return cur.lastrowid

    def update(self, id, data):
        if 'csrf_token' in data:
            data.pop('csrf_token') 
        with sqlite3.connect(self.db_file) as conn:
            cur = conn.cursor()

            parameters = [f"{k} = ?" for k in data]
            parameters = ", ".join(parameters)
            values = tuple(v for v in data.values())
            values += (id,)
            sql = f''' UPDATE books
                                SET {parameters}
                                WHERE id = ?'''
            try:
                cur.execute(sql, values)
                conn.commit()
                print("OK")
            except sqlite3.OperationalError as e:
                print(e)

    def form_values(form):
        form_values = []
        for value in form:
            form_values.append(value)
            print(form_values)

books = Books()


