from django.urls import path
from .views import KakaoSigninView
urlpatterns = [
    path('/social-login',KakaoSigninView.as_view(),)
]
