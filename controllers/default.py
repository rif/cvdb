# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

def index():
    profile, contact, projects, skills = (None, None, None, None)
    if auth.user:
        profile = db(db.userprofile.created_by == auth.user_id).select().first()
        contact = db(db.contactinfo.created_by == auth.user_id).select().first()        
        projects = db(db.entry.created_by == auth.user_id).select()
        skills = db(db.skill.created_by == auth.user_id).select()
    if a0 == 'public':
        response.view = 'default/public.html'
    return locals()

@auth.requires_signature()
def edit_profile():
    if not a0 and db(db.userprofile.created_by == auth.user_id).count() >= 1 : return HTTP(403)
    title = T('Profile')    
    form = crud.update(db.userprofile, a0)    
    response.view = 'default/form.html'
    return locals()

@auth.requires_signature()
def edit_contact():
    if not a0 and db(db.contactinfo.created_by == auth.user_id).count() >= 1: return HTTP(403)
    title = T('Contact Info')
    form = crud.update(db.contactinfo, a0)    
    response.view = 'default/form.html'
    return locals()

@auth.requires_signature()
def edit_entry():
    if not a0 and db(db.entry.created_by == auth.user_id).count() >= MAX_ENTRIES - 1: return HTTP(403)
    title = T('Project')
    form = crud.update(db.entry, a0)    
    response.view = 'default/form.html'
    return locals()

@auth.requires_signature()
def edit_skill():
    if not a0 and db(db.skill.created_by == auth.user_id).count() >= MAX_SKILLS: return HTTP(403)
    title = T('Skill')
    form = crud.update(db.skill, a0)    
    response.view = 'default/form.html'
    return locals()

def user():
    return dict(form=auth())

def download():
    return response.download(request,db)
