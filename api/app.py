from flask import Flask, request, redirect, render_template, session
import json

app = Flask(__name__)
app.secret_key = ""


if __name__ == '__main__':
    app.run(debug=True)