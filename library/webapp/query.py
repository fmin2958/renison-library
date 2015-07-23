from urllib2 import urlopen
import urllib
import json

from django.conf import settings
from django.db import connection

from webapp import models

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


def get_book_info(keyword):
    # the function will be get_book_info(columns, keyword)
    # columns: a list that contains columns that needs to be displayed
    # keyword: the keyword for searching books
    # TODO: the keyword is currently limited to BARCODE, need to refector the
    # function to accept any arbitrary keywords (more than 1)

    rows = run_query('select * from WEBAPP_CONFIGURATION where name like "%get_book_info%" and value = "1"')

    query = 'select '
    need_join = 0
    title_at = None
    cover_at = None
    title_indicator = ''
    cover_indicator = ''
    count = 0
    columns= []
    book_cover_config = models.WebappConfiguration.objects.filter(name = 'book_cover_api_config')

    cover_id = models.Readerware.objects.filter(barcode = keyword).values('rowkey')[0]['rowkey']

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

        query += 'where BARCODE = "%s"' % (keyword)

    query_result = run_query(query)

    values = list(query_result[0])

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

    result = {'content': content, 'title': title, 'cover': cover}

    return result


def get_book_cover_default():

    query_result = query_result = models.WebappConfiguration.objects.filter(name = 'book_cover_api_config')
    
    return query_result.values('value')[0]['value'] + query_result.values('value_1')[0]['value_1']


def get_book_cover(keyword):
    #need test - not functioning as expected
    print 'finding book cover of: %s' % keyword
    print
    query_result = models.WebappConfiguration.filter(name = 'book_cover_api_config')

    try:
        result = models.BookCover.objects.filter(book_id = keyword).values('image_url')[0]['image_url']

    except Exception, e:
        print e

        #default image
        print 'image not found - using default image'
        result = get_book_cover_default()

    return result


def update_book_cover(keyword):
    request = ''
    image_url = ''
    file_name = ''
    file_dir = ''

    query_result = models.WebappConfiguration.filter(name = 'book_cover_api_config')

    file_dir = query_result.values('value')[0]['value']

    item = models.Readerware.objects.filter(isbn = keyword)

    book_id = item.values('rowkey')[0]['rowkey']

    all_api = models.WebappConfiguration.objects.filter(name__icontains = 'book_cover_api').values()

    for api in all_api:
        if api[1] and not image_url:
            request = api[1] + keyword + api[2]

            try:
                image_url = json.loads(urlopen(request).read())[api[3]]

            except KeyError:
                print 'cannot find image / json key does not match'
                image_url = ''

            except Exception, e:
                print e
                image_url = ''

    if image_url:

        file_name = image_url.split('/')[-1]
        file_dir += file_name

        try:
            urllib.urlretrieve(image_url, file_dir)

        except Exception, e:
            print e

            file_name = None


        models.BookCover(book_id = book_id, image_dir = file_dir).save()

    return
