from django.shortcuts import render
from django.views.generic import (TemplateView)

# Create your views here.


class HomeTemplateView(TemplateView):
    template_name = 'twitter_app/home.html'


class MapTemplateView(TemplateView):
    template_name = 'twitter_app/map1.html'


class TeamTemplateView(TemplateView):
    template_name = 'twitter_app/team.html'



class DaySumTableTemplateView(TemplateView):
    template_name = 'twitter_app/daysum_table.html'


class HourSumTableTemplateView(TemplateView):
    template_name = 'twitter_app/hoursum_table.html'


class MapTemplateView(TemplateView):
    template_name = 'twitter_app/map.html'