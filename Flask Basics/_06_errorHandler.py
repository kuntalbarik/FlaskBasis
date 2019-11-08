from flask import Flask,render_template

app=Flask(__name__)


authors=["Kuntal Barik","Rahul Das","Surajit Pal"]

@app.route("/")
@app.route("/home")
def Home():
    return render_template("index.html")

@app.route("/showAuthors")
def ShowAuthors():
    return render_template("routing/authors.html",authors=authors)

@app.route("/About")
def About():
    return render_template("routing/about.html")

@app.errorhandler(404)
def NotFound(error):
    return render_template("routing/404.html"),404