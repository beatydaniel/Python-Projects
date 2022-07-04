from django.apps import AppConfig


class ClassappConfig(AppConfig):  # creates the app, so I can access the class on the admin site
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'classApp'
