# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class BookCover(models.Model):
    book_id = models.BigIntegerField(db_column='BOOK_ID', primary_key=True)  # Field name made lowercase.
    image_dir = models.CharField(db_column='IMAGE_DIR', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOOK_COVER'


class Borrower(models.Model):
    brwr_rowkey = models.BigIntegerField(db_column='BRWR_ROWKEY', primary_key=True)  # Field name made lowercase.
    brwr_fname = models.CharField(db_column='BRWR_FNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    brwr_lname = models.CharField(db_column='BRWR_LNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    brwr_id = models.CharField(db_column='BRWR_ID', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    brwr_status = models.IntegerField(db_column='BRWR_STATUS', blank=True, null=True)  # Field name made lowercase.
    brwr_email = models.CharField(db_column='BRWR_EMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    brwr_phone1 = models.CharField(db_column='BRWR_PHONE1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    brwr_phone2 = models.CharField(db_column='BRWR_PHONE2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    brwr_fax = models.CharField(db_column='BRWR_FAX', max_length=32, blank=True, null=True)  # Field name made lowercase.
    brwr_org = models.CharField(db_column='BRWR_ORG', max_length=100, blank=True, null=True)  # Field name made lowercase.
    brwr_addr1 = models.CharField(db_column='BRWR_ADDR1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    brwr_addr2 = models.CharField(db_column='BRWR_ADDR2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    brwr_city = models.CharField(db_column='BRWR_CITY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    brwr_state = models.CharField(db_column='BRWR_STATE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    brwr_zip = models.CharField(db_column='BRWR_ZIP', max_length=32, blank=True, null=True)  # Field name made lowercase.
    brwr_user1 = models.CharField(db_column='BRWR_USER1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    brwr_user2 = models.CharField(db_column='BRWR_USER2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    brwr_filler1 = models.CharField(db_column='BRWR_FILLER1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    brwr_filler2 = models.CharField(db_column='BRWR_FILLER2', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BORROWER'


class CategoryList(models.Model):
    rowkey = models.BigIntegerField(db_column='ROWKEY', primary_key=True)  # Field name made lowercase.
    listitem = models.CharField(db_column='LISTITEM', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATEGORY_LIST'


class ConditionList(models.Model):
    rowkey = models.BigIntegerField(db_column='ROWKEY', primary_key=True)  # Field name made lowercase.
    listitem = models.CharField(db_column='LISTITEM', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONDITION_LIST'


class Contributor(models.Model):
    rowkey = models.BigIntegerField(db_column='ROWKEY', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=128)  # Field name made lowercase.
    sort_name = models.CharField(db_column='SORT_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    role1 = models.IntegerField(db_column='ROLE1', blank=True, null=True)  # Field name made lowercase.
    role2 = models.IntegerField(db_column='ROLE2', blank=True, null=True)  # Field name made lowercase.
    role3 = models.IntegerField(db_column='ROLE3', blank=True, null=True)  # Field name made lowercase.
    bio = models.TextField(db_column='BIO', blank=True, null=True)  # Field name made lowercase.
    favorite = models.IntegerField(db_column='FAVORITE')  # Field name made lowercase.
    birth_date = models.DateField(db_column='BIRTH_DATE', blank=True, null=True)  # Field name made lowercase.
    birth_place = models.CharField(db_column='BIRTH_PLACE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    death_date = models.DateField(db_column='DEATH_DATE', blank=True, null=True)  # Field name made lowercase.
    death_place = models.CharField(db_column='DEATH_PLACE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='NOTES', blank=True, null=True)  # Field name made lowercase.
    contrib_url = models.CharField(db_column='CONTRIB_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    image_data = models.TextField(db_column='IMAGE_DATA', blank=True, null=True)  # Field name made lowercase.
    external_id = models.CharField(db_column='EXTERNAL_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    user1 = models.CharField(db_column='USER1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user2 = models.CharField(db_column='USER2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    filler1 = models.CharField(db_column='FILLER1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    filler2 = models.CharField(db_column='FILLER2', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTRIBUTOR'


class Dbcatalog(models.Model):
    ev = models.DateField(db_column='EV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DBCATALOG'


class EditionList(models.Model):
    rowkey = models.BigIntegerField(db_column='ROWKEY', primary_key=True)  # Field name made lowercase.
    listitem = models.CharField(db_column='LISTITEM', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EDITION_LIST'


class FormatList(models.Model):
    rowkey = models.BigIntegerField(db_column='ROWKEY', primary_key=True)  # Field name made lowercase.
    listitem = models.CharField(db_column='LISTITEM', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FORMAT_LIST'


class LanguageList(models.Model):
    rowkey = models.BigIntegerField(db_column='ROWKEY', primary_key=True)  # Field name made lowercase.
    listitem = models.CharField(db_column='LISTITEM', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LANGUAGE_LIST'


class Loans(models.Model):
    ln_rowkey = models.BigIntegerField(db_column='LN_ROWKEY', primary_key=True)  # Field name made lowercase.
    ln_item_rowkey = models.BigIntegerField(db_column='LN_ITEM_ROWKEY')  # Field name made lowercase.
    ln_brwr_rowkey = models.BigIntegerField(db_column='LN_BRWR_ROWKEY')  # Field name made lowercase.
    ln_item_copy_id = models.CharField(db_column='LN_ITEM_COPY_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ln_status = models.IntegerField(db_column='LN_STATUS', blank=True, null=True)  # Field name made lowercase.
    ln_out_date = models.DateField(db_column='LN_OUT_DATE')  # Field name made lowercase.
    ln_due_date = models.DateField(db_column='LN_DUE_DATE', blank=True, null=True)  # Field name made lowercase.
    ln_in_date = models.DateField(db_column='LN_IN_DATE', blank=True, null=True)  # Field name made lowercase.
    ln_user1 = models.CharField(db_column='LN_USER1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ln_user2 = models.CharField(db_column='LN_USER2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ln_filler1 = models.CharField(db_column='LN_FILLER1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ln_filler2 = models.CharField(db_column='LN_FILLER2', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOANS'


class LocationList(models.Model):
    rowkey = models.BigIntegerField(db_column='ROWKEY', primary_key=True)  # Field name made lowercase.
    listitem = models.CharField(db_column='LISTITEM', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOCATION_LIST'


class MyRatingList(models.Model):
    rowkey = models.BigIntegerField(db_column='ROWKEY', primary_key=True)  # Field name made lowercase.
    listitem = models.CharField(db_column='LISTITEM', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MY_RATING_LIST'


class OwnerList(models.Model):
    rowkey = models.BigIntegerField(db_column='ROWKEY', primary_key=True)  # Field name made lowercase.
    listitem = models.CharField(db_column='LISTITEM', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OWNER_LIST'


class PublicationPlaceList(models.Model):
    rowkey = models.BigIntegerField(db_column='ROWKEY', primary_key=True)  # Field name made lowercase.
    listitem = models.CharField(db_column='LISTITEM', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PUBLICATION_PLACE_LIST'


class PublisherList(models.Model):
    rowkey = models.BigIntegerField(db_column='ROWKEY', primary_key=True)  # Field name made lowercase.
    listitem = models.CharField(db_column='LISTITEM', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PUBLISHER_LIST'


class PurchasePlaceList(models.Model):
    rowkey = models.BigIntegerField(db_column='ROWKEY', primary_key=True)  # Field name made lowercase.
    listitem = models.CharField(db_column='LISTITEM', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PURCHASE_PLACE_LIST'


class Readerware(models.Model):
    rowkey = models.BigIntegerField(db_column='ROWKEY', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=255)  # Field name made lowercase.
    alt_title = models.CharField(db_column='ALT_TITLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subtitle = models.CharField(db_column='SUBTITLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    author = models.BigIntegerField(db_column='AUTHOR', blank=True, null=True)  # Field name made lowercase.
    author2 = models.BigIntegerField(db_column='AUTHOR2', blank=True, null=True)  # Field name made lowercase.
    author3 = models.BigIntegerField(db_column='AUTHOR3', blank=True, null=True)  # Field name made lowercase.
    author4 = models.BigIntegerField(db_column='AUTHOR4', blank=True, null=True)  # Field name made lowercase.
    author5 = models.BigIntegerField(db_column='AUTHOR5', blank=True, null=True)  # Field name made lowercase.
    author6 = models.BigIntegerField(db_column='AUTHOR6', blank=True, null=True)  # Field name made lowercase.
    illustrator = models.BigIntegerField(db_column='ILLUSTRATOR', blank=True, null=True)  # Field name made lowercase.
    translator = models.BigIntegerField(db_column='TRANSLATOR', blank=True, null=True)  # Field name made lowercase.
    editor = models.BigIntegerField(db_column='EDITOR', blank=True, null=True)  # Field name made lowercase.
    publisher = models.BigIntegerField(db_column='PUBLISHER', blank=True, null=True)  # Field name made lowercase.
    pub_place = models.BigIntegerField(db_column='PUB_PLACE', blank=True, null=True)  # Field name made lowercase.
    release_date = models.DateField(db_column='RELEASE_DATE', blank=True, null=True)  # Field name made lowercase.
    copyright_date = models.DateField(db_column='COPYRIGHT_DATE', blank=True, null=True)  # Field name made lowercase.
    pages = models.IntegerField(db_column='PAGES', blank=True, null=True)  # Field name made lowercase.
    edition = models.BigIntegerField(db_column='EDITION', blank=True, null=True)  # Field name made lowercase.
    content_language = models.BigIntegerField(db_column='CONTENT_LANGUAGE', blank=True, null=True)  # Field name made lowercase.
    signed = models.BigIntegerField(db_column='SIGNED', blank=True, null=True)  # Field name made lowercase.
    dimensions = models.CharField(db_column='DIMENSIONS', max_length=32, blank=True, null=True)  # Field name made lowercase.
    reading_level = models.BigIntegerField(db_column='READING_LEVEL', blank=True, null=True)  # Field name made lowercase.
    lexile_level = models.CharField(db_column='LEXILE_LEVEL', max_length=14, blank=True, null=True)  # Field name made lowercase.
    copies = models.IntegerField(db_column='COPIES')  # Field name made lowercase.
    barcode = models.CharField(db_column='BARCODE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=14, blank=True, null=True)  # Field name made lowercase.
    issn = models.CharField(db_column='ISSN', max_length=16, blank=True, null=True)  # Field name made lowercase.
    lccn = models.CharField(db_column='LCCN', max_length=16, blank=True, null=True)  # Field name made lowercase.
    dewey = models.CharField(db_column='DEWEY', max_length=32, blank=True, null=True)  # Field name made lowercase.
    call_number = models.CharField(db_column='CALL_NUMBER', max_length=32, blank=True, null=True)  # Field name made lowercase.
    user_number = models.CharField(db_column='USER_NUMBER', max_length=32, blank=True, null=True)  # Field name made lowercase.
    type = models.BigIntegerField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
    format = models.BigIntegerField(db_column='FORMAT', blank=True, null=True)  # Field name made lowercase.
    series = models.BigIntegerField(db_column='SERIES', blank=True, null=True)  # Field name made lowercase.
    series_number = models.IntegerField(db_column='SERIES_NUMBER', blank=True, null=True)  # Field name made lowercase.
    my_rating = models.BigIntegerField(db_column='MY_RATING', blank=True, null=True)  # Field name made lowercase.
    item_condition = models.BigIntegerField(db_column='ITEM_CONDITION', blank=True, null=True)  # Field name made lowercase.
    cover_condition = models.BigIntegerField(db_column='COVER_CONDITION', blank=True, null=True)  # Field name made lowercase.
    category1 = models.BigIntegerField(db_column='CATEGORY1', blank=True, null=True)  # Field name made lowercase.
    category2 = models.BigIntegerField(db_column='CATEGORY2', blank=True, null=True)  # Field name made lowercase.
    category3 = models.BigIntegerField(db_column='CATEGORY3', blank=True, null=True)  # Field name made lowercase.
    location = models.BigIntegerField(db_column='LOCATION', blank=True, null=True)  # Field name made lowercase.
    keywords = models.CharField(db_column='KEYWORDS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    read_count = models.IntegerField(db_column='READ_COUNT')  # Field name made lowercase.
    date_last_read = models.DateField(db_column='DATE_LAST_READ', blank=True, null=True)  # Field name made lowercase.
    product_info = models.TextField(db_column='PRODUCT_INFO', blank=True, null=True)  # Field name made lowercase.
    my_comments = models.TextField(db_column='MY_COMMENTS', blank=True, null=True)  # Field name made lowercase.
    date_entered = models.DateField(db_column='DATE_ENTERED')  # Field name made lowercase.
    date_last_updated = models.DateField(db_column='DATE_LAST_UPDATED')  # Field name made lowercase.
    source = models.BigIntegerField(db_column='SOURCE', blank=True, null=True)  # Field name made lowercase.
    purchase_price = models.DecimalField(db_column='PURCHASE_PRICE', max_digits=12, decimal_places=2)  # Field name made lowercase.
    purchase_date = models.DateField(db_column='PURCHASE_DATE', blank=True, null=True)  # Field name made lowercase.
    purchase_place = models.BigIntegerField(db_column='PURCHASE_PLACE', blank=True, null=True)  # Field name made lowercase.
    list_price = models.DecimalField(db_column='LIST_PRICE', max_digits=12, decimal_places=2)  # Field name made lowercase.
    item_value = models.DecimalField(db_column='ITEM_VALUE', max_digits=12, decimal_places=2)  # Field name made lowercase.
    valuation_date = models.DateField(db_column='VALUATION_DATE', blank=True, null=True)  # Field name made lowercase.
    currency_symbol = models.CharField(db_column='CURRENCY_SYMBOL', max_length=5, blank=True, null=True)  # Field name made lowercase.
    favorite = models.IntegerField(db_column='FAVORITE')  # Field name made lowercase.
    out_of_print = models.IntegerField(db_column='OUT_OF_PRINT')  # Field name made lowercase.
    media_url = models.CharField(db_column='MEDIA_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    owner = models.BigIntegerField(db_column='OWNER', blank=True, null=True)  # Field name made lowercase.
    status = models.BigIntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    external_id = models.CharField(db_column='EXTERNAL_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    inventory = models.IntegerField(db_column='INVENTORY')  # Field name made lowercase.
    image1_data = models.TextField(db_column='IMAGE1_DATA', blank=True, null=True)  # Field name made lowercase.
    image2_data = models.TextField(db_column='IMAGE2_DATA', blank=True, null=True)  # Field name made lowercase.
    image1_large_data = models.TextField(db_column='IMAGE1_LARGE_DATA', blank=True, null=True)  # Field name made lowercase.
    image2_large_data = models.TextField(db_column='IMAGE2_LARGE_DATA', blank=True, null=True)  # Field name made lowercase.
    in_last_batch = models.IntegerField(db_column='IN_LAST_BATCH')  # Field name made lowercase.
    am_asin = models.CharField(db_column='AM_ASIN', max_length=14, blank=True, null=True)  # Field name made lowercase.
    sale_price = models.DecimalField(db_column='SALE_PRICE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sale_date = models.DateField(db_column='SALE_DATE', blank=True, null=True)  # Field name made lowercase.
    new_value = models.DecimalField(db_column='NEW_VALUE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    new_count = models.IntegerField(db_column='NEW_COUNT', blank=True, null=True)  # Field name made lowercase.
    used_value = models.DecimalField(db_column='USED_VALUE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    used_count = models.IntegerField(db_column='USED_COUNT', blank=True, null=True)  # Field name made lowercase.
    collectible_value = models.DecimalField(db_column='COLLECTIBLE_VALUE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    collectible_count = models.IntegerField(db_column='COLLECTIBLE_COUNT', blank=True, null=True)  # Field name made lowercase.
    buyer_waiting = models.IntegerField(db_column='BUYER_WAITING', blank=True, null=True)  # Field name made lowercase.
    weight = models.CharField(db_column='WEIGHT', max_length=32, blank=True, null=True)  # Field name made lowercase.
    sales_rank = models.IntegerField(db_column='SALES_RANK')  # Field name made lowercase.
    user1 = models.CharField(db_column='USER1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user2 = models.CharField(db_column='USER2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user3 = models.CharField(db_column='USER3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user4 = models.CharField(db_column='USER4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user5 = models.CharField(db_column='USER5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user6 = models.CharField(db_column='USER6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user7 = models.CharField(db_column='USER7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user8 = models.CharField(db_column='USER8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user9 = models.CharField(db_column='USER9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user10 = models.CharField(db_column='USER10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    filler1 = models.CharField(db_column='FILLER1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    filler2 = models.CharField(db_column='FILLER2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    filler3 = models.CharField(db_column='FILLER3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    filler4 = models.CharField(db_column='FILLER4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    filler5 = models.CharField(db_column='FILLER5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    filler6 = models.CharField(db_column='FILLER6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    filler7 = models.CharField(db_column='FILLER7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    filler8 = models.CharField(db_column='FILLER8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    filler9 = models.CharField(db_column='FILLER9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    filler10 = models.CharField(db_column='FILLER10', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'READERWARE'


class ReaderwareChapters(models.Model):
    rowkey = models.BigIntegerField(db_column='ROWKEY', primary_key=True)  # Field name made lowercase.
    vol = models.ForeignKey('ReaderwareVolumes', db_column='VOL_ID')  # Field name made lowercase.
    chp_number = models.IntegerField(db_column='CHP_NUMBER')  # Field name made lowercase.
    chp_title = models.CharField(db_column='CHP_TITLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chp_author = models.BigIntegerField(db_column='CHP_AUTHOR', blank=True, null=True)  # Field name made lowercase.
    chp_illustrator = models.BigIntegerField(db_column='CHP_ILLUSTRATOR', blank=True, null=True)  # Field name made lowercase.
    chp_translator = models.BigIntegerField(db_column='CHP_TRANSLATOR', blank=True, null=True)  # Field name made lowercase.
    chp_editor = models.BigIntegerField(db_column='CHP_EDITOR', blank=True, null=True)  # Field name made lowercase.
    chp_my_rating = models.BigIntegerField(db_column='CHP_MY_RATING', blank=True, null=True)  # Field name made lowercase.
    chp_favorite = models.IntegerField(db_column='CHP_FAVORITE')  # Field name made lowercase.
    chp_read_count = models.IntegerField(db_column='CHP_READ_COUNT')  # Field name made lowercase.
    chp_comments = models.CharField(db_column='CHP_COMMENTS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chp_media_url = models.CharField(db_column='CHP_MEDIA_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chp_user1 = models.CharField(db_column='CHP_USER1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chp_user2 = models.CharField(db_column='CHP_USER2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chp_filler1 = models.CharField(db_column='CHP_FILLER1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chp_filler2 = models.CharField(db_column='CHP_FILLER2', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'READERWARE_CHAPTERS'


class ReaderwareVolumes(models.Model):
    rowkey = models.BigIntegerField(db_column='ROWKEY', primary_key=True)  # Field name made lowercase.
    book = models.ForeignKey(Readerware, db_column='BOOK_ID')  # Field name made lowercase.
    vol_number = models.IntegerField(db_column='VOL_NUMBER')  # Field name made lowercase.
    vol_title = models.CharField(db_column='VOL_TITLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vol_user1 = models.CharField(db_column='VOL_USER1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vol_user2 = models.CharField(db_column='VOL_USER2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vol_filler1 = models.CharField(db_column='VOL_FILLER1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vol_filler2 = models.CharField(db_column='VOL_FILLER2', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'READERWARE_VOLUMES'


class ReadingLevelList(models.Model):
    rowkey = models.BigIntegerField(db_column='ROWKEY', primary_key=True)  # Field name made lowercase.
    listitem = models.CharField(db_column='LISTITEM', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'READING_LEVEL_LIST'


class SeriesList(models.Model):
    rowkey = models.BigIntegerField(db_column='ROWKEY', primary_key=True)  # Field name made lowercase.
    listitem = models.CharField(db_column='LISTITEM', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SERIES_LIST'


class SignedList(models.Model):
    rowkey = models.BigIntegerField(db_column='ROWKEY', primary_key=True)  # Field name made lowercase.
    listitem = models.CharField(db_column='LISTITEM', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SIGNED_LIST'


class SourceList(models.Model):
    rowkey = models.BigIntegerField(db_column='ROWKEY', primary_key=True)  # Field name made lowercase.
    listitem = models.CharField(db_column='LISTITEM', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SOURCE_LIST'


class StatusList(models.Model):
    rowkey = models.BigIntegerField(db_column='ROWKEY', primary_key=True)  # Field name made lowercase.
    listitem = models.CharField(db_column='LISTITEM', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STATUS_LIST'


class TypeList(models.Model):
    rowkey = models.BigIntegerField(db_column='ROWKEY', primary_key=True)  # Field name made lowercase.
    listitem = models.CharField(db_column='LISTITEM', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TYPE_LIST'


class WebappConfiguration(models.Model):
    name = models.CharField(primary_key=True, max_length=127)
    value = models.CharField(max_length=127)
    value_1 = models.CharField(max_length=255, blank=True, null=True)
    value_2 = models.CharField(max_length=255, blank=True, null=True)
    value_3 = models.CharField(max_length=255, blank=True, null=True)
    value_4 = models.CharField(max_length=255, blank=True, null=True)
    value_5 = models.CharField(max_length=255, blank=True, null=True)
    value_6 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WEBAPP_CONFIGURATION'
