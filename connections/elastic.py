"""
This file contains all the elasticsearch functions.
"""

"""Importing Elasticsearch libraries
"""
from elasticsearch import Elasticsearch as elasticSearch
from elasticsearch import ElasticsearchException as elasticException

"""
impotting dateTime library
"""
import datetime


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

"""
Elasticsearch mapping
"""
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

"""
The insert data function.
Function taks 4 parameters.

dataset_info: information about the data set (data set name, uploaded person's name and data set source)
dataset: The data set as a json object.
headers: properties of the data set.
is_api: This parameter is for check whether the dataset is an api or not.

"""
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


"""
This function is to insert api information to elaseticsearch
"""
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


"""
This function is to get data set from the data set ID."""
def get_dataset(dataset_name):
    index_exsist = es.indices.exists(index)

    if index_exsist:
        result = es.get(index=index, doc_type='data_sets', id=dataset_name)

        doc = result['_source']

        if (doc):
            return doc
        else:
            return {}


"""
The function is to delete data set from elasticsearch by data set id. """
def delete_dataset(dataset_name):
    index_exsist = es.indices.exists(index)

    if index_exsist:
        try:
            result = es.delete(index=index, doc_type='data_sets', id=dataset_name)

        except elasticException as err:
            result = err

        if hasattr(result, 'args'):

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


"""the funciton is to do a search query in elasticsearch by a search term. """
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


"""
this function is to get all the elastic data sets."""
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
