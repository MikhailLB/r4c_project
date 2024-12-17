from django.urls import path
from .views import *

app_name = 'orders'

urlpatterns = [
    path('add-order/', create_order_processing, name='add-order'),
]