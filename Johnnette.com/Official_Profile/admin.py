from django.contrib import admin
from Official_Profile.models import JobPost, NewsandMedia, HomePageProduct, Product,ProductPageImagesAndVideos, ProductSpecsOnBannerAndDetailedDescription, ProductSpecsOnSlides, BoardOfDirectors, SeniorManagement

# Register your models here.

admin.site.register(Product)
admin.site.register(HomePageProduct)
admin.site.register(ProductSpecsOnSlides)
admin.site.register(ProductPageImagesAndVideos)
admin.site.register(ProductSpecsOnBannerAndDetailedDescription)
admin.site.register(BoardOfDirectors)
admin.site.register(SeniorManagement)
admin.site.register(NewsandMedia)
admin.site.register(JobPost)