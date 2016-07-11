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
    def get(self):
        BaseHandler.initialize(self)
        user_id = self.get_argument('uid')
        users = db.user
        user_one = user.update_one({'user_id': user_id})
        user_

class AuthReviseHandler(BaseHandler):
    pass