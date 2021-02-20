from django.urls import path
from productapp import views

app_name = 'Product'

urlpatterns = [
    path('',views.index, name = 'index')
]