from . import views
from django.urls import path

urlpatterns = [      
    path('', views.servicios, name='servicios'),
	path('servicio_status_/<int:servicio_id>/', views.change_status_servicio, name='servicio_status'),            
]