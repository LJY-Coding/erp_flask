from flask import Flask

app = Flask(__name__, static_url_path='/')

app.secret_key = "23jguia634bt"