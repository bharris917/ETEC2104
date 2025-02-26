import mako.template
import os.path
import datetime

srcdir = os.path.dirname(__file__)

#lookup = mako.lookup.TemplateLookup(
#    directories
#)

def get(): 
    today=datetime.datetime.now()
    T = mako.template.Template(filename=f"html/signup.html")
    return T.render(
        today=f"{today.month}/{today.day}/{today.year}"
    )
    