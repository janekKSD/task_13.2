from flask import Flask, request, render_template, redirect, url_for

from forms import BookForm
#from models_dzialajace import books #działa wszystko
from models_nowe import books #nowe działa wszystko


app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"



@app.route('/books/', methods=["GET", "POST"])
def books_list():
    conn = books.create_table()
    form = BookForm()
    error = ""
    if request.method == "POST":
        print('if method post')
        if form.validate_on_submit():
            books.create(form.data, conn)
        return redirect(url_for("books_list"))
    
    return render_template("books.html", form=form, books=books.all(conn), error=error)

@app.route("/book/<int:book_id>/", methods=["GET", "POST"])
def book_details(book_id):
    conn = books.create_table()
    book = books.get(book_id, conn)
    print(tuple(book))
    form = BookForm(data=book)

    if request.method == "POST":
        if form.validate_on_submit():
            books.update(book_id, form.data, conn)
        return redirect(url_for("books_list"))
    return render_template("book.html", form=form, book_id=book_id)

if __name__ == "__main__":
    app.run(debug=True)