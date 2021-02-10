from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

@method_decorator(login_required, name='dispatch')
class IndexView(LoginRequiredMixin, TemplateView):
    template_name ='gerenciador/index.html'