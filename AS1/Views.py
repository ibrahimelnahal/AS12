# coding=utf-8
from django.template.loader import get_template
from django.http import Http404, HttpResponse
from django.template import Template, Context
import datetime

''''3''''''
def hello(request):
    return HttpResponse('Hello World')


def current_datetime(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It's {{ current_date }}.</body></html>")
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

''''''''''''
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>lt is %s</body></html>" % now
    return HttpResponse(html)
'''

'''''''''
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = '<html><body>In %s hour(s), it’ll be %s.</body></html>' % (offset, dt)
    return HttpResponse(html)
'''
def wordcount(request):
    file = get_template('mytext.html').render()
    wordcount={}
    for word in file.split():
        if word not in wordcount:
                 wordcount[word] = 1
        else:
                 wordcount[word] += 1

    for k,v in wordcount.items():
        print k,v
    mt = get_template('MyTemplate.html')
    html = mt.render(Context({'word':wordcount.items()}))
    return HttpResponse(html)