from flask import Flask, render_template
from flask.ext.mongoengine import MongoEngine
from flask.ext.classy import FlaskView


app = Flask(__name__)

# Configure the database
app.config['MONGODB_SETTINGS'] = {
    'db': 'namethatbird',
    'host': 'localhost',
    'port': 10036
}

db = MongoEngine(app)


class HomeView(FlaskView):
    route_base = '/'

    def index(self):
        return render_template('index.html')

HomeView.register(app)

if __name__ == '__main__':
    app.run(debug=True)