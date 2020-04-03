from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import requests
from html.parser import HTMLParser

links = []
URL = 'http://vmcrawl.southeastasia.cloudapp.azure.com/super_secret_path/'

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data != "\n":
            links.append(data)

def index(request):
    r = requests.get(url=URL)

    raw_content = r.text

    parser = MyHTMLParser()
    parser.feed(raw_content)

    context = {'linklist': links}

    # return render(request, 'index.html', context)
    template = loader.get_template('linklister/index.html')

    return HttpResponse(template.render(context, request))