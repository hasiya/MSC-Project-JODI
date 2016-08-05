import requests
from elasticsearch import Elasticsearch as elasticSearch
from elasticsearch import ElasticsearchException as elasticException
import json
import datetime

res = requests.get('http://localhost:9200')

es = elasticSearch([{'host': 'localhost', 'port': 9200}])

db_dateTime = "date_time"
db_datasetName = "dataset_name"
db_personName = "person_name"
db_dataSource = "data_source"
db_dataset = "dataset"
db_headers = 'headers'
db_isApi = 'is_api'
db_apiUrl = "APIurl"
db_urlDatasetPath = "url_dataset_path"
db_apiType = "api_type"
index = 'csv_data'

mapping = {
    "mappings": {
        "data_sets": {
            "properties": {
                "dataset_name": {
                    "type": "string"
                },
                "person_name": {
                    "type": "string"
                },
                "data_source": {
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
                },
                "is_api": {
                    "type": "boolean"
                },
                "APIurl": {
                    "type": "string"
                },
                "url_dataset_path": {
                    "type": "string"
                },
                "api_type":
                    {
                        "type": "string"
                    }
            }
        }
    }
}


def insert_data(dataset_info, dataset, headers, is_api):
    index_exsist = es.indices.exists(index)

    if not index_exsist:

        es.indices.create(index=index, body=mapping)

    dataset_name_exist = es.exists(index=index, doc_type='data_sets', id=dataset_info['dataset_name'])

    all_data = {
        db_dateTime: datetime.datetime.now(),
        db_datasetName: dataset_info['dataset_name'],
        db_personName: dataset_info['person_name'],
        db_dataSource: dataset_info['data_source'],
        db_headers: headers,
        db_dataset: dataset,
        db_isApi: is_api
    }
    if not dataset_name_exist:
        es.index(index=index, doc_type='data_sets', id=dataset_info['dataset_name'], body=all_data)

        return {
            "error_code": 0,
            "message": "Successfully data added to elasticsearch"
        }

    else:
        return {
            "error_code": 1,
            "message": "Data set name already exist"
        }


def insert_api(dataset_info, is_api, url, data_path, api_type):
    index_exsist = es.indices.exists(index)

    if not index_exsist:
        es.indices.create(index=index, body=mapping)

    dataset_name_exist = es.exists(index=index, doc_type='data_sets', id=dataset_info['dataset_name'])

    all_data = {
        db_dateTime: datetime.datetime.now(),
        db_datasetName: dataset_info['dataset_name'],
        db_personName: dataset_info['person_name'],
        db_dataSource: dataset_info['data_source'],
        db_isApi: is_api,
        db_apiUrl: url,
        db_urlDatasetPath: data_path,
        db_apiType: api_type
    }
    if not dataset_name_exist:
        es.index(index=index, doc_type='data_sets', id=dataset_info['dataset_name'], body=all_data)

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


def delete_dataset(dataset_name):
    index_exsist = es.indices.exists(index)

    if index_exsist:
        try:
            result = es.delete(index=index, doc_type='data_sets', id=dataset_name)

        except elasticException as err:
            result = err

        if result.args[0]:

            if result.args[0] == 404:
                return {
                    "error_code": 1,
                    "message": "Data Not Found"
                }
        else:
            return {
                "error_code": 0,
                "message": "Data set deleted!"
            }


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

        # result2 = es.search(index=index, doc_type='data_sets', body={})

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


def get_all_datasets():
    index_exsist = es.indices.exists(index)

    if index_exsist:

        result = es.search(index=index, doc_type='data_sets', body={})

        # result2 = es.search(index=index, doc_type='data_sets', body={})

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
