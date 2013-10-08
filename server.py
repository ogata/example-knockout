# -*- coding: utf-8 -*-

import cherrypy
import os

dir = os.path.dirname(os.path.abspath(__file__))

conf = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8080,
    },
    '/examples': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'pages',
        'tools.staticdir.root': dir,
        'tools.staticdir.index': 'index.htm',
    }
}

cherrypy.quickstart(None, '/app', conf)

