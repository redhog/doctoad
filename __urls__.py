from django.conf.urls import *
from django.conf import settings

urlpatterns = patterns('',
    (r'^doctoad/?$', 'appomatic_doctoad.views.index'),
    (r'^doctoad/file/?$', 'appomatic_doctoad.views.file'),
    (r'^doctoad/change/?$', 'appomatic_doctoad.views.change'),
    (r'^doctoad/log/?$', 'appomatic_doctoad.views.log'),
    (r'^doctoad/merge/?$', 'appomatic_doctoad.views.merge'),
    (r'^doctoad/fix/?$', 'appomatic_doctoad.views.fix'),
)