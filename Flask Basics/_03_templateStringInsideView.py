from flask import Flask,render_template_string

app=Flask(__name__)

authors=["Kuntal Barik","Rahul Das","Surajit Pal"]

@app.route("/hello")
def helloWorld():
    return "hello World....."

@app.route("/showAuthors")
def ShowAuthors():
    html="""
    <h1>Authors</h1>
    <ul>
    {%for author in authors%}
    <li>{{author}}</li>
    {%endfor%}
    </ul>
    """
    return render_template_string(html,authors=authors)