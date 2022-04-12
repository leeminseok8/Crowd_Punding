import json

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