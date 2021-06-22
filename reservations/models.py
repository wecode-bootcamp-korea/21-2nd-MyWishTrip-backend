from django.db import models

class Reservation(models.Model):
    count     = models.PositiveIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user      = models.ForeignKey('users.User', on_delete=models.CASCADE)
    option    = models.ForeignKey('products.Option', on_delete=models.CASCADE)

    class Meta:
        db_table = 'reservations'