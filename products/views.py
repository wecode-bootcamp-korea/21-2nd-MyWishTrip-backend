import json

from django.db.models.aggregates import Avg
from django.db.models.fields     import IntegerField
from django.db.models.query      import Prefetch
from django.views                import View
from django.http                 import JsonResponse
from django.core                 import exceptions
from django.http                 import JsonResponse
from django.db.models            import Q, Count,ExpressionWrapper,IntegerField,Sum
from django.db.models.functions  import Coalesce


from products.models import Product, Date, Region, Review, ReviewImage,Option, SubCategory, MainCategory

class RegionsView(View):
    def get(self,request):
        regions = [ {"id"   : region.id,
                     "name" :region.name, 
                    } for region in Region.objects.all()]
        return JsonResponse({"regions": regions}, status= 200)

class ProductView(View):
    def get(self, request, product_id):
        product = Product.objects.filter(id=product_id).prefetch_related(
            'review_set', 'review_set__user','review_set__reviewimage_set',
            'option_set', 'option_set__date_set').first()

        if not product:
            return JsonResponse({'message':'NOT EXIST'}, status=404)

        total_score = product.review_set.aggregate(Avg('score'))['score__avg']

        result = {
            'name'         : product.name,
            'price'        : product.price,
            'discount'     : product.discount,
            'main_image'   : product.main_image,
            'detail_image' : product.detail_image,
            'total_score'  : total_score if total_score != None else 0,
            'total_review' : product.review_set.count() if product.review_set.count() > 0 else 0,
            'reviews'      : [{
                'user'         : review.user.name,
                'contents'     : review.contents,
                'score'        : review.score,
                'manager_text' : review.manager_text,
                'create_at'    : review.create_at,
                'update_at'    : review.update_at,
                'images'       : [data.image for data in review.reviewimage_set.all()]
            }for review in product.review_set.all()],
            'options'      : [{
                'name'  : option.name,
                'price' : option.price,
                'dates' : [data.date for data in option.date_set.all()]
            } for option in product.option_set.all()]
        }

        return JsonResponse({'product':result}, status=200)

class OptionView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            date = Date.objects.get(id=data['option_id'])
        
            result = (True if date.count > data['count'] else False)

            return JsonResponse({'status':result}, status=200)

        except Date.DoesNotExist:
            return JsonResponse({'message':'NOT EXIST'}, status=404)

class ReviewView(View):
    def get(self, request):
        product_id = request.GET.get('product_id')
        offset     = int(request.GET.get('offset',0))
        limit      = int(request.GET.get('limit',3))

        reviews = Review.objects.filter(product_id=product_id).prefetch_related('user','reviewimage_set')[offset:limit]

        result = [{
                'user'         : review.user.name,
                'contents'     : review.contents,
                'score'        : review.score,
                'manager_text' : review.manager_text,
                'create_at'    : review.create_at,
                'update_at'    : review.update_at,
                'images'       : [data.image for data in review.reviewimage_set.all()]
                } for review in reviews]

        return JsonResponse({'reviews':result}, status=200)
class RegionsView(View):
    def get(self,request):
        regions = [ {"id"       : region.id,
                    "name"     : region.name, 
                    "landmark" : [landmark.name for landmark in region.landmark_set.all()]
                    } for region in Region.objects.all()]
        return JsonResponse({"regions": regions}, status= 200)  

class ProductsView(View):
    def get(self,request):
        region        = request.GET.get("region",None)
        landmarks      = request.GET.getlist("landmarks",None)
        sub_category  = request.GET.get("sub_category",None)
        main_category = request.GET.get("main_category",None)
        score         = request.GET.get("score", None)
        date          = request.GET.get("date",None)
        price         = request.GET.get("price",None)
        sort          = request.GET.get("sort","recent")
        search_word   = request.GET.get('search_word', None)
        limit         = int(request.GET.get('limit', 10))
        offset        = int(request.GET.get('offset',1))
        
        offset = limit*(offset-1)
        
        q = Q()
        if search_word:
            q &= Q(name__icontains = search_word)

        if sub_category:
            q &= Q(subcategory__name = sub_category)
        
        if main_category:
            q &= Q(subcategory__maincategory__name = main_category)
        
        if region:
            q &= Q(region__name = region)
        
        if landmarks:
            q &= Q(landmarks__name__in = landmarks)

        if score:
            score =score.split("~")
            q &= Q(average_review_score__gte = score[0])
            q &= Q(average_review_score__lte = score[1])
        
        if date:
            date = date.split("~")
            q &= Q(option__date__date__gte = date[0])
            q &= Q(option__date__date__lte = date[1])
        
        if price:
            price = price.split("~")
            q &= Q(price__gte = price[0]) 
            q &= Q(price__lte = price[1])

    
        products= Product.objects.all().prefetch_related(
            'subcategory',
            'subcategory__maincategory',
            'option_set__date_set',
            'review_set',
            'region',
            'region__landmark_set'
        ).annotate(\
        average_review_score = ExpressionWrapper(Coalesce(Avg('review__score'),0),output_field= IntegerField())).filter(q)
        
        sort_dict = {"recent"              : "-create_at",
                    "average_review_score" : "-average_review_score",
                    "price_ASC"            : "price",
                    "price_DESC"           : "-price"
                    }

        products = products.order_by(sort_dict[sort])[offset : offset+limit]
        
        result = [ 
            {"id"           : product.id,
            "name"          : product.name,
            "main_image"    : product.main_image,
            "create_at"     : product.create_at,
            "discount"      : product.discount,
            "price"         : int(product.price),
            "region"        : product.region.name,
            "review_count"  : product.review_set.count(),
            "average_score" : int(product.average_review_score),
            "sub_category"  : product.subcategory.name,
            "main_category" : product.subcategory.maincategory.name,
            "landmark"      : [landmark.name for landmark in product.landmarks.all()],
            "date"          : list(set([date.date for date in Date.objects.filter(option__product = product.id)]))
            } for product in products ]
            
        return JsonResponse({"products": result}, status= 200)
