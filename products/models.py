from django.db    import models

class MainCategory(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'maincategories'

class SubCategory(models.Model):
    name         = models.CharField(max_length=20, unique=True)
    maincategory = models.ForeignKey(MainCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = 'subcategories'

class Region(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'regions'

class Landmark(models.Model):
    name   = models.CharField(max_length=20)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        db_table = 'landmarks'

class ProductLandmark(models.Model):
    landmark = models.ForeignKey(Landmark, on_delete=models.CASCADE)
    product  = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_landmarks'

class Product(models.Model):
    name         = models.CharField(max_length=100, unique=True)
    price        = models.DecimalField(max_digits=10, decimal_places=2)
    discount     = models.FloatField(default=0)
    main_image   = models.URLField(max_length=200)
    detail_image = models.URLField(max_length=1000)
    create_at    = models.DateTimeField(auto_now_add=True)
    update_at    = models.DateTimeField(auto_now=True)
    subcategory  = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    region       = models.ForeignKey(Region, on_delete=models.CASCADE)
    landmarks    = models.ManyToManyField(Landmark, through='ProductLandmark')
    wishes       = models.ManyToManyField('users.User', through='wishes.Wish', related_name='wishes_set')
    reviews      = models.ManyToManyField('users.User', through='Review', related_name='reviews_set')

    class Meta:
        db_table = 'products'

class Option(models.Model):
    name    = models.CharField(max_length=100)
    price   = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'options'

class Date(models.Model):
    date   = models.DateField()
    count  = models.PositiveIntegerField(default=0)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)

    class Meta:
        db_table = 'dates'

class Review(models.Model):
    contents     = models.TextField()
    score        = models.PositiveIntegerField(default=0)
    manager_text = models.TextField(null=True)
    create_at    = models.DateTimeField(auto_now_add=True)
    update_at    = models.DateTimeField(auto_now=True)
    user         = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product      = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviews'

class ReviewImage(models.Model):
    image  = models.URLField(max_length=200)
    review = models.ForeignKey(Review,on_delete=models.CASCADE)

    class Meta:
        db_table = 'review_images'