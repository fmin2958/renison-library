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
author_fields = ['author', 'author2', 'author3', 'author4', 'author5', 'author6']
fields = [
    readerware_fields,
    author_fields
]

def get_author_id_list(keywords):
    result = []

    authors = models.Contributor.objects.all()
    for item in keywords:
        authors = authors.filter(name__icontains=item)

    if authors:
        for item in authors:
            result.append(item.rowkey)

    print result
    print

    return result


def do_search(field, keyword):
    #TODO: need to refactor the function to search fields other than those in the Readerware table
    # e.g. author(contributor), language, etc.

    table_is = None
    result = []

    print field, keyword

    if keyword:
        keyword = keyword.replace(',', ' ').replace(';', ' ').replace('+', ' ').split()

        if field == 'title':
            result = query.get_book_info('title', keyword)

        elif field == 'author':
            author_keywords = get_author_id_list(keyword)

            if keyword:
                for author_keyword in author_keywords:
                    for author_field in author_fields:
                        search_result = query.get_book_info(author_field, author_keyword, is_exact=True)
                        if search_result:
                            result += search_result

        elif field == 'isbn':
            result = query.get_book_info('isbn', keyword)

    return result
