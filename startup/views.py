from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import ContactForm, QuoteForm
from .models import Team, Service, Testimonial
from blog.models import Blog

# Create your views here.

def home(request):
  blogs = Blog.objects.order_by('-created_on')
  teams = Team.objects.all()
  services = Service.objects.all()
  testimonials = Testimonial.objects.all()
  context = { 'blogs': blogs, 'teams': teams, 'services': services, 'testimonials': testimonials}
  return render(request, "index.html", context)


def about(request):
  teams = Team.objects.all()
  context = { 'teams': teams}
  return render(request, "about.html", context)


def service(request):
  services = Service.objects.all()
  testimonials = Testimonial.objects.all()
  context = { 'services': services, 'testimonials': testimonials}
  return render(request, "service.html", context)


def price_plan(request):
  return render(request, "price.html")


def team(request):
  teams = Team.objects.all()
  context = { 'teams': teams}
  return render(request, "team.html", context)


def feature(request):
  return render(request, "feature.html")


def testimonial(request):
  testimonials = Testimonial.objects.all()
  context = { 'testimonials': testimonials}
  return render(request, "testimonial.html", context)


def contact(request):
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data["name"]
      email = form.cleaned_data["email"]
      subject = form.cleaned_data["subject"]
      message = form.cleaned_data["message"]

      html_content = render_to_string(
                "emails/emaildisplay.html",
                {
                    "name": name,
                    "email": email,
                    "subject": subject,
                    "message": message,
                },
            )

      send_mail("You got a mail!!!", message, email, ['recipient_email'], html_message=html_content, fail_silently=False)
    
      return redirect("contact")
  else:
    form = ContactForm()
  return render(request, 'contact.html', {'form': form})



def quote(request):
  if request.method == "POST":
    form = QuoteForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data["name"]
      email = form.cleaned_data["email"]
      service = form.cleaned_data["service"]
      message = form.cleaned_data["message"]

      html_content = render_to_string(
                "emails/quote_email.html",
                {
                    "name": name,
                    "email": email,
                    "service": service,
                    "message": message,
                },
            )

      send_mail("You got a mail for a Quote!!!", message, email, ['recipient_email'], html_message=html_content, fail_silently=False)
    
      return redirect("quote")
  else:
    form = QuoteForm()
  return render(request, 'quote.html', {'form': form})





