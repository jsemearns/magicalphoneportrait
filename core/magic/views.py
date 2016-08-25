import os

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, View
from django.http import HttpResponse

import usernames
import requests
import json
import re

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'


class MessageFacebookUser(View):
    def post(self, request, *args, **kwargs):
        base_cmd = 'python message_fb.py'
        image = request.POST.get('image', None)
        username = ''
        index = 0

        filename = str(image).split('.')[0]
        if filename.isdigit():
            if int(filename) < 6:
                index = int(filename)

        username = usernames.usernames[index]

        if image is not None:
            try:
                os.system('{} {}'.format(base_cmd, username))
            except:
                return HttpResponse(status=400)

        # return redirect(reverse('home'))
        return HttpResponse()
