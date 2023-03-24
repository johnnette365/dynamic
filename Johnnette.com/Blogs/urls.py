from django.urls import path
from django.conf import settings
from Blogs import views
from django.conf.urls.static import static



urlpatterns = [
    path("bloglist/", views.bloglist, name="bloglist"),
    path("<pk>/articles/", views.articles, name="articles"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)