from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def contact_us(request):
    return render(request, "contact us.html")
def appointment(request):
    return render(request, "appointment.html")
def blog(request):
    return render(request, "blog.html")
def contact(request):
    return render(request, "contact.html")
def detail(request):
    return render(request, "detail.htmll")
def index(request):
    return render(request, "index.html")
def price(request):
    return render(request, "price.html")
def search(request):
    return render(request, "search.html")
def service(request):
    return render(request, "service.html")
def team(request):
    return render(request, "team.html")
def testimonial(request):
    return render(request, "testimonial.html")

