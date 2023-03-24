from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.



import os
class Product(models.Model):
    product_name=models.CharField(max_length=500, blank=True, null=True,)
    product_description=models.TextField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return str(self.product_name)
     
    
class HomePageProduct(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, default=None)

    def desktop(ProductHomePage, filename):
        folder_name = "Johnnette/" + ProductHomePage.product.product_name + "/Home Page Images/Desktop"
        return os.path.join(folder_name, filename)
    
    def mobile(ProductHomePage, filename):
        folder_name = "Johnnette/" + ProductHomePage.product.product_name + "/Home Page Images/Mobile"
        return os.path.join(folder_name, filename)
    
    product_home_page_desktop_image=models.ImageField(upload_to=desktop, blank=True, null=True, editable=True,)
    product_home_page_mobile_image=models.ImageField(upload_to=mobile, blank=True, null=True, editable=True,)
    product_description=models.TextField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = "Product On Home Page"
        verbose_name_plural = "Products On Home Page"

    def __str__(self):
        return str(self.product.product_name)
 

class ProductPageImagesAndVideos(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ImagesAndVideos')
    
    def banner(ProductPage, filename):
        folder_name = "Johnnette/" + ProductPage.product.product_name + "/Product Page Images/Banner Images"
        return os.path.join(folder_name, filename)
    
    def bannerVideo(ProductPage, filename):
        folder_name = "Johnnette/" + ProductPage.product.product_name + "/Product Page Images/Banner Video"
        return os.path.join(folder_name, filename)
    
    def descriptionImagesDesktop(ProductPage, filename):
        folder_name = "Johnnette/" + ProductPage.product.product_name + "/Product Page Images/Wireframe Images/Desktop"
        return os.path.join(folder_name, filename)
    
    def descriptionImagesMobile(ProductPage, filename):
        folder_name = "Johnnette/" + ProductPage.product.product_name + "/Product Page Images/Wireframe Images/Mobile"
        return os.path.join(folder_name, filename)
    
    product_banner_image=models.ImageField(upload_to=banner, blank=True, null=True, editable=True,)
    product_banner_video=models.FileField(upload_to=bannerVideo, blank=True, null=True, editable=True,)
    product_wireframe_image_for_desktop=models.ImageField(upload_to=descriptionImagesDesktop, blank=True, null=True, editable=True,)
    product_wireframe_image_for_mobile=models.ImageField(upload_to=descriptionImagesMobile, blank=True, null=True, editable=True,)
    
    def productDesktopSliderImages(ProductPage, filename):
        folder_name = "Johnnette/" + ProductPage.product.product_name + "/Product Page Images/slider images/desktop"
        return os.path.join(folder_name, filename)
    
    product_slider_desktop_image1=models.ImageField(upload_to=productDesktopSliderImages, blank=True, null=True, editable=True,)
    product_slider_desktop_image2=models.ImageField(upload_to=productDesktopSliderImages, blank=True, null=True, editable=True,)
    product_slider_desktop_image3=models.ImageField(upload_to=productDesktopSliderImages, blank=True, null=True, editable=True,)
    product_slider_desktop_image4=models.ImageField(upload_to=productDesktopSliderImages, blank=True, null=True, editable=True,)

    def productMobileSliderImages(ProductPage, filename):
        folder_name = "Johnnette/" + ProductPage.product.product_name + "/Product Page Images/slider images/mobile"
        return os.path.join(folder_name, filename)

    product_slider_mobile_image1=models.ImageField(upload_to=productMobileSliderImages, blank=True, null=True, editable=True,)
    product_slider_mobile_image2=models.ImageField(upload_to=productMobileSliderImages, blank=True, null=True, editable=True,)
    product_slider_mobile_image3=models.ImageField(upload_to=productMobileSliderImages, blank=True, null=True, editable=True,)
    product_slider_mobile_image4=models.ImageField(upload_to=productMobileSliderImages, blank=True, null=True, editable=True,)

    def productAnimationImages(ProductPage, filename):
        folder_name = "Johnnette/" + ProductPage.product.product_name + "/Product Page Images/Animation Images"
        return os.path.join(folder_name, filename)

    product_animation_wireframe_image=models.ImageField(upload_to=productAnimationImages, blank=True, null=True, editable=True,)
    product_animation_rander_image=models.ImageField(upload_to=productAnimationImages, blank=True, null=True, editable=True,)
    
    def productVideoThumbnail(ProductPage, filename):
        folder_name = "Johnnette/" + ProductPage.product.product_name + "/Product Page Images/Product Video and Thumbnail"
        return os.path.join(folder_name, filename)
    
    product_video_thumbnail_image=models.ImageField(upload_to=productVideoThumbnail, blank=True, null=True, editable=True,)
    product_Intro_video=models.FileField(upload_to=productVideoThumbnail, blank=True, null=True, editable=True,)

    def productFieldImages(ProductPage, filename):
        folder_name = "Johnnette/" + ProductPage.product.product_name + "/Product Page Images/Product Field Images"
        return os.path.join(folder_name, filename) 
    
    product_field_image1=models.ImageField(upload_to=productFieldImages, blank=True, null=True, editable=True)
    product_field_image2=models.ImageField(upload_to=productFieldImages, blank=True, null=True, editable=True)
    product_field_image3=models.ImageField(upload_to=productFieldImages, blank=True, null=True, editable=True)
    product_field_image4=models.ImageField(upload_to=productFieldImages, blank=True, null=True, editable=True)

    class Meta:
        verbose_name = "Product Images and Videos"
        verbose_name_plural = "Product Images and Videos"

    def __str__(self):
        return str(self.product.product_name)


class ProductSpecsOnBannerAndDetailedDescription(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, default=None, related_name='BannerSpecs')
    operational_range=models.CharField(max_length=500, blank=True, null=True)
    flight_time = models.CharField(max_length=500, blank=True, null=True)
    aircraft_weight = models.CharField(max_length=500, blank=True, null=True)
    product_detailed_description=RichTextUploadingField(max_length=2000, blank=True, null=True)

    class Meta:
        verbose_name = "Product Specs On Banner"
        verbose_name_plural = "Product Specs On Banner"

    def __str__(self):
        return str(self.product.product_name)


class ProductSpecsOnSlides(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, default=None, related_name='ProductSlideSpecs')
    wingspan = models.CharField(max_length=500, blank=True, null=True)
    length = models.CharField(max_length=500, blank=True, null=True)
    height = models.CharField(max_length=500, blank=True, null=True)
    aircraft_weight = models.CharField(max_length=500, blank=True, null=True)
    payloads = models.CharField(max_length=500, blank=True, null=True)
    propulsion = models.CharField(max_length=500, blank=True, null=True)
    material = models.CharField(max_length=500, blank=True, null=True)
    cruise_speed = models.CharField(max_length=500, blank=True, null=True)
    max_flight_altitude = models.CharField(max_length=500, blank=True, null=True)
    max_launch_altitude = models.CharField(max_length=500, blank=True, null=True)
    endurance = models.CharField(max_length=500, blank=True, null=True)
    maximum_speed = models.CharField(max_length=500, blank=True, null=True)
    data_link_range = models.CharField(max_length=500, blank=True, null=True)
    operating_temprature = models.CharField(max_length=500, blank=True, null=True)
    launch_recovery = models.CharField(max_length=500, blank=True, null=True)
    communication = models.CharField(max_length=500, blank=True, null=True)
    operational_range = models.CharField(max_length=500, blank=True, null=True)
    max_flight_distance = models.CharField(max_length=500, blank=True, null=True)
    operational_radius = models.CharField(max_length=500, blank=True, null=True)
    # flight_time = models.CharField(max_length=500, blank=True, null=True)
    max_live_video_operational_radius = models.CharField(max_length=500, blank=True, null=True)
    navigation = models.CharField(max_length=500, blank=True, null=True)
    msl = models.CharField(max_length=500, blank=True, null=True)
    feature1 = models.CharField(max_length=500, blank=True, null=True)
    feature2 = models.CharField(max_length=500, blank=True, null=True)
    feature3 = models.CharField(max_length=500, blank=True, null=True)
    feature4 = models.CharField(max_length=500, blank=True, null=True)
    feature5 = models.CharField(max_length=500, blank=True, null=True)
    feature6 = models.CharField(max_length=500, blank=True, null=True)
    advantage1 = models.CharField(max_length=500, blank=True, null=True)
    advantage2 = models.CharField(max_length=500, blank=True, null=True)
    advantage3 = models.CharField(max_length=500, blank=True, null=True)
    advantage4 = models.CharField(max_length=500, blank=True, null=True)
    advantage5 = models.CharField(max_length=500, blank=True, null=True)    
    advantage6 = models.CharField(max_length=500, blank=True, null=True)    

    class Meta:
        verbose_name = "Product Specs On Slides"
        verbose_name_plural = "Product Specs On Slides"

    def __str__(self):
        return str(self.product.product_name)



class SeniorManagement(models.Model):
    employee_name=models.CharField(max_length=500, blank=True, null=True)
    employee_designation=models.CharField(max_length=500, blank=True, null=True)
    employee_profile_picture=models.ImageField(upload_to="Johnnette/About/Senior Management", blank=True, null=True, editable=True,)
    linkedin_profile_link=models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = "Senior Management"
        verbose_name_plural = "Senior Management"
        
    def __str__(self):
        return str(self.employee_name)


class BoardOfDirectors(models.Model):
    director_name=models.CharField(max_length=500, blank=True, null=True)
    director_designation=models.CharField(max_length=500, blank=True, null=True)
    director_profile_picture=models.ImageField(upload_to="Johnnette/About/Directors", blank=True, null=True, editable=True,)
    linkedin_profile_link=models.CharField(max_length=500, blank=True, null=True)
    
    class Meta:
        verbose_name = "Board Of Directors"
        verbose_name_plural = "Board Of Directors"

    def __str__(self):
        return str(self.director_name)

        
        
        
        
        
class JobPost(models.Model):
    job_profile_name=models.CharField(max_length=500, blank=True, null=True)
    job_profile_picture=models.ImageField(upload_to="Johnnette/Job Post", blank=True, null=True, editable=True,)
    job_brief=RichTextUploadingField(max_length=10000, blank=True, null=True)
    job_description=RichTextUploadingField(max_length=10000, blank=True, null=True)
    responsibilities=RichTextUploadingField(max_length=10000, blank=True, null=True)
    desired_skill=RichTextUploadingField(max_length=500, blank=True, null=True)
    qualification=models.CharField(max_length=500, blank=True, null=True)
    experience=models.CharField(max_length=500, blank=True, null=True)
    location=models.CharField(max_length=500, blank=True, null=True)
    number_of_openings=models.CharField(max_length=500, blank=True, null=True)
    first_email_address_to_which_resume_will_be_sent=models.CharField(max_length=500, blank=True, null=True,)
    second_email_address_to_which_resume_will_be_sent=models.CharField(max_length=500, blank=True, null=True,)

    class Meta:
        verbose_name = "Job Post"
        verbose_name_plural = "Job Posts"
        
    def __str__(self):
        return str(self.job_profile_name)



class NewsandMedia(models.Model):
    news_channel_logo=models.ImageField(upload_to="Johnnette/News/Thumbnail", blank=True, null=True, editable=True,)
    news_title=models.CharField(max_length=500, blank=True, null=True)
    news_content=models.TextField(max_length=500, blank=True, null=True)
    news_channel_link=models.CharField(max_length=500, blank=True, null=True)
    news_thumbnail_picture=models.ImageField(upload_to="Johnnette/News/Logo", blank=True, null=True, editable=True,)
    news_video_id=models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = "News And Media"
        verbose_name_plural = "News And Media"
    
    def __str__(self):
        return "News" + str(self.id)