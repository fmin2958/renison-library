import os

from urllib2 import urlopen
import urllib
import json

from django.conf import settings
from django.db import connection
from django.utils.encoding import DjangoUnicodeDecodeError

from webapp import models

from webapp import config

#TODO: this one is nasty - either update the models or write a generic raw query in query.py

def run_query(query):
    print "running query: %s" % query
    print
    cursor = connection.cursor()
    cursor.execute(query)
    result = ()

    try:
        result = cursor.fetchall()

    except Exception as e:
        print e

    print ("query result: ", result)
    print

    return result


def get_book_info(field, keyword):
    # the function will be get_book_info(columns, keyword)
    # columns: a list that contains columns that needs to be displayed
    # keyword: the keyword for searching books

    # NOTE: function is refactored, now accepts fields in the Readerware table
    # need more testing.

    # NOTE: returned value changed: now returns a list of dict,
    # i.e. result[0] is the original expected output.

    rows = run_query('select * from WEBAPP_CONFIGURATION where name like "%get_book_info%" and value = "1"')

    query = 'select '
    need_join = 0
    title_at = None
    cover_at = None
    title_indicator = u''
    cover_indicator = u''
    count = 0
    columns= []

    book_cover_config = models.WebappConfiguration.objects.filter(name = 'book_cover_api_config')

    result = []

    print 'flag'

    if rows:
        for item in rows:
            query += '%s.%s, ' % (item[3], item[5])
            columns.append(item[2])

            if item[2].lower() == 'title':
                title_at = count
                title_indicator = item[2]

            if item[2].lower() == 'cover':
                cover_at = count
                cover_indicator = item[2]

            if item[4]:
                need_join = 1

            count += 1

        query = query[:-2]

        query += ' from READERWARE '

        if need_join:
            for item in rows:
                if item[4]:
                    query += 'left join %s on %s.%s = %s.%s ' % (item[3], item[4], item[7], item[3], item[6])

        query += 'where READERWARE.%s like "%%%s%%"' % (field, keyword)

    query_result = run_query(query)

    values = list(query_result[0])

    for item in query_result:
        values = list(item)

        if title_indicator:
            title = values[title_at]

        if cover_indicator:
            cover = values[cover_at]

        if not cover:
            cover = get_book_cover_default()


        content = dict(zip(columns, values))

        if title_indicator:
            del content[title_indicator]
        if cover_indicator:
            del content[cover_indicator]

        result.append({'content': content, 'title': title, 'cover': cover})

    return result


def get_book_cover_default():
    return config.DEFAULT_COVER_FILE_PATH


def get_book_cover(keyword):
    #TODO: should be working, not tested
    result = u''
    print 'finding book cover of: %s' % keyword
    print

    try:
        result = models.BookCover.objects.filter(book_id = keyword).values('image_url')[0]['image_url']

    except Exception, e:
        print e

        #default image
        print 'image not found - using default image'
        result = get_book_cover_default()

    return result


def update_book_cover(keyword):
    result = False
    request = u''
    image_url = u''
    file_name = u''
    file_dir = u''

    file_dir = config.COVER_PATH

    item = models.Readerware.objects.filter(isbn = keyword)

    if item:
        book_id = item.values('rowkey')[0]['rowkey']

        all_api = models.WebappConfiguration.objects.filter(name__icontains = 'book_cover_api_get_by').values()

        for api in all_api:

            if api['value'] and not image_url:
                request = api['value'] + keyword + api['value_1']

                try:
                    image_url = json.loads(urlopen(request).read())[api['value_2']]

                except KeyError:
                    print 'cannot find image / json key does not match'
                    image_url = u''

                except Exception, e:
                    print e
                    image_url = u''

        if image_url:

            file_name = image_url.split('/')[-1]
            file_dir += file_name

            try:
                urllib.urlretrieve(image_url, os.path.join(settings.STATIC_PATH, file_dir))

            except Exception, e:
                print e

                file_name = None

            models.BookCover(book_id = book_id, image_dir = file_dir).save()

            result = True

        else:
            print 'no image found for book with given isbn (%s)' % keyword

    else:
        print 'book with given isbn (%s) does not exist in database.' % keyword

    return result


def update_book_cover_all():
    success_count = 0

    items = models.Readerware.objects.exclude(isbn__isnull = True)
    items_length = items.count()

    print 'updating %s books\' cover' % items_length
    print

    for index in range(0, items_length):
        print 'updating %s / %s book\'s cover' % (index + 1, items_length)
        #TODO: need to be updated when migrating to py3

        #TODO: known bug: UnicodeDecodeError will be thrown if the db uses BOM it should be fixed on the db side so exception is supressed.

        try:
            update_result = update_book_cover(items[index].isbn)
        except DjangoUnicodeDecodeError:
            print 'Unicode Error Encountered.'
            pass

        else:
            if update_result:
                success_count += 1

    print '%s / %s covers updated.' % (success_count, items_length)
    print

    return
