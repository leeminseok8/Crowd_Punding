from django.urls import path

from products.views import ProductView, ProductDetailView, FundingView

urlpatterns = [
    path("/", ProductView.as_view()),
    path("/<int:product_id>", ProductView.as_view()),
    path("/detail/<int:product_id>", ProductDetailView.as_view()),
    path("/funding", FundingView.as_view())
]