from flask import Flask
from redis import Redis
import os


app = Flask(__name__)
redis = Redis(host="redis", port=6379)


@app.route("/")
def hello():
    redis.incr("hits")
    counter = str(redis.get("hits"), "utf-8")
    return "This webpage has been viewed " + counter + " time(s)"


def create_file():
    with open("/code/test_file.txt", "w") as f:
        f.write("This is a test file created on startup.")


if __name__ == "__main__":
    create_file()
    app.run(host="0.0.0.0", port=8000, debug=True)
