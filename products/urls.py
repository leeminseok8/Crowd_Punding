from django.urls import path

from products.views import ProductOpenView, ProductDetailView, ProductListView, ProductAdminView

urlpatterns = [
    path("/open", ProductOpenView.as_view()),
    path("/list", ProductListView.as_view()),
    path("/detail/<int:product_id>", ProductDetailView.as_view()),
    path("/<int:product_id>", ProductAdminView.as_view())    # REST API 설계를 위해 2개 기능을 하나의 URL로 작성
]