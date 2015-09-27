from django.template.loader import get_template
from django.shortcuts import render

from webapp import query
from webapp import search

from django.http import HttpResponse
import json

def get_book_search(request):
    field = request.GET.get('field', 'null')
    keyword = request.GET.get('keyword', 'null')

    result = json.dumps({})

    result = search.do_search(field, keyword)

    if 'error' in result:
        status = 400

    else:
        status = 200

    response = HttpResponse(result, content_type="application/json", status=status)

    return response

def get_book_list(request):

    result = search.get_all_book()

    if 'error' in result:
        status = 400

    else:
        status = 200

    response = HttpResponse(result, content_type="application/json", status=status)

    return response
