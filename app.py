from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, GCP from Docker and Jenkins!. From Jenkins Automation pipeline"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
