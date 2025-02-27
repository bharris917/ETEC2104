import cherrypy
import os.path
import random

#we have modules for each page we're displaying 
import page_index
import page_signup
import page_posts
import page_test
import mako.template
import quotes
import names

BASEDIR=os.path.abspath( os.path.dirname(__file__) )

class App:
    @cherrypy.expose
    def index(self):
        return page_index.get()
    @cherrypy.expose
    def signup(self):
        return page_signup.get()
    @cherrypy.expose
    def posts(self):
        return page_posts.get()
    @cherrypy.expose
    def test(self):
        return page_test.get()
    
    @cherrypy.expose
    def quote(self):
        d = os.path.dirname(__file__)
        t = mako.template.Template(
            filename=f"{d}/quote.html")
        q = random.choice(quotes.quotations)
        return t.render(quote=q)
    
    @cherrypy.expose
    def name(self):
        d = os.path.dirname(__file__)
        t = mako.template.Template(
            filename=f"{d}html/index.html")
        q = random.choice(names.name)
        return t.render(name=q)
    
    @cherrypy.expose
    def updateprofile(self):
        with open(f"{BASEDIR}/../html/updateprofile.html") as fp:
            return fp.read()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def do_update(self, name, birthday, pic ):
        print("name is:",name)
        print("birthday is:",birthday)
        print("pic is:",pic)
        tmp = pic.file.read()
        #just print first 10 bytes
        print("pic is:",tmp[:10])
        return {"ok": True }
        
#the location where the main.py file is stored: The src folder
srcdir = os.path.abspath(os.path.dirname(__file__))

app = App()
cherrypy.quickstart(
    app,
    '/',
    {
        "/html": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": f"{srcdir}/../html"
        }
    }
)
