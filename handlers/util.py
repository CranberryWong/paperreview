#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
import tornado.locale
import random
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.papersourcing_db

def NameRewrite(filename):
    file_timestamp = int(time.time())
    name_split = filename.split('.')
    if len(name_split) == 1:
        filename = filename + str(file_timestamp)
    else:
        filename = name_split[0] + str(file_timestamp) + '.' + name_split[1]
    return filename