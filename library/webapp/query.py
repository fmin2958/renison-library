from django.db import connection

from webapp import models

#TODO: this one is nasty - either update the models or write a generic raw query in query.py

def run_query(query):
    #print "running query: '%s'" % query
    cursor = connection.cursor()
    cursor.execute(query)
    result = ()

    try:
        result = cursor.fetchall()

    except Exception as e:
        print e

    #print result

    return result


def get_book_info(keyword):
    # the function will be get_book_info(columns, keyword)
    # columns: a list that contains columns that needs to be displayed
    # keyword: the keyword for searching books
    # TODO: the keyword is currently limited to BARCODE, need to refector the
    # function to accept any arbitrary keywords (more than 1)

    rows = run_query('select * from WEBAPP_CONFIGURATION where value = "1" and name like "%get_book_info%"')

    query = 'select '
    need_join = 0
    title_at = -1
    cover_at = -1
    title_indicator = ''
    cover_indicator = ''
    count = 0
    columns= []

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
        cover = values[title_at]

    content = dict(zip(columns, values))

    if title_indicator:
        del content[title_indicator]
    if cover_indicator:
        del content[cover_indicator]

    result = {'content': content, 'title': title, 'cover': cover}

    return result


#def get_book_cover(keyword):
