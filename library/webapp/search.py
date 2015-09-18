import os

from django.conf import settings
from django.db import connection
from django.db.models import Q
from django.utils.encoding import DjangoUnicodeDecodeError

from webapp import models
from webapp import config
from webapp import query

show_fields = ['title', 'author', 'isbn', 'dewey', 'cover'] # does not have any effect - just a note

readerware_fields = ['title', 'isbn', 'dewey']
author_fields = ['author']
fields = [
    readerware_fields,
    author_fields
]

def do_search(field, keyword):
    #TODO: need to refactor the function to search fields other than those in the Readerware table
    # e.g. author(contributor), language, etc.
    
    table_is = None
    result = []

    if field in readerware_fields:
        table_is = 'readerware'

    if field in author_fields:
        table_is = 'contributor'

    if table_is:
        if table_is != 'readerware':
            pass

        else:
            result = query.get_book_info(field, keyword)

    return result
