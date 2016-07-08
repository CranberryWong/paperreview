#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
import tornado.locale
import random
from handlers.util import db
from handlers.auth import StaticData
from handlers.main import BaseHandler
import uuid

global lang_encode
lang_encode = 'zh_CN'
tornado.locale.set_default_locale(lang_encode)

class SearchListHandler(BaseHandler):
    pass
