# Generated by Django 4.1.4 on 2022-12-17 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "specifications",
                    models.CharField(
                        choices=[
                            ("WINGSPAN", "WINGSPAN"),
                            ("AIRCRAFT WEIGHT", "AIRCRAFT WEIGHT"),
                            ("MAX TRAVEL DISTANCE", "MAX TRAVEL DISTANCE"),
                            (
                                "MAX RECORDABLE OPERATIONAL RADIUS",
                                "MAX RECORDABLE OPERATIONAL RADIUS",
                            ),
                            ("PAYLOAD", "PAYLOAD"),
                            ("MAX FLIGHT ALTITUDE", "MAX FLIGHT ALTITUDE"),
                            ("ENDURANCE", "ENDURANCE"),
                            (
                                "MAX LIVE VIDEO OPERATIONAL RADIUS",
                                "MAX LIVE VIDEO OPERATIONAL RADIUS",
                            ),
                            ("OPERATING TEMPRATURE", "OPERATING TEMPRATURE"),
                            ("LAUNCH/RECOVERY", "LAUNCH/RECOVERY"),
                            ("PROPULSION", "PROPULSION"),
                            ("COMMUNICATION", "COMMUNICATION"),
                            ("OPERATIONAL RANGE", "OPERATIONAL RANGE"),
                            ("FLIGHT TIME", "FLIGHT TIME"),
                            ("NAVIGATION", "NAVIGATION"),
                            ("MSL", "MSL"),
                        ],
                        max_length=100,
                    ),
                ),
                ("product_name", models.CharField(max_length=500)),
                ("wingspan", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "aircraft_weight",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                (
                    "operational_radius",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("payloads", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "max_flight_altitude",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("endurance", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "max_live_video_operational_radius",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                (
                    "operating_temprature",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                (
                    "launch_recovery",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("propulsion", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "communication",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                (
                    "operational_range",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                (
                    "flight_time",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("navigation", models.CharField(blank=True, max_length=500, null=True)),
                ("msl", models.CharField(blank=True, max_length=500, null=True)),
                ("feacher1", models.CharField(blank=True, max_length=500, null=True)),
                ("feacher2", models.CharField(blank=True, max_length=500, null=True)),
                ("feacher3", models.CharField(blank=True, max_length=500, null=True)),
                ("feacher4", models.CharField(blank=True, max_length=500, null=True)),
                ("feacher5", models.CharField(blank=True, max_length=500, null=True)),
                ("advantage1", models.CharField(blank=True, max_length=500, null=True)),
                ("advantage2", models.CharField(blank=True, max_length=500, null=True)),
                ("advantage3", models.CharField(blank=True, max_length=500, null=True)),
                ("advantage4", models.CharField(blank=True, max_length=500, null=True)),
                ("advantage5", models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
