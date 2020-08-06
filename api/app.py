from flask import Flask

app = Flask(__name__)
app.secret_key = ""

from routes import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
