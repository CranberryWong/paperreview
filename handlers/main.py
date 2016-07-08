#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
import tornado.locale
import random
from handlers.util import db
from handlers.auth import StaticData
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

class PaperHandler(BaseHandler):
    def get(self, id):
        BaseHandler.initialize(self)
        papers = db.paper
        result = papers.find_one({"paper_id": id})
        self.title = result["title"]
        self.render("main/detail.html", result = result)

class UserHandler(BaseHandler):
    def get(self, id):
        BaseHandler.initialize(self)
        users = db.user
        user_id = uuid.UUID(id)
        result = users.find_one({"user_id": user_id})
        self.title = result["username"]
        self.render("main/profile.html", result = result)

class FormHandler(tornado.web.RequestHandler):
    def get(self):
        self.title = "Test"
        self.render("experiment/form.html")
        
    def post(self):
        self.title = "Test"
    
        ifTest = self.get_argument('ifTest', default='')   
        gender = self.get_argument('gender', default='')
        age = self.get_argument('age', default='')
        ifReside = self.get_argument('ifReside', default='')
        firstCountry = self.get_argument('firstCountry', default='')
        howLong = self.get_argument('howLong', default='')
        language = self.get_argument('language', default='')
        fatherNation = self.get_argument('fatherNation', default='')
        motherNation = self.get_argument('motherNation', default='')
        education = self.get_argument('education', default='')
        surfingTime = self.get_argument('surfingTime', default='')
        
        collection = db.form_collection
        newForm = form(ifTest, gender, age, ifReside, firstCountry, howLong, language, fatherNation, motherNation, education, surfingTime)
        post = dict(id = newForm.id, 
                    ifTest = newForm.ifTest, 
                    gender = newForm.gender,
                    age = newForm.age,
                    ifReside = newForm.ifReside,
                    firstCountry = newForm.firstCountry,
                    howLong = newForm.howLong,
                    language = newForm.language,
                    fatherNation = newForm.fatherNation,
                    motherNation = newForm.motherNation,
                    education = newForm.education,
                    surfingTime = newForm.surfingTime,
                    createTime = newForm.createTime)
        post_id = collection.insert_one(post).inserted_id
        self.redirect('/aesthetic/note')
  
class StatementHandler(tornado.web.RequestHandler):
    def get(self):
        self.title = "Statement"
        self.render("experiment/first.html")
        
class NoteHandler(tornado.web.RequestHandler):
    def get(self):
        self.title = "Note"
        self.render("experiment/second.html")            
                
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

