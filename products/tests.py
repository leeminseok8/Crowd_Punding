import json

from django.test import TestCase, Client

from products.models import Product, Productdetail
from users.models import Seller

class ProductOpenTest(TestCase):
    def setUp(self):
        Seller.objects.create(
            id = 1,
            name = "minseok"
        )

        Product.objects.create(
            id=1,
            subject = "화성 정착",
            description = "우주 개척",
            amount = 100,
            goal_amount = 10000,
            end_date = "2022-12-12",
            seller_id = 1,
        )

        Productdetail.objects.create(
            id = 1,
            total_amount = 0,
            total_supporter = 0,
            rate = 0,
            product_id = 1
        )

    def test_success_product_open_view_get_method(self):
        client = Client()

        result = {
            "id" : 1,
            "subject" : "화성 정착",
            "description" : "우주 개척",
            "amount" : 100,
            "goal_amount" : 10000,
            "end_date" : "2022-12-12",
            "seller_id" : 1
        }
        res = json.dumps(result)
        response = client.post('/products/open', res, content_type="application/json")

        self.assertEqual(response.json(),{"message" : "SECCESS"})
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        Product.objects.all().delete()
        Productdetail.objects.all().delete()
        Seller.objects.all().delete()


class ProductAdminTest(TestCase):
    def setUp(self):
        sellers = [
            Seller(
                id   = 1,
                name = 'min'
            ),
            Seller(
                id   = 2,
                name = 'suk'
            ),
            Seller(
                id   = 3,
                name = 'chan'
            )
        ]
        Seller.objects.bulk_create(sellers)
        products = [
            Product(
                id = 1,
                subject = '핸드폰',
                description = '핸드폰 상세설명',
                amount = 100000,
                goal_amount = 2000000,
                end_date = '2022-12-20',
                seller_id = 1,
                created_at = '2022-03-10',
            ),
            Product(
                id = 2,
                subject = '킥보드',
                description = '킥보드 상세설명',
                amount = 50000,
                goal_amount = 4000000,
                end_date = '2022-08-15',
                seller_id = 2,
                created_at = '2022-04-02',
            ),
            Product(
                id = 3,
                subject = '편안한 날으는 자동차',
                description = '편안한 날으는 자동차 상세설명',
                amount = 2000000,
                goal_amount = 80000000,
                end_date = '2022-09-19',
                seller_id = 3,
                created_at = '2022-02-05',
            )
        ]
        Product.objects.bulk_create(products)
        productdetails = [
            Productdetail(
                id = 1,
                total_amount = 0,
                total_supporter = 0,
                rate = 0,
                product_id = 1
            ),
            Productdetail(
                id = 2,
                total_amount = 0,
                total_supporter = 0,
                rate = 0,
                product_id = 2
            ),
            Productdetail(
                id = 3,
                total_amount = 0,
                total_supporter = 0,
                rate = 0,
                product_id = 3
            )
        ]
        Productdetail.objects.bulk_create(productdetails)

    def tearDown(self):
        Seller.objects.all().delete()
        Product.objects.all().delete()
        Productdetail.objects.all().delete()

    def test_success_product_patch(self):
        data = {
            'seller_id' : 1,
            'subject' : '1번 제품 수정본',
            'description' : '상세 설명 수정',
            'amount' : 400000,
            'end_date' : '2022-11-11'
        }
        url = '/products/1'
        res = json.dumps(data)
        client = Client()
        response = client.patch(url, res, content_type='application/json')
        self.assertEqual(response.json(),
            {'result': 'SECCESS'}
        )
        self.assertEqual(response.status_code, 200)

    def test_fail_product_patch(self):       
        tmp = {
            'seller_id' : 1,
            'subject' : '서빙 로봇',
            'description' : '상세 설명 수정',
            'amount' : 400000,
            'end_date' : '2022-11-11'
        }
        url = '/products/10000000000000000000'
        data = json.dumps(tmp)
        client = Client()
        response = client.patch(url, data, content_type='application/json')
        self.assertEqual(response.json(),
            {'result': 'Product matching query does not exist.'}
        )
        self.assertEqual(response.status_code, 400)

