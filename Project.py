import json
import logging

from flask import Flask, request, Response, render_template

import readers.CSV as csv
import readers.PDF as pdf
from connections import mongo
from connections import elastic

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
def csv_data():
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


@app.route('/insert_dataset', methods=['GET', 'POST'])
def insert_data_set():
    response = {}
    if request.method == 'POST':
        name_s = request.get_data()
        data = json.loads(name_s)

        response = mongo.insert_data(data["collectionName"], data["collectionData"])
        # response = elastic.insert_data(data["collectionName"], data["collectionData"])


        # logging.warning(data)

    return Response(
        json.dumps(response),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        }
    )


@app.route('/check_dataset', methods=['GET', 'POST'])
def check_data_set():
    response = {}
    if request.method == 'POST':
        name_s = request.get_data()
        data = json.loads(name_s)

        response = mongo.check_data_set(data)

        # logging.warning(data)

    return Response(
        json.dumps(response),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        }
    )


@app.route('/pdf_data', methods=['POST', 'GET'])
def pdf_data():
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
