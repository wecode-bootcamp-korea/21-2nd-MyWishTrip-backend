from django.urls import path
from .views      import ProductView, OptionView

urlpatterns = [
    path('/<int:product_id>', ProductView.as_view()),
    path('/option', OptionView.as_view())
]