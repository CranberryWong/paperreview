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
from handlers.util import db
from handlers.main import BaseHandler

class AdminMainHandler(BaseHandler):
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