from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .globalvariables import email

def index(request):

	if request.method == 'POST':
		message = request.POST['message']

		send_mail('Django mail',
		 message, 
		 settings.EMAIL_HOST_USER,
		 
		 [email], 
		 fail_silently=False)
	return render(request, 'app/index.html')
