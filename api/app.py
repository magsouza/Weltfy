from flask import Flask

app = Flask(__name__)
app.secret_key = ""
app.SERVER_NAME = "api:5000"

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
