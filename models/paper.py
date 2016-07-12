#!/usr/bin/env python
# -*- coding:utf-8 -*-

from datetime import datetime
import uuid

class Paper(object):
    '''
    _db = "papersourcing_db"
    _collection = "paper"

    paper_id = field.AutoIncrement(collection = "paper")
    user = field.DynamicDocument()
    title = field.Char()
    author = field.Char()
    content = field.Char()
    pubDate = field.Date()
    createTime = field.TimeStamp()
    reviseTime = field.TimeStamp()

    Paper.user = orm.Lazy(type = User, key = 'user_id')   
    '''
    def __init__(self, user_id, username, avatar, title, author, content, pubDate):    

        self.paper_id = str(uuid.uuid1())
        self.user = {'user_id': user_id, 'username': username, 'avatar': avatar}
        self.title = title
        self.author = author
        self.content = content
        self.pubDate = pubDate
        self.createTime = datetime.now()
        self.reviseTime = datetime.now()        
        
    def __repr__(self):   

        return '<post:%s, title:%s>' % (self.id, self.name)

    def getValue(self):
        
        return dict(paper_id = self.paper_id, user = self.user, title = self.title, author = self.author, content = self.content, pubDate = self.pubDate, createTime = self.createTime, reviseTime = self.reviseTime)

 