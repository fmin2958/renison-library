import os
import sys

from django.conf import settings

from webapp import models

#init

__book_cover_api_config = models.WebappConfiguration.objects.get(name__iexact = 'book_cover_api_config')

if not __book_cover_api_config:
    sys.exit('initilization failed - cannot find webapp configuration in db.')

COVER_PATH = __book_cover_api_config.value

DEFAULT_COVER_URL = os.path.join(settings.STATIC_URL, COVER_PATH, __book_cover_api_config.value_1)

DEFAULT_COVER_FILE_PATH = os.path.join(settings.STATIC_PATH, COVER_PATH, __book_cover_api_config.value_1)

SEARCH_MAX_ITEM = 2000
