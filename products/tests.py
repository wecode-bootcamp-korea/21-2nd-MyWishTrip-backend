from datetime import datetime
from decimal  import Decimal
import json
from unittest.loader import defaultTestLoader
from django.http import response
from django.test import TestCase, Client

from .models      import Date, Option, Product, Region, Review, ReviewImage,SubCategory,MainCategory
from users.models import User

class ProductTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        MainCategory.objects.create(id=1,name='test')
        SubCategory.objects.create(id=1,name='test', maincategory_id=1)
        Region.objects.create(id=1,name='test')
        User.objects.create(id=1,name='test', password='123')
        Product.objects.create(
            id=1,
            name='test',
            price=Decimal(123.00),
            discount=0.1,
            main_image='test',
            detail_image='test',
            subcategory_id=1,
            region_id=1
        )
        Option.objects.create(
            id=1,
            name='test',
            price=Decimal(1),
            product_id=1
        )
        Date.objects.create(
            id=1,
            date=datetime.strptime('2021-06-26', '%Y-%m-%d'),
            count=1,
            option_id=1
        )
        Review.objects.create(
            id=1,
            contents='test',
            score=1,
            manager_text='test',
            product_id=1,
            user_id=1
        )
        ReviewImage.objects.create(id=1, image='test', review_id=1)
    
    def tearDown(self):
        User.objects.all().delete()
        MainCategory.objects.all().delete()
        SubCategory.objects.all().delete()
        Region.objects.all().delete()
        Product.objects.all().delete()
        Date.objects.all().delete()
        Option.objects.all().delete()
        Review.objects.all().delete()
        ReviewImage.objects.all().delete()

    def test_get_product(self):
        client = Client()

        data = {
            'name'         : 'test',
            'price'        : '123.00',
            'discount'     : 0.1,
            'main_image'   : 'test',
            'detail_image' : 'test',
            'total_score'  : 1.0,
            'total_review' : 1,
            'reviews'      : [{
                'contents'    : 'test',
                'score'       : 1,
                'manager_text': 'test',
                'create_at'   : '',
                'update_at'   : '',
                'images'       : ['test']
            }],
            'options'   : [{
                'name'  : 'test',
                'price' : '1.00',
                'dates' : ['2021-06-26']
            }]
        }

        response = client.get('/products/1', content_type = 'application/json')
        response_data = response.json()
        
        data['reviews'][0]['create_at'] = response_data['product']['reviews'][0]['create_at']
        data['reviews'][0]['update_at'] = response_data['product']['reviews'][0]['update_at']
        
        self.assertEqual(response.json(),{'product':data})
        self.assertEqual(response.status_code, 200)
    
    def test_get_product_error(self):
        client = Client()

        response = client.get('/products/2', content_type = 'application/json')

        self.assertEqual(response.json(),{'message':'NOT EXIST'})
        self.assertEqual(response.status_code, 404)

class OptionTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        MainCategory.objects.create(id=1,name='test')
        SubCategory.objects.create(id=1,name='test', maincategory_id=1)
        Region.objects.create(id=1,name='test')
        User.objects.create(id=1,name='test', password='123')
        Product.objects.create(
            id=1,
            name='test',
            price=Decimal(123.00),
            discount=0.1,
            main_image='test',
            detail_image='test',
            subcategory_id=1,
            region_id=1
        )
        Option.objects.create(
            id=1,
            name='test',
            price=Decimal(1),
            product_id=1
        )
        Date.objects.create(
            id=1,
            date=datetime.strptime('2021-06-26', '%Y-%m-%d'),
            count=2,
            option_id=1
        )
    
    def tearDown(self):
        Option.objects.all().delete()
        Date.objects.all().delete()

    def test_post_option(self):
        client = Client()

        body_data = {'option_id' : 1, 'count' : 2}
        data      = {'status' : False}
        response  = client.post('/products/option', json.dumps(body_data), content_type='application/json')

        self.assertEqual(response.json(),data)
        self.assertEqual(response.status_code, 200)
    
    def test_post_option_error(self):
        client = Client()

        body_data = {'option_id' : 2, 'count' : 2}
        data      = {'message':'NOT EXIST'}
        response  = client.post('/products/option', json.dumps(body_data), content_type='application/json')

        self.assertEqual(response.json(),data)
        self.assertEqual(response.status_code, 404)
        