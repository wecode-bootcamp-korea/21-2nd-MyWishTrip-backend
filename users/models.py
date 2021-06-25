from django.db import models

class User(models.Model):
    email       = models.CharField(max_length=45, unique=True)
    name        = models.CharField(max_length=20)
    password    = models.CharField(max_length=200, null=True)
    signup_type = models.CharField(max_length=45)
    social_id   = models.CharField(max_length=45, null=True)
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateField(auto_now=True)
    options     = models.ManyToManyField('products.Option', through='reservations.Reservation')

    class Meta:
        db_table = 'users'