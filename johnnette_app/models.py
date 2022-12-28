from django.db import models

# Create your models here.


Product_specifications=(
    ('WINGSPAN', 'WINGSPAN'),
    ('AIRCRAFT WEIGHT', 'AIRCRAFT WEIGHT'),
    ('MAX TRAVEL DISTANCE', 'MAX TRAVEL DISTANCE'),
    ('MAX RECORDABLE OPERATIONAL RADIUS', 'MAX RECORDABLE OPERATIONAL RADIUS'),
    ('PAYLOAD', 'PAYLOAD'),
    ('MAX FLIGHT ALTITUDE', 'MAX FLIGHT ALTITUDE'),
    ('ENDURANCE', 'ENDURANCE'),
    ('MAX LIVE VIDEO OPERATIONAL RADIUS', 'MAX LIVE VIDEO OPERATIONAL RADIUS'),
    ('OPERATING TEMPRATURE', 'OPERATING TEMPRATURE'),
    ('LAUNCH/RECOVERY', 'LAUNCH/RECOVERY'),
    ('PROPULSION', 'PROPULSION'),
    ('COMMUNICATION', 'COMMUNICATION'),
    ('OPERATIONAL RANGE', 'OPERATIONAL RANGE'),
    ('FLIGHT TIME', 'FLIGHT TIME'),
    ('NAVIGATION', 'NAVIGATION'),
    ('MSL', 'MSL'),
)

class Products(models.Model):
    specifications = models.CharField(choices=Product_specifications, max_length=100)
    product_name = models.CharField(max_length=500)
    wingspan = models.CharField(max_length=500, blank=True, null=True)
    aircraft_weight = models.CharField(max_length=500, blank=True, null=True)
    operational_radius = models.CharField(max_length=500, blank=True, null=True)
    payloads = models.CharField(max_length=500, blank=True, null=True)
    max_flight_altitude = models.CharField(max_length=500, blank=True, null=True)
    endurance = models.CharField(max_length=500, blank=True, null=True)
    max_live_video_operational_radius = models.CharField(max_length=500, blank=True, null=True)
    operating_temprature = models.CharField(max_length=500, blank=True, null=True)
    launch_recovery = models.CharField(max_length=500, blank=True, null=True)
    propulsion = models.CharField(max_length=500, blank=True, null=True)
    communication = models.CharField(max_length=500, blank=True, null=True)
    operational_range = models.CharField(max_length=500, blank=True, null=True)
    flight_time = models.CharField(max_length=500, blank=True, null=True)
    navigation = models.CharField(max_length=500, blank=True, null=True)
    msl = models.CharField(max_length=500, blank=True, null=True)
    
    feacher1 = models.CharField(max_length=500, blank=True, null=True)
    feacher2 = models.CharField(max_length=500, blank=True, null=True)
    feacher3 = models.CharField(max_length=500, blank=True, null=True)
    feacher4 = models.CharField(max_length=500, blank=True, null=True)
    feacher5 = models.CharField(max_length=500, blank=True, null=True)

    advantage1 = models.CharField(max_length=500, blank=True, null=True)
    advantage2 = models.CharField(max_length=500, blank=True, null=True)
    advantage3 = models.CharField(max_length=500, blank=True, null=True)
    advantage4 = models.CharField(max_length=500, blank=True, null=True)
    advantage5 = models.CharField(max_length=500, blank=True, null=True)
    
    # if specifications:
    # for specific in specifications:
    #     if specific == "WINGSPAN":