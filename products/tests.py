import json

from decimal         import Decimal
from datetime        import datetime
from unittest.loader import defaultTestLoader

from django.http import response
from django.test import TestCase ,Client

from .models      import *
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
                'user'        : 'test',
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
        
class ReviewTestCase(TestCase):
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
        Review.objects.all().delete()
        ReviewImage.objects.all().delete()
    
    def test_review_get(self):
        client = Client()
        data = [{
                'user'        : 'test',
                'contents'    : 'test',
                'score'       : 1,
                'manager_text': 'test',
                'create_at'   : '',
                'update_at'   : '',
                'images'       : ['test']
            }]

        response      = client.get('/products?product_id=1&page=1&page_size=1')
        response_data = response.json()
        
        data[0]['create_at'] = response_data['reviews'][0]['create_at']
        data[0]['update_at'] = response_data['reviews'][0]['update_at']

        self.assertEqual(response.json(),{'reviews':data})
        self.assertEquals(response.status_code, 200)
        


class RegionsTest(TestCase):
    @classmethod
    def setUpTestData(self):
        Region.objects.bulk_create([
            Region(
            id   = 1,
            name = "서울"
            ),
            Region(
            id   = 2,
            name = "제주도"
            )
        ])
        Landmark.objects.bulk_create([
            Landmark(
                id        = 1,
                name      = "올레길",
                region_id = 2
            ),
            Landmark(
                id        = 2,
                name      = "성산일출봉",
                region_id = 2
            ),
            Landmark(
                id        = 3,
                name      = "경복궁",
                region_id = 1
            ),
            Landmark(
                id        = 4,
                name      = "북촌한옥",
                region_id = 1
            )
        ])
    def tearDown(self):
        Region.objects.all().delete()
        Landmark.objects.all().delete()

    def test_RegionsView_get_success(self):
        client   = Client()
        response = client.get('/products/regions')
        
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 
            {"regions" : [
                    {"id" : 1,
                    "name" : "서울",
                    "landmark" : ["경복궁","북촌한옥"]},
                    {"id" : 2,
                    "name" : "제주도",
                    "landmark" : ["올레길","성산일출봉"]}]
                }
        )

