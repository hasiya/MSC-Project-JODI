from pymongo import MongoClient
import datetime

db_dateTime = "date_time"
db_datasetName = "dataset_name"
db_dataset = "dataset"



def connect_db():
    client = MongoClient("mongodb://localhost:27017/")

    db = client.dct_csv
    db.datasets.create_index([(db_datasetName, 1), (db_dataset, 1)], unique=True)
    db.datasets.create_index([(db_dateTime, 1)], unique=False)

    return db


def insert_data(datasetName, datasetObject):
    db = connect_db()

    checkDataset = db.datasets.find_one({
        db_dataset: datasetObject
    })

    checkDatasetName = db.datasets.find_one({
        db_datasetName: datasetName
    })
    # if not checkDataset:
    if not checkDatasetName:
        a = db.datasets.insert_one({
            db_dateTime: datetime.datetime.utcnow(),
            db_datasetName: datasetName,
            db_dataset: datasetObject
        })

        return {
            "error_code": 0,
            "message": "Successfully data added to mongo"
        }

    else:
        return {
            "error_code": 1,
            "message": "Data set name already exist"
        }
        # else:
        #     return {
        #         "error_code": 1,
        #         "data_set_name": checkDataset[db_datasetName],
        #         "message": "Data set already exist"
        #     }


def check_data_set(dataset):
    db = connect_db()

    checkDataset = db.datasets.find_one({
        db_dataset: dataset
    })

    if checkDataset:
        return {
            "error_code": 1,
            "data_set_name": checkDataset[db_datasetName],
            "message": "Data set already exist"
        }
    else:
        return {
            "error_code": 0,
            "message": "New data set"
        }
