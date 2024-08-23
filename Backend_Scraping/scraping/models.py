from django.db import models

class SKU(models.Model):
     color = models.CharField(max_length=50)
    
    # For PostgreSQL: use ArrayField for storing sizes
    #  size = ArrayField(models.CharField(max_length=10), default=list)  # For PostgreSQL
    
    # For other databases: use TextField and store sizes as a comma-separated string
     size = models.CharField(max_length=200, default="")  # Uncomment this line if not using PostgreSQL

class Product(models.Model):
    url = models.URLField(default="https://example.com/default-url")
    title = models.CharField(max_length=200, default="Untitled Product")
    price = models.CharField(max_length=20, default="0.00")
    mrp = models.CharField(max_length=20, default="0.00")
    last_7_day_sale = models.TextField(default="0")
    available_skus = models.ManyToManyField(SKU, blank=True)
    fit = models.CharField(max_length=100, default="Regular",null= True, blank=True)
    fabric = models.CharField(max_length=100, default="Cotton",null= True, blank=True)
    neck = models.TextField(null=True, blank=True, default='N/A')
    sleeve = models.TextField(null=True, blank=True, default='N/A')
    length = models.TextField(default="",null= True, blank=True)
    pattern = models.TextField(default="",null= True, blank=True)
    description = models.TextField(default="No description available.")

    def __str__(self):
        return self.title
