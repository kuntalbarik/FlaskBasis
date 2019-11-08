from flask import Flask

app=Flask(__name__)

authors=["Kuntal Barik","Rahul Das","Surajit Pal"]


@app.route("/hello")
def helloWorld():
    return "hello World....."

@app.route("/showAuthors")
def ShowAuthors():
    html="""
    <h1>Authors</h1>
    {authors_list}
    """
    authors_list="<ul>"
    for author in authors:
        authors_list+="\n<li>"+author+"</li>"
    authors_list+="\n</ul>"

    return html.format(authors_list=authors_list)