from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'app/index.html')

def jf5(request):
    return render(request, 'app/jf5.html')

def jm2(request):
    return render(request, 'app/jm2.html')

def jf2(request):
    return render(request, 'app/jf2.html')

def about(request):
    return render(request, 'app/about.html')

def certification(request):
    return render(request, 'app/accolades-and-certifications.html')

def career(request):
    return render(request, 'app/career.html')

def contact(request):
    return render(request, 'app/contact.html')

def cookies(request):
    return render(request, 'app/cookies.html')

def ethics_code(request):
    return render(request, 'app/ethics_code.html')

def news(request):
    return render(request, 'app/news.html')

def policy(request):
    return render(request, 'app/policy.html')

def services(request):
    return render(request, 'app/services.html')

def terms(request):
    return render(request, 'app/terms.html')

def skeldar(request):
    return render(request, 'app/skeldar.html')