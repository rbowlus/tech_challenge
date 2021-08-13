from flask import current_app as app
from flask.json import jsonify

@app.route('/scrape')
def scrape():
    return jsonifygit