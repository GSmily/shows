from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /shows/
    url(r'^$', views.index, name='index'),

    # ex: /shows/5/
    url(r'^(?P<show_id>[0-9]+)/$', views.detail, name='detail'),

    # ex: /shows/5/rating/
    url(r'^(?P<show_id>[0-9]+)/rating/$', views.rating, name='rating'),

    # ex: /shows/5/rate/
    url(r'^(?P<show_id>[0-9]+)/rate/$', views.rate, name='rate'),
]