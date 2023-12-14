from flask import Flask
from controllers import api

app = Flask(__name__)
app.register_blueprint(api)

# Home route (optional)
@app.route("/", methods=["GET"])
def index():
    return "Welcome to your Flask application!"

if __name__ == "__main__":
    app.run(debug=True)
