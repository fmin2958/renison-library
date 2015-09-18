from django.template.loader import get_template
from django.shortcuts import render

from webapp import query

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
        template = 'book_page.html'

    result = render(request, template, context)

    return result
