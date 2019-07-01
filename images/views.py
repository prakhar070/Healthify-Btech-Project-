from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Image
from . forms import ImageUploadForm, UserRegistrationForm
from services import reversegeocode, geocode, centres, createpdf
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage
from django.conf import settings
import os
# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class IndexView(TemplateView):
	template_name = 'main/index.html'

	def get_context_data(self, **kwargs):
		ctx = super().get_context_data(**kwargs)
		ctx['uploadform'] = ImageUploadForm()
		ctx['result'] = self.request.GET.get('result')
		ctx['posturl'] = reverse('save')			
		return ctx



class CentresView(LoginRequiredMixin, TemplateView):
	template_name = 'main/centres.html'

	def get_context_data(self, **kwargs):
		ctx = super().get_context_data(**kwargs)
		return ctx

	def get(self, request, *args, **kwargs):
		context = self.get_context_data()
		data = self.request.GET
		if not data:
			context['var'] = True
		else:
			if data.get('address'):
				context['address'] = data.get('address')
				latlng = geocode.getCoords(context['address'])
				res = centres.getNearbyHospitals(latlng)
				context['results'] = res
				file_path = BASE_DIR + "/media/pdf/centresList-user{}.pdf"
				file_path = file_path.format(self.request.user.first_name)
				createpdf.createPDF(res, file_path)
			else:
				latlng = {'lat':data.get('lat'),'lng':data.get('long')}
				context['address'] = reversegeocode.getAddress(data.get('lat'),data.get('long'))
				
				# if the user clicked the submit button
		#print("contexxxxxxxxxxxxxxxt of centres is {}".format(context['results']))
		return super().render_to_response(context)



class SaveImageView(CreateView):
	form_class = ImageUploadForm

	def get_initial(self):
		return super().get_initial()

	def get_success_url(self):
		url = "{}?result={}".format(reverse('index'),self.object.res)
		return url

	def render_to_response(self, context=None, **response_kwargs):
		return redirect(to = reverse('index'))


# view to handle user registration
def register(request):
	if request.method == "POST":
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			# go to the registration done page
			return render(request, "account/register_done.html",{'new_user':new_user} )
	else:
		user_form = UserRegistrationForm()
	return render(request, "account/register.html", {'user_form':user_form})


# a view to send email
def email(request):
	if request.user.is_authenticated:
		email = EmailMessage()	
		email.subject = "Healtify - List of nearby health centres from your place"
		email.body = "check the pdf file attached with this mail"
		email.from_email = "bansalprakhar.2266@gmail.com"
		email.to = [ "{}".format(request.user.email), ] 
		file_path = BASE_DIR + "/media/pdf/centresList-user{}.pdf"
		file_path = file_path.format(request.user.first_name)
		#print("file path here is {}".format(file_path))
		email.attach_file(file_path) # Attach a file directly
		email.send() 
		return redirect(to=reverse('index'))
	else:
		return redirect(to= reverse('login'))




