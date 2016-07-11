#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
import tornado.locale
import random
from handlers.util import db, generatePagination
from handlers.auth import StaticData
from handlers.main import BaseHandler
import uuid

global lang_encode
lang_encode = 'zh_CN'
tornado.locale.set_default_locale(lang_encode)

class SearchListHandler(BaseHandler):
    def get(self):
        BaseHandler.initialize(self)
        targetpage = int(self.get_argument('page',default='1'))
        keyword = self.get_argument('keyword',default='')
        papers = db.paper
        keywords = '/'+keyword+'/'
        paperList = papers.find({"$or":[{"title": {"$regex":keyword}},{"content": {"$regex":keyword}}]}).sort("reviseTime")
        paper, self.pagination = generatePagination('/search?keyword=' + keyword + '&page=', paperList, targetpage)
        self.thisquery = "搜索：" + keyword.encode('utf8')
        self.title = "搜索：" + keyword.encode('utf8')
        self.render("main/main.html", paper = paper)