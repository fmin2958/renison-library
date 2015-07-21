from django.db import connection

from webapp import models

#TODO: this one is nasty - either update the models or write a generic raw query in query.py
def get_book_info(keyword):
    # the function will be get_book_info(columns, keyword)
    # columns: a list that contains columns that needs to be displayed
    # keyword: the keyword for searching books
    # TODO: the keyword is currently limited to BARCODE, need to refector the
    # function to accept any arbitrary keywords (more than 1)

    columns = ['Title', 'ISBN', 'DEWEY', 'Author']

    arguments = ['READERWARE.TITLE', 'READERWARE.ISBN', 'READERWARE.DEWEY', 'CONTRIBUTOR.NAME']
    arguments.append(keyword)

    query = 'select %s, %s, %s, %s from READERWARE inner join CONTRIBUTOR on READERWARE.AUTHOR=CONTRIBUTOR.ROWKEY where BARCODE="%s";' % tuple(arguments)

    cursor = connection.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    values = list(row)

    title = values.pop(0)
    columns.pop(0)

    content = dict(zip(columns, values))

    result = {'content': content, 'title': title}

    return result
