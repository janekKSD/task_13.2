import sqlite3
from sqlite3 import Error

class Books:
    def create_table(self):
        db_file = "books_list.db"
        conn = sqlite3.connect(db_file)
        conn.execute("""
                -- books table
                CREATE TABLE IF NOT EXISTS books (
                    id	integer PRIMARY KEY,
                    title text NOT NULL,
                    author text,
                    year text
                    );
                """)
        conn.row_factory = sqlite3.Row
        return conn
        
    def all(self, conn):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM books")
        rows_all = cur.fetchall()
        return rows_all

    def get(self, id, conn):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM books WHERE id=?", (id,))
        rows = cur.fetchone()
        return rows

    def create(self, data, conn):
        cur = conn.cursor()
        if 'csrf_token' in data:
            data.pop('csrf_token')
        sql = '''INSERT INTO books(title, author, year)
                VALUES(?,?,?)'''
        values = tuple(v for v in data.values())
        cur.execute(sql, values)
        conn.commit()
        return cur.lastrowid

    def update(self, id, data, conn):
        cur = conn.cursor()
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
            cur.execute(sql, values)
            conn.commit()
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
#books.update(27, u)
