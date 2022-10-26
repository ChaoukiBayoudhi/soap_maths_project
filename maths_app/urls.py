from django.urls import path
from . import views
urlpatterns = [
    path('',views.my_soap_application,name='mathsApp')
]
