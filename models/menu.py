# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = 'in-telligence'
response.subtitle = T('submit your resume')

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Radu Fericean <radu@fericean.ro>'
response.meta.description = 'Application for submitting resumes'
response.meta.keywords = 'in-telligence, resume, cv'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    ]

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller    
_()