class ProductsListTest(TestCase):
    maxDiff = None
    @classmethod
    def setUpTestData(self):
        User.objects.create(
            id          = 1,
            email       = "minionRock123",
            name        = "kingbob",
            password    = " minionisking123!",
            signup_type = "kakakotalk",
        )
        
        Region.objects.bulk_create([
             Region(
                id   = 1,
                name = "서울",
            ),
            Region(
                id   = 2,
                name = "제주도",
            )
        ])
        MainCategory.objects.bulk_create([
            MainCategory(
                id   = 1,
                name = "투어"
            ),
            MainCategory(
                id   = 2,
                name = "입장권"
            )
        ])
        SubCategory.objects.bulk_create([
            SubCategory(
                id              = 1,
                name            = "시내투어",
                maincategory_id = 1
            ),
            SubCategory(
                id              = 2,
                name            = "자연투어",
                maincategory_id = 1
            ),
            SubCategory(
                id              = 3,
                name            = "랜선투어",
                maincategory_id = 1
            )
        ])

        Product.objects.bulk_create([
            Product(
                id             = 1,
                name           = '[제주] 시내투어',
                price          =  8000,
                discount       = 0.3,
                main_image     = "~~~",
                detail_image   = "!!~",
                region_id      = 2,
                subcategory_id = 1
            ),
            Product(
                id             = 2,
                name           = '[제주] 랜선투어',
                price          =  15000,
                discount       = 0.1,
                main_image     = "~~~",
                detail_image   = "!!~",
                region_id      = 2,
                subcategory_id = 3
            ),
            Product(
                id             = 3,
                name           = '[제주] 자연투어',
                price          =  8000,
                discount       = 0.3,
                main_image     = "~~~",
                detail_image   = "!!~",
                region_id      = 2,
                subcategory_id = 2
            ),
            Product(
                id             = 4,
                name           = '[서울] 시내투어',
                price          =  30000,
                discount       = 0.1,
                main_image     = "~~~",
                detail_image   = "!!~",
                region_id      = 1,
                subcategory_id = 1
            ),
            Product(
                id             = 5,
                name           = '[서울] 랜선투어',
                price          =  8000,
                discount       = 0.3,
                main_image     = "~~~",
                detail_image   = "!!~",
                region_id      = 1,
                subcategory_id = 3
            )
        ])

        # create_at- setting
        day = [10,11,12,13,14]
        dt = [datetime(2021,6,i,0,0,0).date() for i in day]
        for index,product in enumerate(Product.objects.all()):
            product.create_at = str(dt[index])
            product.save()
            
        Landmark.objects.bulk_create([
            Landmark(
                id        = 1,
                name      = "올레길",
                region_id = 2
            ),
            Landmark(
                id        = 2,
                name      = "성산일출봉",
                region_id = 2
            ),
            Landmark(
                id        = 3,
                name      = "경복궁",
                region_id = 1
            ),
            Landmark(
                id        = 4,
                name      = "북촌한옥",
                region_id = 1
            )
        ])
        ProductLandmark.objects.bulk_create([
            ProductLandmark(
                id          = 1,
                product_id  = 1,
                landmark_id = 1
            ),
            ProductLandmark(
                id          = 2,
                product_id  = 1,
                landmark_id = 2
            )
        ])
        Review.objects.bulk_create([
            Review(
                id = 1,
                contents     = "review of 1-1",
                score        = 5,
                manager_text = "welcome",
                product_id   = 1,
                user_id      = 1
            ),
            Review(
                id=2,
                contents     = "review of 1-2",
                score        = 5,
                manager_text = "",
                product_id   = 1,
                user_id      = 1
            ),
            Review(
                id=3,
                contents     = "review of 1-3",
                score        = 5,
                manager_text = "welcome",
                product_id   = 1,
                user_id      = 1
            ),
            Review(
                id= 4,
                contents     = "review of 2-1",
                score        = 5,
                manager_text = "welcome",
                product_id   = 2,
                user_id      = 1
            ),
            Review(
                id=5,
                contents     = "review of 2-2",
                score        = 4,
                manager_text = "welcome",
                product_id   = 2,
                user_id      = 1
            )
        ])
        Option.objects.bulk_create([
            Option(
                id         = 1,
                name       = "대인",
                price      = 3000,
                product_id = 1
            ),
            Option(
                id         = 2,
                name       = "소인",
                price      = 1000,
                product_id = 1
            ),
            Option(
                id         = 3,
                name       = "대인",
                price      = 3000,
                product_id = 2
            ),
            Option(
                id         = 4,
                name       = "소인",
                price      = 1000,
                product_id = 2
            )
        ])
        Date.objects.bulk_create([
            Date(
                id        = 1,
                date      = '2021-06-21',
                count     = 3,
                option_id = 1
            ),
            Date(
                id        = 2,
                date      = '2021-06-22',
                count     = 3,
                option_id = 1
            ),
            Date(
                id        = 3,
                date      = '2021-06-23',
                count     = 3,
                option_id = 3
            ),
            Date(
                id        = 4,
                date      = '2021-06-24',
                count     = 3,
                option_id = 3
            )
        ])
    def tearDown(self):
        User.objects.all().delete()
        Product.objects.all().delete()
        MainCategory.objects.all().delete()
        SubCategory.objects.all().delete()
        Landmark.objects.all().delete()
        ProductLandmark.objects.all().delete()
        Review.objects.all().delete()
        Option.objects.all().delete()
        Date.objects.all().delete()
    
    #지역 
    def test_ProductsView_get_region(self):
            client = Client()
            response = client.get('/products?region=제주도')
            print(response.json())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), 
                            {"products" : [
                                {"id"           : 3,
                                "name"          : '[제주] 자연투어',
                                "main_image"    : "~~~",
                                "average_score" : 0,
                                "create_at"     : "2021-06-12T00:00:00",
                                "price"         : 8000,
                                "discount"      : 0.3,
                                "region"        : "제주도",
                                "review_count"  : 0,
                                "sub_category"  : "자연투어",
                                "main_category" : "투어",
                                "landmark"      : [],
                                "date"          : []
                                },{"id"           : 2,
                                "name"          : '[제주] 랜선투어',
                                "main_image"    : "~~~",
                                "average_score" : 4,
                                "create_at"     : "2021-06-11T00:00:00",
                                "price"         : 15000,
                                "discount"      : 0.1,
                                "region"        : "제주도",
                                "review_count"  : 2,
                                "sub_category"  : "랜선투어",
                                "main_category" : "투어",
                                "landmark"      : [],
                                "date"          : ['2021-06-23','2021-06-24']
                                },
                                {"id"           : 1,
                                "name"          : '[제주] 시내투어',
                                "main_image"    : "~~~",
                                "average_score" : 5,
                                "create_at"     : "2021-06-10T00:00:00",
                                "price"         : 8000,
                                "discount"      : 0.3,
                                "region"        : "제주도",
                                "review_count"  : 3,
                                "sub_category"  : "시내투어",
                                "main_category" : "투어",
                                "landmark"      : ["올레길","성산일출봉"],
                                "date"          : ['2021-06-21','2021-06-22']
                                }

                            ]
                        }
                    )
    #랜드마크
    def test_ProductsView_get_landmark(self):
            client = Client()
            response = client.get('/products?landmarks=올레길&성산일출봉')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(),
                {"products" : [
                                {"id"           : 1,
                                "name"          : '[제주] 시내투어',
                                "main_image"    : "~~~",
                                "average_score" : 5,
                                "create_at"     : "2021-06-10T00:00:00",
                                "price"         : 8000,
                                "discount"      : 0.3,
                                "region"        : "제주도",
                                "review_count"  : 3,
                                "sub_category"  : "시내투어",
                                "main_category" : "투어",
                                "landmark"      : ["올레길","성산일출봉"],
                                "date"          : ['2021-06-21','2021-06-22']
                                }
                            ]
                        }
                    )

    #메인카테고리
    def test_ProductsView_get_main_category(self):
            client = Client()
            response = client.get('/products?main_category=투어')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), 
                            {"products" : [
                                {"id"           : 5,
                                "name"          : '[서울] 랜선투어',
                                "main_image"    : "~~~",
                                "average_score" : 0,
                                "create_at"     : "2021-06-14T00:00:00",
                                "price"         : 8000,
                                "discount"      : 0.3,
                                "region"        : "서울",
                                "review_count"  : 0,
                                "sub_category"  : "랜선투어",
                                "main_category" : "투어",
                                "landmark"     : [],
                                "date"         : []
                                },
                                {"id"           : 4,
                                "name"          : '[서울] 시내투어',
                                "main_image"    : "~~~",
                                "average_score" : 0, 
                                "create_at"     : "2021-06-13T00:00:00",
                                "price"         : 30000,
                                "discount"      : 0.1,
                                "region"        : "서울",
                                "review_count"  : 0,
                                "sub_category"  : "시내투어",
                                "main_category" : "투어",
                                "landmark"     : [],
                                "date"         : []
                                },
                                {"id"           : 3,
                                "name"          : '[제주] 자연투어',
                                "main_image"    : "~~~",
                                "average_score" : 0,
                                "create_at"     : "2021-06-12T00:00:00",
                                "price"         : 8000,
                                "discount"      : 0.3,
                                "region"        : "제주도",
                                "review_count"  : 0,
                                "sub_category"  : "자연투어",
                                "main_category" : "투어",
                                "landmark"     : [],
                                "date"         : []
                                },
                                {"id"           : 2,
                                "name"          : '[제주] 랜선투어',
                                "main_image"    : "~~~",
                                "average_score" : 4,
                                "create_at"     : "2021-06-11T00:00:00",
                                "price"         : 15000,
                                "discount"      : 0.1,
                                "region"        : "제주도",
                                "review_count"  : 2,
                                "sub_category"  : "랜선투어",
                                "main_category" : "투어",
                                "landmark"      : [],
                                "date"          : ['2021-06-23','2021-06-24']
                                },
                                {"id"           : 1,
                                "name"          : '[제주] 시내투어',
                                "main_image"    : "~~~",
                                "average_score" : 5,
                                "create_at"     : "2021-06-10T00:00:00",
                                "price"         : 8000,
                                "discount"      : 0.3,
                                "region"        : "제주도",
                                "review_count"  : 3,
                                "sub_category"  : "시내투어",
                                "main_category" : "투어",
                                "landmark"      : ["올레길","성산일출봉"],
                                "date"          : ['2021-06-21','2021-06-22']
                                }
                            ]
                        }
                    )
