import sqlite3
from sqlite3 import Error

class Books:
    def __init__(self):
        self.db_file = "books_list.db"
        with sqlite3.connect(self.db_file) as self.conn:
            self.conn.execute("""
                -- books table
                CREATE TABLE IF NOT EXISTS books (
                    id	integer PRIMARY KEY,
                    title text NOT NULL,
                    author text,
                    year text
                    );
                """)
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()

    def all(self):
        self.cur.execute(f"SELECT * FROM books")
        rows_all = self.cur.fetchall()
        return rows_all

    def get(self, id):
        self.cur.execute(f"SELECT * FROM books WHERE id=?", (id,))
        rows = self.cur.fetchone()
        return rows

    def create(self, data):
        if 'csrf_token' in data:
            data.pop('csrf_token')
        sql = '''INSERT INTO books(title, author, year)
                VALUES(?,?,?)'''
        values = tuple(v for v in data.values())
        self.cur.execute(sql, values)
        self.conn.commit()
        return self.cur.lastrowid

    def update(self, id, data):
        if 'csrf_token' in data:
            data.pop('csrf_token')
        parameters = [f"{k} = ?" for k in data]
        parameters = ", ".join(parameters)
        values = tuple(v for v in data.values())
        values += (id,)
        sql = f''' UPDATE books
                                SET {parameters}
                                WHERE id = ?'''
        try:
            self.cur.execute(sql, values)
            self.conn.commit()
        except sqlite3.OperationalError as e:
            print(e)

    def form_values(form):
        form_values = []
        for value in form:
            form_values.append(value)
            print(form_values)

books = Books()

#wywołania

#print(books.all())
#k = {'title':'ttttt', 'author':'ssssssssss', 'year':123}
#books.create(k)
#print(f' get: {books.get(1)}')
#u = {'title':'aaaaaaa', 'author':'3333333333', 'year':234234}
#books.update(20, u)
