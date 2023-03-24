from django.urls import path
from Official_Profile import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("certification/", views.certification, name="certification"),
    path("career/", views.career, name="career"),
    path("contact/", views.contact, name="contact"),
    path("cookies/", views.cookies, name="cookies"),
    path("code-of-ethics/", views.ethics_code, name="code-of-ethics"),
    path("news/", views.news, name="news"),
    path("policy/", views.policy, name="policy"),
    path("services/", views.services, name="services"),
    path("terms/", views.terms, name="terms"),
    path("<pk>/product/", views.product, name="product"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)