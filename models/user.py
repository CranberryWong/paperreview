#!/usr/bin/env python
# -*- coding:utf-8 -*-

from datetime import datetime
#import logging
#import humongolus.field as field
#import humongolus as orm
import uuid

class User(object):
    '''
    _db = "papersourcing_db"
    _collection = "user"

    user_id = field.AutoIncrement(collection = "user")
    username = field.Char(required = True)
    password = field.Char()
    email = field.Email()
    position = field.Char()
    role = field.Integer()
    authenication = field.Boolean()
    avatar = field.Char()
    paper = orm.List(type = Paper)
    '''
    def __init__(self, username, password, email, position, role, avatar):

        self.user_id = uuid.uuid1()
        self.username = username
        self.password = password
        self.email = email
        self.position = position
        self.role = 3
        self.authenication = True
        self.avatar = avatar
        self.paper = []
    
    def __repr__(self):
        
        return '<user:%s, name=%s>' % (self.id, self.name)

    def getValue(self):

        return dict(user_id = self.user_id, username = self.username, password = self.password, email = self.email, position = self.position, role = self.role, authenication = self.authenication, avatar = self.avatar, paper = self.paper)