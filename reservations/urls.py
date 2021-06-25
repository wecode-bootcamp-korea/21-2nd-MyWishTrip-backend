from django.urls import path

from .views import ReservationVeiw

urlpatterns = [
    path('',ReservationVeiw.as_view())
]
