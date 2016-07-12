#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import tornado.web
import tornado.locale
import random
from PIL import Image
from cStringIO import StringIO
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

class Pagination(object):
    def __init__(self):
        self.pre = ''
        self.next = ''
        self.pages = []
        self.current = ''
        self.action = ''

def generatePagination(action, list, targetpage):
    targetpage = int(targetpage)
    pagination = Pagination()
    pagination.current = targetpage
    maxpage = list.count()
    pagination.pages = range(1, maxpage/10+2)
    pagination.pre = str(targetpage-1) if targetpage-1 in pagination.pages else str(targetpage)
    pagination.next = str(targetpage+1) if targetpage+1 in pagination.pages else str(targetpage)
    pagination.action = action
    list = list[(targetpage-1) * 10 : targetpage * 10]
    return list, pagination

class ImageUpload(tornado.web.RequestHandler):
    def post(self):
        #upload_path = os.path.join(os.path.dirname(__file__),"static"),
        if 'fileData' in self.request.files:
            file_dict_list = self.request.files['fileData']
            for file_dict in file_dict_list:
                filename = nameRewrite(file_dict["filename"]).encode('utf8')
                data = file_dict["body"]
                image = Image.open(StringIO(data))
                image.save(articles_path + filename, quality=150)
            self.write({
			"success": True,
			"msg": 'success',
			"file_path": '/static/articles/' + filename
		})
