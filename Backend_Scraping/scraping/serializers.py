# serializers.py
from rest_framework import serializers
from .models import Product, SKU

class SKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = ['color', 'size']

class ProductSerializer(serializers.ModelSerializer):
    available_skus = SKUSerializer(many=True)

    class Meta:
        model = Product
        fields = [
             'url', 'title', 'price', 'mrp', 'last_7_day_sale', 
            'available_skus', 'fit', 'fabric', 'neck', 'sleeve', 'length', 
            'pattern', 'description'
        ]
