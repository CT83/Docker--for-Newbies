from flask import Flask
import random
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://rohan:1234@database:5432/rand_db'
db = SQLAlchemy(app)

class RandomNumbers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)

@app.route('/')
def generate_random_number():
    r_number = random.randint(0,100)
    
    random_number = RandomNumbers(number=r_number)
    db.session.add(random_number)
    db.session.commit()

    return str(r_number)

if __name__ == "__main__":
    db.create_all()
    app.run(host="0.0.0.0")