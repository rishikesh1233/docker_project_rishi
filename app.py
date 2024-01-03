from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rishi:1234@db:5432/my_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

# Define a simple model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

@app.route('/')
def hello():
    # Create a table if it doesn't exist
    db.create_all()
    
    # Insert a sample record
    new_user = User(username='rishi')
    db.session.add(new_user)
    db.session.commit()

    # Query the database and display the result
    result = User.query.all()
    return f'Hello, world! Database content: {result[0].username}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)