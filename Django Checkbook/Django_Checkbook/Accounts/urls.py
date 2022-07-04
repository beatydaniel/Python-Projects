from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('createAccount', views.createRecord, name='create_account'),
    path('addTransaction',views.createTransaction, name='create_transaction'),

]


urlpatterns += staticfiles_urlpatterns()