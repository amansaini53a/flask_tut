from flask import Flask

app = Flask(__name__)

# POST used to receive the data.
# GEt used to send data only.

@app.route("/")
def home():
    return "Hello, World"


app.run(port=5000)
