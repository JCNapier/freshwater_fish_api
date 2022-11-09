from flask import Flask 

app = Flask(__name__) 

@app.route('/')
def catch_and_release():
  return {'Catch': '& Release'}

if __name__ == '__main__':
  app.run(debug=True)