from flask import Flask, render_template
from flask.ext.mongoengine import MongoEngine


app = Flask(__name__)

# Configure the database
app.config['MONGODB_SETTINGS'] = {
    'db': 'namethatbird',
    'host': 'localhost',
    'port': 10036
}
with app.app_context():
    db = MongoEngine(app)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')
    # return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)