from django.template.loader import get_template
from django.shortcuts import render

from django.http import HttpResponse
import json

from webapp import query
from webapp import api


def book_info_by_barcode(request, book_id):
    # return:
    # -1: no barcode matches found. (default result)
    # -2: other errors

    # barcode is the unique string assigned to the books in library

    result = None
    template = '404.html'
    context = {}

    #TODO: this one is nasty - either update the models or write a generic raw query in query.py

    try:
        context = query.get_book_info('call_number', book_id)[0]

    #todo: fix the exception part
    except Exception as e:
        template = '404.html'
        result = render(request, '404.html')
        print e

    if context:
        template = 'pages/book_detail.html'

    result = render(request, template, context)

    return result


def home_page_render(request):
    context = {}
    result = None
    template = 'pages/home.html'

    result = render(request, template, context)

    return result


def search_page_render(request):
    #TODO: retrieve look-up field and keyword from GET form/request
    context = {}
    result = None
    template = 'pages/search.html'

    result = render(request, template, context)

    return result

def echo(request):

    result = {
        'title' : 'My Title',
        'content' : 'My Book Content'

    }

    json_result = json.dumps(result)

    return HttpResponse(json_result, content_type="application/json")
