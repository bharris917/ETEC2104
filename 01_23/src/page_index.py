import mako.template
import os.path
import random

#demo
import datetime
import names

#location of this file
srcdir = os.path.dirname(__file__)

name = ["Dave, John, Jane"]

def get():
    t = mako.template.Template(
        filename=f"html/index.html")
    q = random.choice(names.name)
    return t.render(name=q)