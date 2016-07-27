import requests
from elasticsearch import Elasticsearch as elasticSearch
import json
import datetime

res = requests.get('http://localhost:9200')
es = elasticSearch([{'host': 'localhost', 'port': 9200}])

db_dateTime = "date_time"
db_datasetName = "dataset_name"
db_dataset = "dataset"
index = 'csv_data'


def insert_data(datasetName, dataset):
    dataset_name_exist = es.exists(index=index, doc_type='data_sets', id=datasetName)

    all_data = {
        db_dateTime: datetime.datetime.utcnow(),
        db_datasetName: datasetName,
        db_dataset: dataset
    }
    if not dataset_name_exist:
        es.index(index=index, doc_type='data_sets', id=datasetName, body=all_data)

        return {
            "error_code": 0,
            "message": "Successfully data added to mongo"
        }

    else:
        return {
            "error_code": 1,
            "message": "Data set name already exist"
        }


def search_dataset(search_term):
    result = es.search(index=index, doc_type='data_sets', body={
        "query": {
            "match": {
                "_all": search_term
            }
        }
    })

    # print (result)


search_dataset("I voted Yes last time and I")
