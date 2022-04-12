from django.urls import path

from products.views import OpenProductView, DetailPageView, ListView

urlpatterns = [
    path("/openproducts", OpenProductView.as_view()),
    path("/lists", ListView.as_view()),
]