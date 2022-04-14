import json

from django.db.models import Q
from datetime import date
from django.http import JsonResponse
from django.views import View

from products.models import Product
from users.models import Seller

class ProductOpenView(View):
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
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)
        except ValueError:
            return JsonResponse({"result" : "VALUE_ERROR"}, status=400)


class ProductListView(View):
    def get(self, request):
        try:
            search = request.GET.get("search", None)
            sorting = request.GET.get("sorting", "id")

            sort_set = {
                "high_amount" : "-productdetail__total_amount",
                "low_amount" : "productdetail__total_amount",
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

        except KeyError:
            return JsonResponse({"result" : "KEY_ERROR"}, status=400)    # sorting key값이 없을 시 발생
        except Product.DoesNotExist:
            return JsonResponse({"result" : "Product matching query does not exist"}, status=400)


class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
    
            data = {
                "subject" : product.subject,
                "name" : product.seller.name,
                "total_amount" : product.productdetail.total_amount,
                "rate" : product.productdetail.rate,
                "d-day" : (product.end_date-date.today()).days,
                "description" : product.description,
                "goal_amount" : product.goal_amount,
                "total_supporter" : product.productdetail.total_supporter
            }
    
            return JsonResponse({"result" : data}, status=200)

        except Product.DoesNotExist:
            return JsonResponse({"result" : "Product matching query does not exist."}, status=400)


class ProductAdminView(View):    # Update, Delete method 클래스
    def delete(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
    
            product.delete()
    
            return JsonResponse({"return" : "SECCESS"}, status=200)

        except Product.DoesNotExist:
            return JsonResponse({"result" : "Product matching query does not exist."}, status=400)

    def patch(self, request, product_id):
        try:
            data = json.loads(request.body)
    
            product = Product.objects.get(id=product_id)
    
            subject = data.get("subject", product.subject)
            description = data.get("description", product.description)
            amount = data.get("amount", product.amount)
            end_date = data.get("end_date", product.end_date)
    
            Product.objects.filter(id=product_id).update(
                subject = subject,
                description = description,
                amount = amount,
                end_date = end_date
            )
    
            return JsonResponse({"result" : "SECCESS"}, status=200)

        except Product.DoesNotExist:
            return JsonResponse({"result" : "Product matching query does not exist."}, status=400)
        except ValueError:
            return JsonResponse({"result" : "VALUE_ERROR"})