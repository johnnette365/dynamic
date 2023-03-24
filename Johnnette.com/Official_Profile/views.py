from django.shortcuts import render
from Official_Profile.models import SeniorManagement, BoardOfDirectors, JobPost, NewsandMedia, HomePageProduct, Product
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
    product = HomePageProduct.objects.all()
    pid=Product.objects.all()
    context={
        "product":product,
        "pid":pid,
    }
    return render(request, "app/index.html", context)

def product(request, pk):
    product = get_object_or_404(Product, id=pk)
    images=product.ImagesAndVideos.all()
    for images in images:
        pass
    
    bannerSpecs=product.BannerSpecs.all()
    for bannerSpecs in bannerSpecs:
        pass
    
    productSlides=product.ProductSlideSpecs.all()
    for productSlides in productSlides:
        pass
    
    contaxt={
        "product":product,
        "images":images,
        "bannerSpecs":bannerSpecs,
        "productSlides":productSlides,
    }
    return render(request, "app/product.html",contaxt)

def about(request):
    Seniormanagement=SeniorManagement.objects.all()
    Boardofdirectors=BoardOfDirectors.objects.all()
    contex={
        "Seniormanagement":Seniormanagement,
        "Boardofdirectors":Boardofdirectors,
    }
    return render(request, "app/about.html", contex)


def career(request):
    post=JobPost.objects.all()
    context={
        "post":post
    }
    return render(request, "app/career.html", context)


def news(request):
    news=NewsandMedia.objects.all()
    context={
        'news':news
    }
    # return render(request, "app/news.html", context)
    return render(request, "app/news.html", context)


def certification(request):
    return render(request, "app/accolades-and-certifications.html")


def contact(request):
    return render(request, "app/contact.html")


def cookies(request):
    return render(request, "app/cookies.html")


def ethics_code(request):
    return render(request, "app/ethics_code.html")


def policy(request):
    return render(request, "app/policy.html")


def services(request):
    return render(request, "app/services.html")


def terms(request):
    return render(request, "app/terms.html")

