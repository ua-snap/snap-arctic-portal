from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
                       url(r'^snapmapapp$', TemplateView.as_view(template_name='snapmapapp/index.html'), name='snapmapapp'),)

