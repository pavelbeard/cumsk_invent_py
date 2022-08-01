from django.urls import path
from . import views

app_name = 'devices_invent'
urlpatterns = [
    path('snmpc_devices_all/', views.snmpc_devices_all, name='snmpc_devices'),
    path('snmpc_device/<node_id>/', views.snmpc_device, name='snmpc_device'),
    path('esma_devices_all/', views.esma_devices_all, name='esma_devices'),
]
