from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "helo, world!"
if __name__ == "__main__":
    app.run( port=5000)  # Explicitly set the host and port