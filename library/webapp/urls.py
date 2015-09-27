from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^home/$', views.home_page_render, name='home page'),
    url(r'^search/$', views.search_page_render, name='search page'),
    url(r'^book/([0-9]*)/$', views.book_info_by_barcode, name='book info'),

    url(r'^api/v1/book/$', views.api.get_book_list, name='search api'),
    url(r'^api/v1/book/([0-9]*)/$', views.api.get_book_detail, name='book detail api'),
    url(r'^api/v1/book/search/', views.api.get_book_search, name='search api'),

]
