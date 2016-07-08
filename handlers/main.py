#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
import tornado.locale
import random
from handlers.util import db
from handlers.auth import StaticData
from models.paper import Paper
import uuid

global lang_encode
lang_encode = 'zh_CN'
tornado.locale.set_default_locale(lang_encode)

class ChangeLang(tornado.web.RequestHandler):
    def get(self):
        global lang_encode
        if lang_encode == 'zh_CN':
            lang_encode = 'en_US'
        else:
            lang_encode = 'zh_CN'
        tornado.locale.set_default_locale(lang_encode)
        self.redirect('/')
      
class BaseHandler(StaticData):
    def initialize(self):
        StaticData.initialize(self)
        self.title = 'Untitled'
        if lang_encode == 'zh_CN':
            self.lang = 'English'
        else:
            self.lang = '中文版'
        if self.signeduser:
            users = db.user
            self.user = users.find_one({'username':self.signeduser})
            self.signedid = self.user['user_id']
            self.signavatar = self.user['avatar']
        else:
            self.signedid = None

    def get_user_locale(self):
        #return tornado.locale.set_default_locale('en_US')
        return tornado.locale.get("en_US")
    
class MainHandler(BaseHandler):
    def get(self):
        BaseHandler.initialize(self)
        self.title = 'Home'
        papers = db.paper
        paper = papers.find({}).sort("reviseTime")
        self.render("main/main.html", paper = paper)

class PaperShowHandler(BaseHandler):
    def get(self, id):
        BaseHandler.initialize(self)
        papers = db.paper
        result = papers.find_one({"paper_id": id})
        self.title = result["title"]
        self.render("main/detail.html", result = result)

class PaperCommitHandler(BaseHandler):
    def post(self, id):
        BaseHandler.initialize(self)

        title = self.get_argument('title', default='')
        content = self.get_argument('content', default='')
        author = self.get_argument('author', default='')
        pubdate = self.get_argument('pubdate', default='')
        
        papers = db.paper
        newPaper = Paper(id, title, author, content, pubdate)
        result = papers.insert_one(newPaper.getValue()).inserted_id
        self.write('<script language="javascript">alert("success");self.location="/user/{0}";</script>'.format(id))

#User Profile Handler
class UserHomeHandler(BaseHandler):
    def get(self, id):
        BaseHandler.initialize(self)
        users = db.user
        user_id = uuid.UUID(id)
        result = users.find_one({"user_id": user_id})
        self.title = result["username"]
        self.render("main/profile.html", result = result)

class UserProfileHandler(BaseHandler):
    pass

'''
class EditPost(tornado.web.RequestHandler):
    def get(self):
        users = self.application.db['user']
        user = users.find_one()
        if user:
            del user["_id"]
            self.set_status(200)
            self.write(user)            
        else:
			self.set_status(404)
			self.write({"error": "word not found"})            
'''

#List by Index Handler
class ListByDate(BaseHandler):
    pass

class ListByType(BaseHandler):
    pass