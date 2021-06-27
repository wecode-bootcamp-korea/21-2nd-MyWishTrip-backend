from django.urls import path
from .views      import ProductView, OptionView, ProductsView, RegionsView, ReviewView

urlpatterns = [
    path('', ProductsView.as_view()),
    path('/review',ReviewView.as_view()),
    path('/option', OptionView.as_view()),
    path('/regions',RegionsView.as_view()),
    path('/<int:product_id>', ProductView.as_view())
]
