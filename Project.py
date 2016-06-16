from flask import Flask, request, redirect, make_response
from flask.templating import render_template
from werkzeug.utils import secure_filename
import readers.CSV as csv
import logging
#
# SECRET_KEY = 'secret!'
# # mandatory
# CODEMIRROR_LANGUAGES = ['python', 'html']
# # optional
# CODEMIRROR_THEME = '3024-day'
# CODEMIRROR_ADDONS = (
#             ('display','placeholder'),
# )

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
#

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
        return render_template("index.html")

@app.route('/csv_data')
def csvData():
    data  = request.args.get()
    logging.warning(data)


if __name__ == '__main__':
    app.run()
