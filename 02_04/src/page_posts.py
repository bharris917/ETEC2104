import mako.template
import os.path
import datetime
import random
import pictures
import titles

srcdir = os.path.dirname(__file__)



#lookup = mako.lookup.TemplateLookup(
#    directories
#)

def get(): 
    x = datetime.timedelta(minutes=random.randrange(8000))
    hoursago = int( x.seconds / 3600 )
    minutesago = round( (x.seconds - hoursago*3600)/60 )
    today=datetime.datetime.now()
    T = mako.template.Template(filename=f"html/posts.html")
    q = random.choice(titles.title)
    return T.render(name1 = random.choice(titles.title),
                    name2 = random.choice(titles.title),
                    name3 = random.choice(titles.title),
                    name4 = random.choice(titles.title),
                    name5 = random.choice(titles.title),
                    name6 = random.choice(titles.title),
                    name7 = random.choice(titles.title),
                    name8 = random.choice(titles.title),
                    name9 = random.choice(titles.title),
                    name10 = random.choice(titles.title),
                    pic1 = random.choice(pictures.pics),
                    pic2 = random.choice(pictures.pics),
                    pic3 = random.choice(pictures.pics),
                    pic4 = random.choice(pictures.pics),
                    pic5 = random.choice(pictures.pics),
                    pic6 = random.choice(pictures.pics),
                    pic7 = random.choice(pictures.pics),
                    pic8 = random.choice(pictures.pics),
                    pic9 = random.choice(pictures.pics),
                    pic10 = random.choice(pictures.pics),
        today1=f"{x.days} days, {hoursago} hours, and {minutesago} minutes ago"
    )
    