#     # 서브카테고리
    def test_ProductsView_get_sub_category(self):
            client = Client()
            response = client.get('/products?sub_category=랜선투어')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), 
                            {"products" : [
                                {"id"           : 5,
                                "name"          : '[서울] 랜선투어',
                                "main_image"    : "~~~",
                                "average_score" : 0,
                                "create_at"     : "2021-06-14T00:00:00",
                                "price"         : 8000,
                                "discount"      : 0.3,
                                "region"        : "서울",
                                "review_count"  : 0,
                                "sub_category"  : "랜선투어",
                                "main_category" : "투어",
                                "landmark"     : [],
                                "date"         : []
                                }, {"id"           : 2,
                                "name"          : '[제주] 랜선투어',
                                "main_image"    : "~~~",
                                "average_score" : 4,
                                "create_at"     : "2021-06-11T00:00:00",
                                "price"         : 15000,
                                "discount"      : 0.1,
                                "region"        : "제주도",
                                "review_count"  : 2,
                                "sub_category"  : "랜선투어",
                                "main_category" : "투어",
                                "landmark"     : [],
                                "date"         : ['2021-06-24','2021-06-23']
                                }
                            ]
                        }
                    )
    # 점수
    def test_ProductsView_get_score_from_4_to_5(self):
            client = Client()
            response = client.get('/products?score=4~5')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), 
                          {"products" : [
                                {"id"           : 2,
                                "name"          : '[제주] 랜선투어',
                                "main_image"    : "~~~",
                                "average_score" : 4,
                                "create_at"     : "2021-06-11T00:00:00",
                                "price"         : 15000,
                                "discount"      : 0.1,
                                "region"        : "제주도",
                                "review_count"  : 2,
                                "sub_category"  : "랜선투어",
                                "main_category" : "투어",
                                "landmark"     : [],
                                "date"         : ['2021-06-23','2021-06-24']
                                },
                                {"id"           : 1,
                                "name"          : '[제주] 시내투어',
                                "main_image"    : "~~~",
                                "average_score" : 5,
                                "create_at"     : "2021-06-10T00:00:00",
                                "price"         : 8000,
                                "discount"      : 0.3,
                                "region"        : "제주도",
                                "review_count"  : 3,
                                "sub_category"  : "시내투어",
                                "main_category" : "투어",
                                "landmark"     : ["올레길","성산일출봉"],
                                "date"         : ['2021-06-21','2021-06-22']
                                }
                            ]
                        }
                     )
    #date
    def test_ProductsView_get_date_from_20210621_to_20210622(self):
            client = Client()
            response = client.get('/products?date=2021-06-21~2021-06-22')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), 
                          {"products" : [
                                {"id"           : 1,
                                "name"          : '[제주] 시내투어',
                                "main_image"    : "~~~",
                                "average_score" : 5,
                                "create_at"     : "2021-06-10T00:00:00",
                                "price"         : 8000,
                                "discount"      : 0.3,
                                "region"        : "제주도",
                                "review_count"  : 3,
                                "sub_category"  : "시내투어",
                                "main_category" : "투어",
                                "landmark"     : ["올레길","성산일출봉"],
                                "date"         : ['2021-06-21','2021-06-22']
                                }
                            ]
                        }
                    )
    #price 8000~10000
    def test_ProductsView_get_date_from_8000_10000(self):
            client = Client()
            response = client.get('/products?price=8000~10000')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), 
                          {"products" : [
                                {"id"           : 5,
                                "name"          : '[서울] 랜선투어',
                                "main_image"    : "~~~",
                                "average_score" : 0,
                                "create_at"     : "2021-06-14T00:00:00",
                                "price"         : 8000,
                                "discount"      : 0.3,
                                "region"        : "서울",
                                "review_count"  : 0,
                                "sub_category"  : "랜선투어",
                                "main_category" : "투어",
                                "landmark"     : [],
                                "date"         : []
                                },
                                {"id"           : 3,
                                "name"          : '[제주] 자연투어',
                                "main_image"    : "~~~",
                                "average_score" : 0,
                                "create_at"     : "2021-06-12T00:00:00",
                                "price"         : 8000,
                                "discount"      : 0.3,
                                "region"        : "제주도",
                                "review_count"  : 0,
                                "sub_category"  : "자연투어",
                                "main_category" : "투어",
                                "landmark"     : [],
                                "date"         : []
                                },
                                {"id"           : 1,
                                "name"          : '[제주] 시내투어',
                                "main_image"    : "~~~",
                                "average_score" : 5,
                                "create_at"     : "2021-06-10T00:00:00",
                                "price"         : 8000,
                                "discount"      : 0.3,
                                "region"        : "제주도",
                                "review_count"  : 3,
                                "sub_category"  : "시내투어",
                                "main_category" : "투어",
                                "landmark"     : ["올레길","성산일출봉"],
                                "date"         : ['2021-06-21','2021-06-22']
                                } 
                            ]
                        }
                    )
    # 제주도 최신순 정렬
    def test_ProductsView_get_region_sort_recent(self):
            client = Client()
            response = client.get('/products?region=제주도&sort=recent')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), 
                            {"products" : [
                                {"id"           : 3,
                                "name"          : '[제주] 자연투어',
                                "main_image"    : "~~~",
                                "average_score" : 0,
                                "create_at"     : "2021-06-12T00:00:00",
                                "price"         : 8000,
                                "discount"      : 0.3,
                                "region"        : "제주도",
                                "review_count"  : 0,
                                "sub_category"  : "자연투어",
                                "main_category" : "투어",
                                "landmark"     : [],
                                "date"         : []
                                },
                                {"id"           : 2,
                                "name"          : '[제주] 랜선투어',
                                "main_image"    : "~~~",
                                "average_score" : 4,
                                "create_at"     : "2021-06-11T00:00:00",
                                "price"         : 15000,
                                "discount"      : 0.1,
                                "region"        : "제주도",
                                "review_count"  : 2,
                                "sub_category"  : "랜선투어",
                                "main_category" : "투어",
                                "landmark"     : [],
                                "date"         : ['2021-06-23','2021-06-24']
                                },
                                {"id"           : 1,
                                "name"          : '[제주] 시내투어',
                                "main_image"    : "~~~",
                                "average_score" : 5,
                                "create_at"     : "2021-06-10T00:00:00",
                                "price"         : 8000,
                                "discount"      : 0.3,
                                "region"        : "제주도",
                                "review_count"  : 3,
                                "sub_category"  : "시내투어",
                                "main_category" : "투어",
                                "landmark"     : ["올레길","성산일출봉"],
                                "date"         : ['2021-06-21','2021-06-22']
                                }
                            ]
                        }
                    )

    #정렬 = 가격 닞은 순
    def test_ProductsView_get_region_sort_price_ASC(self):
            client = Client()
            response = client.get('/products?region=제주도&sort=price_ASC')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), 
                            {"products" : [
                                {"id"           : 1,
                                "name"          : '[제주] 시내투어',
                                "main_image"    : "~~~",
                                "average_score" : 5,
                                "create_at"     : "2021-06-10T00:00:00",
                                "price"         : 8000,
                                "discount"      : 0.3,
                                "region"        : "제주도",
                                "review_count"  : 3,
                                "sub_category"  : "시내투어",
                                "main_category" : "투어",
                                "landmark"     : ["올레길","성산일출봉"],
                                "date"         : ['2021-06-21','2021-06-22']
                                },
                                {"id"           : 3,
                                "name"          : '[제주] 자연투어',
                                "main_image"    : "~~~",
                                "average_score" : 0,
                                "create_at"     : "2021-06-12T00:00:00",
                                "price"         : 8000,
                                "discount"      : 0.3,
                                "region"        : "제주도",
                                "review_count"  : 0,
                                "sub_category"  : "자연투어",
                                "main_category" : "투어",
                                "landmark"     : [],
                                "date"         : []
                                },
                                {"id"           : 2,
                                "name"          : '[제주] 랜선투어',
                                "main_image"    : "~~~",
                                "average_score" : 4,
                                "create_at"     : "2021-06-11T00:00:00",
                                "price"         : 15000,
                                "discount"      : 0.1,
                                "region"        : "제주도",
                                "review_count"  : 2,
                                "sub_category"  : "랜선투어",
                                "main_category" : "투어",
                                "landmark"     : [],
                                "date"         : ['2021-06-23','2021-06-24']
                                }
                            ]
                        }
                    )

    #정렬 = 가격 높은 순  
    def test_ProductsView_get_region_sort_review_price_DESC(self):
            client = Client()
            response = client.get('/products?region=제주도&sort=price_DESC')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), 
                            {"products" : [
                                {"id"           : 2,
                                "name"          : '[제주] 랜선투어',
                                "main_image"    : "~~~",
                                "average_score" : 4,
                                "create_at"     : "2021-06-11T00:00:00",
                                "price"         : 15000,
                                "discount"      : 0.1,
                                "region"        : "제주도",
                                "review_count"  : 2,
                                "sub_category"  : "랜선투어",
                                "main_category" : "투어",
                                "landmark"     : [],
                                "date"         : ['2021-06-23','2021-06-24']
                                },
                                {"id"           : 1,
                                "name"          : '[제주] 시내투어',
                                "main_image"    : "~~~",
                                "average_score" : 5,
                                "create_at"     : "2021-06-10T00:00:00",
                                "price"         : 8000,
                                "discount"      : 0.3,
                                "region"        : "제주도",
                                "review_count"  : 3,
                                "sub_category"  : "시내투어",
                                "main_category" : "투어",
                                "landmark"     : ["올레길","성산일출봉"],
                                "date"         : ['2021-06-21','2021-06-22']
                                },
                                {"id"           : 3,
                                "name"          : '[제주] 자연투어',
                                "main_image"    : "~~~",
                                "average_score" : 0,
                                "create_at"     : "2021-06-12T00:00:00",
                                "price"         : 8000,
                                "discount"      : 0.3,
                                "region"        : "제주도",
                                "review_count"  : 0,
                                "sub_category"  : "자연투어",
                                "main_category" : "투어",
                                "landmark"     : [],
                                "date"         : []
                                }
                            ]
                        }
                    )
