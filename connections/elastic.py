import requests
from elasticsearch import Elasticsearch as elasticSearch
import json
import datetime

res = requests.get('http://localhost:9200')

es = elasticSearch([{'host': 'localhost', 'port': 9200}])

db_dateTime = "date_time"
db_datasetName = "dataset_name"
db_dataset = "dataset"
db_headers = 'headers'
index = 'csv_data'


def insert_data(dataset_name, dataset, headers):
    index_exsist = es.indices.exists(index)

    if not index_exsist:
        mapping = {
            "mappings": {
                "data_sets": {
                    "properties": {
                        "dataset_name": {
                            "type": "string"
                        },
                        "date_time": {
                            "type": "date",
                            "format": "strict_date_optional_time||epoch_millis"
                        },
                        "dataset": {
                            "type": "nested"
                        },
                        "headers": {
                            "type": "string"
                        }
                    }
                }
            }
        }

        es.indices.create(index=index, body=mapping)

    dataset_name_exist = es.exists(index=index, doc_type='data_sets', id=dataset_name)

    all_data = {
        db_dateTime: datetime.datetime.now(),
        db_datasetName: dataset_name,
        db_headers: headers,
        db_dataset: dataset

    }
    if not dataset_name_exist:
        es.index(index=index, doc_type='data_sets', id=dataset_name, body=all_data)

        return {
            "error_code": 0,
            "message": "Successfully data added to elasticsearch"
        }

    else:
        return {
            "error_code": 1,
            "message": "Data set name already exist"
        }


def get_dataset(dataset_name):
    index_exsist = es.indices.exists(index)

    if index_exsist:
        result = es.get(index=index, doc_type='data_sets', id=dataset_name)

        doc = result['_source']

        if (doc):
            return doc
        else:
            return {}



def search_dataset(search_term):
    index_exsist = es.indices.exists(index)

    if index_exsist:

        result = es.search(index=index, doc_type='data_sets', body={
            "query": {
                "match": {
                    "_all": search_term
                }
            }
        })
        hits = result['hits']['hits']

        # print (hits)
        if (hits):
            return hits
        else:
            # return {
            #     "error_code": 1,
            #     "message": "No data."
            # }
            return []

    else:
        return []
# search_dataset("I voted Yes last time and I")
