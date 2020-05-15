from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def generate_random_number():
    r_number = random.randint(0,100)
    return str(r_number)

if __name__ == "__main__":
    app.run(host="0.0.0.0")