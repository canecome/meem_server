from django.shortcuts import render
from django.views.generic import TemplateView


class homePageView(TemplateView):
    template_name = 'front/index.html'

    def get_context_data(self, **kwargs):
        context = super(homePageView, self).get_context_data(**kwargs)
        return context

front_view = homePageView.as_view()