from django.urls import path

from . import views

urlpatterns = [
    path('<int:flight_id>', views.flight_info, name='info'),
]