
import json
import os
from django.core.management.base import BaseCommand
from scraping.models import Product, SKU  # Replace 'myapp' with your actual app name

class Command(BaseCommand):
    help = 'Load products from JSON file into the database'

    def handle(self, *args, **kwargs):
        # Determine the path to the products.json file relative to this command file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(current_dir, 'products.json')

        # Check if the JSON file exists
        if not os.path.exists(json_file_path):
            self.stdout.write(self.style.ERROR(f'File not found: {json_file_path}'))
            return

        # Load the JSON data
        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                products = json.load(f)
        except json.JSONDecodeError as e:
            self.stdout.write(self.style.ERROR(f'Error decoding JSON: {e}'))
            return

        # Iterate over each product and save to the database
        for product_data in products:
            # Handle SKUs
           
              
            # Create or update the Product object
            product_obj, created = Product.objects.update_or_create(
                id=product_data.get('id'),  # Assuming 'id' is unique
                defaults={
                    
                    'url': product_data.get('url', 'https://example.com/default-url'),
                    'title': product_data.get('title', 'Untitled Product'),
                    'price': product_data.get('price', '0.00'),
                    'mrp': product_data.get('mrp', '0.00'),
                    'last_7_day_sale': product_data.get('last_7_day_sale', '0'),
                    'fit': product_data.get('fit', 'Regular'),
                    'fabric': product_data.get('fabric', 'Cotton'),
                    'neck': product_data.get('neck', 'Round Neck'),
                    'sleeve': product_data.get('sleeve', 'Short Sleeve'),
                    'length': product_data.get('length', 'Regular'),
                    'pattern': product_data.get('pattern', 'Solid'),
                    'description': product_data.get('description', 'No description available.'),
                }
            )

            # Associate SKUs with the Product
           
            for sku_data in product_data.get('available_skus', []):
                sku, created = SKU.objects.get_or_create(
                    color=sku_data['color'],
                    size=sku_data['size']  # Store sizes as list (PostgreSQL) or comma-separated string
                )
                product_obj.available_skus.add(sku)
            
            product_obj.save()
 
        self.stdout.write(self.style.SUCCESS('Successfully loaded products'))
