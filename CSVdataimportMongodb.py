# -*- coding: utf-8 -*-
"""
Created on Sun May 21 08:14:53 2017

@author: Kelum Perera
"""

#!/usr/bin/env python
import sys
import pandas as pd
import pymongo
import json
import os


def import_content(filepath):
    mng_client = pymongo.MongoClient('localhost', 27017)
    mng_db = mng_client['Mydatabase'] # Replace mongo db name
    collection_name = 'MyCollection' # Replace mongo db collection name
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname(os.path.realpath('__file__'))
    file_res = os.path.join(cdir, filepath)

    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)

if __name__ == "__main__":
  filepath = 'E://Credit.csv'  # pass csv file path
import_content(filepath)