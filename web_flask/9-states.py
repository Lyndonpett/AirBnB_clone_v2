#!/usr/bin/python3
'''Flask app for states'''


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def states(id=None):
    states = storage.all(State)

    if id:
        states = states.get('State.{}'.format(id))

    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def teardown(context):
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
