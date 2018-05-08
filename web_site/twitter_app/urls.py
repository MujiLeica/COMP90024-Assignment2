from django.conf.urls import url
from . import views

app_name = 'twitter_app'

urlpatterns = [

    url(r'^$', views.HomeTemplateView.as_view(), name='home_page'),

    url(r'^map/$', views.MapTemplateView.as_view(), name='map_page'),

    url(r'^team/$', views.TeamTemplateView.as_view(), name='team_page'),

    url(r'^day_sum_table/$', views.DaySumTableTemplateView.as_view(), name='day_sum_table'),

    url(r'^hour_sum_table/$', views.HourSumTableTemplateView.as_view(), name='hour_sum_table'),

    url(r'^map/$', views.MapTemplateView.as_view(), name='map'),

    url(r'^hash_tag/$', views.HashTagTemplateView.as_view(), name='hash_tag'),
]
