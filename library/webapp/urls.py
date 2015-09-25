from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^home/$', views.home_page_render, name='home page'),
    url(r'^search/$', views.search_page_render, name='search page'),
    url(r'^book/([0-9]*)/$', views.book_info_by_barcode, name='book info'),

]
