from django.urls import path
from .views import KakaoSigninView ,EmailSignupView, EmailSigninView
urlpatterns = [
    path('/signup', EmailSignupView.as_view()),
    path('/signin',EmailSigninView.as_view()),
    path('/social-login',KakaoSigninView.as_view())
]



