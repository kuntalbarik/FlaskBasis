from flask import Flask,render_template

app=Flask(__name__)
authors=["Kuntal Barik","Rahul Das","Surajit Pal"]

@app.route("/")
@app.route("/home")
def Home():
    return render_template("index.html")

@app.route("/about")
def About():
    return render_template("routing/about.html")

@app.route("/authors")
def Authors():
    return render_template("routing/authors.html",authors=authors)
