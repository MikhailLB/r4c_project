from django.urls import path
from .views import *

app_name = 'robots'

urlpatterns = [
    path('add-robot/', robot_processing, name='add-robot'),
    path('export-data/', export_robot_summary_data, name='export_robot_summary_data'),
]