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

    response = HttpResponse(result, content_type="application/json; charset=UTF-8", status=status)

    response['status'] = status

    response['Access-Control-Allow-Origin'] = '*'

    return response

def get_book_list(request):

    result = search.get_all_book()

    if 'error' in result:
        status = 400

    else:
        status = 200

    response = HttpResponse(result, content_type="application/json; charset=UTF-8", status=status)

    response['status'] = status

    response['Access-Control-Allow-Origin'] = '*'

    return response


def get_book_detail(request, book_id):
    # return:
    # -1: no barcode matches found. (default result)
    # -2: other errors

    # barcode is the unique string assigned to the books in library

    result = None
    result = {}

    print book_id

    #TODO: this one is nasty - either update the models or write a generic raw query in query.py

    try:
        result = query.get_book_info('call_number', book_id)[0]

    #todo: fix the exception part
    except Exception as e:
        result['error'] = 400
        print e

    if 'error' in result:
        status = 400

    else:
        status = 200

    result = json.dumps(result)

    response = HttpResponse(result, content_type="application/json; charset=UTF-8", status=status)

    response['status'] = status

    response['Access-Control-Allow-Origin'] = '*'

    return response
