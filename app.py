from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/north_freshwater_fish_api' 
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class FishModel(db.Model):
  __tablename__ = 'Fish'

  id = db.Column(db.Integer, primary_key=True)
  species = db.Column(db.String())

  def __init__(self, species):
    self.species = species 

  def __repr__(self):
    return f'<Fish {self.species}'

@app.route('/')
def catch_and_release():
  return {'Catch': '& Release'}

if __name__ == '__main__':
  app.run(debug=True)