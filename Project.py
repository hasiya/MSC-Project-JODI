import json

from flask import Flask, request, Response, render_template
# from werkzeug.utils import secure_filename
import readers.CSV as csv
import readers.PDF as pdf
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

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/csv_data', methods=['GET', 'POST'])
def csvdata():
    dict_data = {}

    if request.method == 'POST':
        data = request.values['data']
        logging.warning(request)
        dict_data = csv.read(data)

    return Response(
        json.dumps(dict_data),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        }
    )


@app.route('/pdf_data', methods=['POST', 'GET'])
def pdfdata():
    pdfText = ""
    if request.method == 'POSt':
        data = request.get_data()
        pdfText = pdf.readText(data)

    return Response(
        pdfText,
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        }
    )


if __name__ == '__main__':
    app.run()
