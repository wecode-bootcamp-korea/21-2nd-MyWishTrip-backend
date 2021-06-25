import json

from django.http  import JsonResponse
from django.views import View
from django.db    import transaction

from .models         import Reservation
from users.utils     import user_decorator
from products.models import Date

class ReservationVeiw(View):
    @user_decorator
    @transaction.atomic
    def post(self, request):
        data = json.loads(request.body)
        
        for data in data['reservations']:
            reservation, created = Reservation.objects.get_or_create(
                user_id = request.user.id,
                option_id = data['option_id'],
                count = 1)
        
            if created:
                reservation.count = data["count"]
            else:
                reservation.count += data["count"]

            reservation.save()

            date = Date.objects.get(id=data['date_id'])
            date.count -= data["count"]
            date.save()

        return JsonResponse({'reservations':'SUCCESS'}, status=201)