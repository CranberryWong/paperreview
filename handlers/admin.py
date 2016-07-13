#! /usr/bin/env python
#coding:utf-8

import tornado.web
import time
import os
import markdown
from models.user import User
from models.paper import Paper
import hashlib
import json
import random
from datetime import datetime
from PIL import Image
from handlers.util import db, Role
from handlers.main import BaseHandler
import markdown

class AdminMainHandler(BaseHandler):
    @tornado.web.authenticated
    @Role
    def get(self):
        BaseHandler.initialize(self)
        self.title = "Dashboard | " + self.signeduser
        users = db.user
        userList = users.find({}).sort('username')
        self.render("admin/index.html", userList = userList)

class RoleReviseHandler(BaseHandler):
    def post(self):
        BaseHandler.initialize(self)
        user_id = self.get_argument('user_id')
        role = self.get_argument('roleselect')
        users = db.user
        user_one = users.update_one({'user_id': user_id},{"$set": {"role": int(role)}})
        self.write("done")

class AuthReviseHandler(BaseHandler):
    def post(self):
        BaseHandler.initialize(self)
        user_id = self.get_argument('user_id')
        auth = self.get_argument('authselect')
        print auth
        if auth == 'True':
            auth = True
        else:
            auth = False
        users = db.user
        user_one = users.update_one({'user_id': user_id},{"$set": {"authenication": auth}})
        self.write("done")

#About Us
class AboutAdminHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        BaseHandler.initialize(self)
        self.title = "Edit About Us"
        
        info_path = os.path.join(self.get_template_path(), 'aboutme.md')
        aboutcontent = open(info_path).read().decode('utf8')
        self.render("admin/about.html", aboutcontent = aboutcontent)

    def post(self):
        BaseHandler.initialize(self)
        content = self.get_argument("content", default="")
        info_path = os.path.join(self.get_template_path(), 'aboutme.md')
        with open(info_path, 'w') as f:
            f.write(content.encode('utf8'))
        self.redirect('/admin/aboutus')

