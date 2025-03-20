from .. import app
from flask import jsonify

@app.route('/')
def hello_world():
    """ Testing if flask app is running """
    return jsonify({
        'success': True,
        'message': 'Flask app is working'
    }), 200
