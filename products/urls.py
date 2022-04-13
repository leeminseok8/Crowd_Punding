from django.urls import path

from products.views import OpenProductView, DetailPageView, ListView, DeleteProductView

urlpatterns = [
    path("/openproducts", OpenProductView.as_view()),
    path("/lists", ListView.as_view()),
    path("/detailpages/<int:product_id>", DetailPageView.as_view()),
    path("/deleteproducts/<int:product_id>", DeleteProductView.as_view()),
]