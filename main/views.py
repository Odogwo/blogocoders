from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator #import Paginator
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages #import messages

# Create your views here.

def homepage(request):
	books = Book.objects.all() #queryset containing all books we just created
	paginator = Paginator(books, 6)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request=request, template_name="main/home.html", context={'books':page_obj})



# Create your views here.
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			messages.success(request, "Message sent." )
			return redirect ("main:homepage")
		messages.error(request, "Error. Message not sent.")
      
	form = ContactForm()
	return render(request, "main/contact.html", {'form':form})