from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World 2016 esto es una maravilla!"

if __name__ == "__main__":
    app.run('0.0.0.0',debug=True)
