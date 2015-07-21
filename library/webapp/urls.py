from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^book/([0-9]*)/', views.book_info_by_barcode, name='book info'),

]
