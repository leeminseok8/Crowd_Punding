import json

from django.db.models import Q
from datetime import date
from django.http import JsonResponse
from django.views import View

from products.models import Product
from users.models import Seller

class OpenProductView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            subject = data["subject"]
            description = data["description"]
            amount = data["amount"]
            goal_amount = data["goal_amount"]
            end_date = data["end_date"]
            seller_name = data["seller"]

            seller, created = Seller.objects.get_or_create(
                name = seller_name
            )

            Product.objects.create(
                subject = subject,
                description = description,
                amount = amount,
                goal_amount = goal_amount,
                end_date = end_date,
                seller = seller
            )

            return JsonResponse({"message" : "SECCESS"}, status=200)

        except KeyError:
            return JsonResponse({"message" : "KEYERROR"}, status=400)


class ListView(View):
    def get(self, request):
        search = request.GET.get("search", None)
        sorting = request.GET.get("sorting", "id")

        sort_set = {
            "high_amount" : "-productdetail__total_amount",
            "low_amount" : "product__total_amount",
            "late_open" : "-created_at",
            "early_open" : "created_at",
            "id" : "id"
        }

        q = Q()
        if search:
            q &= Q(subject__icontains=search)

        result = [{
            "subject" : product.subject,
            "name" : product.seller.name,
            "total_amount" : str(format((product.productdetail.total_amount), ",d"))+"원",
            "rate" : str(int((product.productdetail.total_amount/product.goal_amount)*100))+"%",
            "d-day" : str((product.end_date-date.today()).days)+"일"
        }for product in Product.objects.filter(q).order_by(sort_set[sorting])]

        return JsonResponse({"result" : result}, status=200)

