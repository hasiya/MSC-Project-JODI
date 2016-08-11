"""
The main server file
Contains all the server side routing functions.
"""

"""
importing the python Json library
"""
import json

"""
Importing Flask libraries
"""
from flask import Flask, request, Response

"""
Importing reader python functions
"""
import readers.PDF as pdf

"""
Importing connections functions
"""
from connections import elastic
from connections import api_call

app = Flask(__name__)

"""
The /insert_data route.
This takes the data set information and the data set from the request and post the data in to the elasticsearch.
"""


@app.route('/insert_dataset', methods=['POST'])
def insert_data_set():
    response = {}
    if request.method == 'POST':
        name_s = request.get_data()
        data = json.loads(name_s)

        # response = mongo.insert_data(data["collectionName"], data["collectionData"])
        response = elastic.insert_data(data["datasetInfo"], data["DataSet"], data["headers"], data["apiData"])

    return Response(
        json.dumps(response),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        }
    )


"""
this function insert api data in to elasticsearch
"""


@app.route('/insert_api', methods=['POST'])
def insert_api():
    response = {}
    if request.method == 'POST':
        name_s = request.get_data()
        data = json.loads(name_s)

        # response = mongo.insert_data(data["collectionName"], data["collectionData"])
        response = elastic.insert_api(data["datasetInfo"], data["apiData"], data["apiUrl"], data["dataPath"],
                                      data["apiType"])

    return Response(
        json.dumps(response),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        }
    )


"""
This route takes the id of data set and retrieve the data set from the elasticsearch
"""


@app.route('/get_dataset/<id>', methods=['GET'])
def get_data(id):
    doc = elastic.get_dataset(id)

    return Response(
        json.dumps(doc),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        })


"""
this route call the url in the request query string.
"""


@app.route('/get_api_data', methods=['GET'])
def get_ai_data():
    if request.method == 'GET':
        url = request.query_string
        data = api_call.get_api_content(url)

        return Response(
            json.dumps(data),
            mimetype='application/json',
            headers={
                'Cache-Control': 'no-cache',
                'Access-Control-Allow-Origin': '*'
            })


"""
The route function delete the data set from the elastic search.
"""


@app.route('/delete_dataset/<dataset_id>')
def delete_data(dataset_id):
    # if request.method == "DELETE":
    response = elastic.delete_dataset(dataset_id)

    return Response(
        json.dumps(response),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        })


"""
The route function to search data sets in elastic by search terms
"""


@app.route('/search_dataset/<search_term>', methods=['GET'])
def search_data(search_term):
    hits = elastic.search_dataset(search_term)

    return Response(
        json.dumps(hits),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        })


"""
this function returns all the data sets in the elasticsearch
"""


@app.route('/get_all_dataset', methods=['GET'])
def get_all_data():
    hits = elastic.get_all_datasets()

    return Response(
        json.dumps(hits),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        })


"""This route funciton is not used the project
this function gets a PDF file from client side and using PDFMiner library readers the pdf file and returns the content
of the file
"""


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
