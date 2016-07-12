#!/usr/bin/env python
# -*- coding:utf-8 -*-

from handlers import main, auth, search, admin, util

handlers = [
            (r"/", main.MainHandler),
            (r"/paper/([0-9a-zA-Z\-]*)", main.PaperShowHandler),
            (r"/paper/([0-9a-zA-Z\-]*)/commit", main.PaperCommitHandler),
            (r"/paper/([0-9a-zA-Z\-]*)/revise", main.PaperReviseHandler),
            (r"/user/([0-9a-zA-Z\-]*)", main.UserHomeHandler),
            (r"/user/([0-9a-zA-Z\-]*)/profile", main.UserProfileHandler),
            (r'/q/date/([0-9]+)/([0-9]+)',main.ListByDate),
            (r'/type/([0-9a-zA-Z]*)', main.ListByType),
            (r"/upload",util.ImageUpload),

            #User Profile
            (r"/signin", auth.SignIn),
            (r"/signup", auth.SignUp),
            (r"/signout", auth.SignOut),


            #Search Item
            (r"/search", search.SearchListHandler),

            #Admin Handler
            #(r"/admin/signin", admin.SignInHandler),
            #(r"/admin/signout", admin.SignOutHandler),
            (r"/admin", admin.AdminMainHandler),
            (r"/admin/role", admin.RoleReviseHandler),
            (r"/admin/auth", admin.AuthReviseHandler),
            
    ]