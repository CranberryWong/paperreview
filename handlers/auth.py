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

class SignValidateBase(tornado.web.RequestHandler):
   def get_current_user(self):
      return self.get_secure_cookie('username')

class StaticData(SignValidateBase):
   def initialize(self):
      self.signeduser = SignValidateBase.get_current_user(self)
      #if ture:
      #    self.write('<script language="javascript">alert("你不适合这里！！");self.location="/signin";</script>')

class SignIn(SignValidateBase):
   def get(self):
      self.title = 'Sign in'
      self.render('main/signin.html')

   def post(self):
      username = self.get_argument('username', default='')
      password = self.get_argument('password', default='')
      md5_psw = hashlib.md5(password).hexdigest()
      users = db.user
      user = users.find_one({"username": username})
      if user:
          uname = user["username"]
          psw = user["password"]
      else:    
          return self.write('<script language="javascript">alert("{0}");self.location="/signin";</script>'.format('没有找到该用户！'))  
      if username == uname and md5_psw == psw:
          if user['authenication'] == True:
              self.set_secure_cookie('username', username)
              self.redirect('/')
          else:
              self.write('<script language="javascript">alert("对不起，账户需管理员确认后方能生效");self.location="/signin";</script>')
      else:
          self.write('<script language="javascript">alert("用户名或密码错误");self.location="/signin";</script>')

class SignUp(SignValidateBase):
   def get(self):
      self.title = 'Sign Up'
      self.render('main/signup.html')

   def post(self):
      username = self.get_argument('username', default='')
      password = self.get_argument('password', default='')
      passvali = self.get_argument('passvali', default='')
      uemail = self.get_argument('email', default='')
      users = db.user
      if password == passvali:
          uname = users.find_one({"username": username})
          if uname != None:
              self.write('<script language="javascript">alert("用户名已被占用");self.location="/signup";</script>')
          else:
              psw = hashlib.md5(password).hexdigest()
              avatar = '/static/images/avatar/' + 'avatar-'+ str(random.randint(1,16)) +'.svg'
              newuser = User(username, psw, uemail, 'master', 2, avatar)
              result = users.insert_one(newuser.getValue()).inserted_id
              self.set_secure_cookie('username', username)
              self.write('<script language="javascript">alert("注册成功");self.location="/signin";</script>')
      else:
          self.write('<script language="javascript">alert("密码不匹配");self.location="/signup";</script>')

class SignOut(SignValidateBase):
   def get(self):
      self.clear_cookie('username')
      self.redirect('/')