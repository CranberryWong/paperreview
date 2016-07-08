#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options

from tornado.options import define, options

from urls import handlers


define('port', default=8000, help='run on the given port', type=int)

class Application(tornado.web.Application):
    def __init__(self, handlers):    
        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), 'templates'),
            static_path = os.path.join(os.path.dirname(__file__), 'static'),
            debug = True,   
            cookie_secret = "dEr2Viz6TrqsoQVbQCRdxUmzKB5q40U0jYtp+fnsAOY=",
            login_url = "/signin",
            autoescape = None,         
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(handlers))
    http_server.listen(options.port)
    print 'Development server is running at http://127.0.0.1:%s/' % options.port
    print 'Quit the server with Ctrl-C'
    tornado.ioloop.IOLoop.instance().start()
    
if __name__ == '__main__':
    main()