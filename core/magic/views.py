import os

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, View
from django.http import HttpResponse

import usernames
import requests
import json

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
		message = requests.get('http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1')
		message = json.loads(message.text)[0]['content']

		if image is not None:
			os.system('{} {} {}'.format(base_cmd, username, message))

		return redirect(reverse('home'))