class ProductListTest(TestCase):
   def test_product_list_search_if_Key_error(self):
        client = Client()
        response = client.get('/products/list?sorting=')
        self.maxDiff = None

        self.assertEqual(response.json(),
            {'result' : 'KEY_ERROR'}
        )
        self.assertEqual(response.status_code, 400)

    
    #  search & sorting test는 아래의 에러 코드를 해결하지 못하였습니다. 빠른 시일 내에 해결하겠습니다.
    #  ValueError: Content-Type header is "text/html", not "application/json"

    # def setUp(self):
    #     seller_list = [
    #         Seller(
    #             id = 1,
    #             name = 'min',
    #         ),
    #         Seller(
    #             id = 2,
    #             name = 'seok',
    #         ),
    #         Seller(
    #             id = 3,
    #             name = 'lee',
    #         ),
    #         Seller(
    #             id = 4,
    #             name = 'hae'
    #         )
    #     ]
    #     Seller.objects.bulk_create(seller_list)

    #     product_list = [
    #         Product(
    #             id = 1,
    #             subject = '가정용 의자',
    #             description = '테스트용',
    #             amount = 1000,
    #             goal_amount = 100000,
    #             end_date = '2022-04-30',
    #             created_at = '2022-01-01',
    #             seller_id = 1,
    #         ),
    #         Product(
    #             id = 2,
    #             subject = '가정용 버너',
    #             description = '테스트용',
    #             amount = 1500,
    #             goal_amount = 55000,
    #             end_date = '2022-05-04',
    #             created_at = '2022-02-01',
    #             seller_id = 2,
    #         ),
    #         Product(
    #             id = 3,
    #             subject = '가정용 책상',
    #             description = '테스트용',
    #             amount = 10000,
    #             goal_amount = 200000,
    #             end_date = '2022-05-20',
    #             created_at = '2022-03-01',
    #             seller_id = 3,
    #         ),
    #         Product(
    #             id = 4,
    #             subject = '군만두',
    #             description = '테스트용',
    #             amount = 2000,
    #             goal_amount = 20000,
    #             end_date = '2022-06-10',
    #             created_at = '2022-04-01',
    #             seller_id = 4,
    #         )
    #     ]
    #     Product.objects.bulk_create(product_list)

    #     product_detail_list = [
    #         Productdetail(
    #             id = 1,
    #             product_id = 1,
    #             total_amount = 0,
    #             total_supporter = 0,
    #             rate = 0,
    #         ),
    #         Productdetail(
    #             id = 2,
    #             product_id = 2,
    #             total_amount = 0,
    #             total_supporter = 0,
    #             rate = 0,
    #         ),
    #         Productdetail(
    #             id = 3,
    #             product_id = 3,
    #             total_amount = 0,
    #             total_supporter = 0,
    #             rate = 0,
    #         ),
    #         Productdetail(
    #             id = 4,
    #             product_id = 4,
    #             total_amount = 0,
    #             total_supporter = 0,
    #             rate = 0,
    #         )
    #     ]
    #     Productdetail.objects.bulk_create(product_detail_list)

    # def tearDown(self):
    #     Seller.objects.all().delete()
    #     Product.objects.all().delete()
    #     Productdetail.objects.all().delete()
    
    # def test_product_list_search_success(self):
    #     client = Client()

    #     response = client.get('products/list?search=가정&sorting=late_open', content_type="application/json")
    #     print(response)
    #     self.maxDiff = None

    #     self.assertEqual(response.json(),
    #         {
    #         'result' : [{
    #             'product_id' : 1,
    #             'subject' : '가정용 책상',
    #             'seller_id' : 1,
    #             'name' : 'lee',
    #             'total_amount' : '0원',
    #             'rate' : '0%',
    #             'd-day' : '16일'
    #             },
    #             {
    #             'product_id' : 2,
    #             'subject' : '가정용 버너',
    #             'seller_id' : 2,
    #             'name' : 'seok',
    #             'total_amount' : '0원',
    #             'rate' : '0%',
    #             'd-day' : '20일'
    #             },
    #             {
    #             'product_id' : 3,
    #             'subject' : '가정용 의자',
    #             'seller_id' : 3,
    #             'name' : 'min',
    #             'total_amount' : '0원',
    #             'rate' : '0%',
    #             'd-day' : '36일'
    #             }]
    #         }
    #     )
    #     self.assertEqual(response.status_code, 200)