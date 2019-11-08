from flask import  Flask,render_template

app=Flask(__name__)

authors=["Kuntal Barik","Rahul Das","Surajit Pal"]

@app.route("/hello")
def helloWorld():
    return "hello World....."

@app.route("/showAuthors")
def ShowAuthors():
    return render_template("routing/authors.html",authors=authors)