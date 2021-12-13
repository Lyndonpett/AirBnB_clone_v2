#!/usr/bin/python3
'''Flask app for states'''


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states/")
def state_list():
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route("/states/<id>")
def state_by_id(id=None):
    states_value = storage.all(State)
    if id:
        states = states_value.get('State.{}'.format(id))
    else:
        states = states_value.values()
    return render_template('9-states.html', states=states, found=True)


@app.teardown_appcontext
def teardown(context):
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
