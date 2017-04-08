# !/usr/bin/env python
# -*- coding: utf-8 -*-
#

import web

# Templates
rend = web.template.render('/home/pcanales/templates')

# URL's
urls = (
    '/', 'index1',
    '/add', 'add'
    '/delete/id', 'delete'
)

# Database

dB = web.database(dbn='postgres', user='postgres', pw='mafepa', db='myweb')

# App

app = web.application(urls, globals())

class index1:
    def GET(self):
        todos = dB.select('todo')
        return rend.index1(todos)

class add:
    def POST(self, identificador):
        print identificador
        #i = web.input()
        #n = dB.insert('todo', title = i.title)
        raise web.seeother('/')

class delete:
    def POST(self):
#        j = web.input()
#        print j
#        db.delete('todo', id = j.id)
        raise web.seeother('/')

if __name__ == "__main__": app.run()