from flask import Flask
from controllers import api
import os

app = Flask(__name__)
app.register_blueprint(api)
app.secret_key = os.urandom(24)

if __name__ == "__main__":
    app.run(debug=True)
