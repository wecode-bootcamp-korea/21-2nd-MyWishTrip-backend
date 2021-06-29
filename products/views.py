import json

from django.http           import JsonResponse
from django.views          import View
from django.db.models      import Avg

from .models import Product, Date, Review

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