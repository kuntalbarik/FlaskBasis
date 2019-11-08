from flask import Flask

app=Flask(__name__)

@app.route("/hello")
def helloWorld():
    return "hello World....."
