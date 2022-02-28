from flask import Flask, request, render_template, redirect, url_for

from forms import BookForm
from models import books #działa wszystko
#from models_proste import books #działa przez RUN nie działa WWW
#from models_with import books #działa przez RUN nie działa WWW

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route('/books/', methods=["GET", "POST"])
def books_list():
    form = BookForm()
    error = ""
    if request.method == "POST":
        print('if method post')
        if form.validate_on_submit():
            books.create(form.data)
        return redirect(url_for("books_list"))
    
    return render_template("books.html", form=form, books=books.all(), error=error)

@app.route("/book/<int:book_id>/", methods=["GET", "POST"])
def book_details(book_id):
    book = books.get(book_id)
    print(tuple(book))
    form = BookForm(data=book)

    if request.method == "POST":
        if form.validate_on_submit():
            books.update(book_id, form.data)
        return redirect(url_for("books_list"))
    return render_template("book.html", form=form, book_id=book_id)

if __name__ == "__main__":
    app.run(debug=True)