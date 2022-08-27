from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from .models import *


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, '')
