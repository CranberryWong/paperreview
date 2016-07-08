#!/usr/bin/env python
# -*- coding:utf-8 -*-

from handlers import main, auth

handlers = [
            (r"/", main.MainHandler),
            (r"/paper/([0-9a-zA-Z\-]*)", main.PaperHandler),
            (r"/user/([0-9a-zA-Z\-]*)", main.UserHandler),

            #User Profile
            (r"/signin", auth.SignIn),
            (r"/signup", auth.SignUp),
            (r"/signout", auth.SignOut),

    ]