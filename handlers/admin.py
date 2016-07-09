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
        self.title = "Dashboard | " + self.signeduser
        self.render("admin/index.html")
