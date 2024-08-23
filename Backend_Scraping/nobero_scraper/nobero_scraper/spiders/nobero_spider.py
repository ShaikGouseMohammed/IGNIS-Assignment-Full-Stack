# # import scrapyfrom scrapy.http import HtmlResponse
# # import requests
# # import re
# # from bs4 import BeautifulSoup

# # class NoberoSpider(scrapy.Spider):
# #     name = "nobero"
# #     start_urls = ['https://nobero.com/pages/men']

# #     def parse(self, response):
# #         # Using requests to fetch the content
# #         page = requests.get(self.start_urls[0])
        
# #         # Creating a Scrapy response object from requests content
# #         response = HtmlResponse(url=page.url, body=page.text, encoding='utf-8')
        
# #         # Extract category URLs
# #         categories = response.css('div.custom-page-season-grid-item a::attr(href)').getall()
# #         if not categories:
# #             self.logger.error("No categories found on the page!")
        
# #         for category in categories:
# #             full_url = response.urljoin(category.strip())
# #             self.logger.info(f"Following category URL: {full_url}")
# #             yield scrapy.Request(url=full_url, callback=self.parse_category)

# #     def parse_category(self, response):
# #         # Using requests to fetch the category page content
# #         page = requests.get(response.url)
# #         response = HtmlResponse(url=page.url, body=page.text, encoding='utf-8')
        
# #         # Extract product URLs
# #         product_urls = response.css('a.product_link::attr(href)').getall()
# #         if not product_urls:
# #             self.logger.error(f"No products found in category: {response.url}")
        
# #         for product_url in product_urls:
# #             full_product_url = response.urljoin(product_url.strip())
# #             self.logger.info(f"Following product URL: {full_product_url}")
# #             yield scrapy.Request(url=full_product_url, callback=self.parse_product)

# #         # Follow pagination links if available
# #         next_page = response.css('a.pagination__next::attr(href)').get()
# #         if next_page:
# #             yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse_category)

# #     def parse_product(self, response):
# #         # Using requests to fetch product details
# #         page = requests.get(response.url)
# #         response = HtmlResponse(url=page.url, body=page.text, encoding='utf-8')
# #         soup = BeautifulSoup(response.text, 'html.parser')
# #         # Safely extract product details based on provided HTML structure
# #         title = response.css('h1.product-title::text').get()
# #         price = soup.find('h2', {'id': 'variant-price'})
        
# #         # Extracting MRP
# #         mrp =  soup.find('span', {'id': 'variant-compare-at-price'})
       
# #         item = {
# #             "category": response.css('nav.breadcrumb a::text').getall()[-1] if response.css('nav.breadcrumb a::text').getall() else "Unknown",
# #             "url": response.url,
# #             "title": title.strip() if title else "No Title Found",
# #             "price": price.text.strip(),
# #             "MRP": mrp.text.strip(),
# #             "last_7_day_sale": response.css('div.product_bought_count span::text').re_first(r'\d+') or "No Sale Data",
# #             "available_skus": self.parse_skus(response),
# #             "fit": response.css('strong:contains("Fit") + span::text').get(),
# #             "fabric": response.css('strong:contains("Material") + span::text').get(),
# #             "neck": response.css('strong:contains("Neck") + span::text').get(),
# #             "sleeve": response.css('strong:contains("Sleeves") + span::text').get(),
# #             "pattern": response.css('strong:contains("Pattern") + span::text').get(),
# #             "length": response.css('strong:contains("Length") + span::text').get(),
# #             "description": response.css('div.product-description__content p::text').getall(),
# #         }

# #         if not item['title']:
# #             self.logger.error(f"Failed to scrape product details from: {response.url}")
# #         else:
# #             self.logger.info(f"Scraped product: {item['title']}")
# #         yield item

# #     def parse_skus(self, response):
# #         skus = []
# #         for sku in response.css('select.option-select option'):
# #             variant = sku.css('option::attr(data-variant)').get()
# #             if variant:
# #                 color, size = variant.split('-')[:2]
# #                 skus.append({
# #                     "color": color,
# #                     "size": size
# #                 })
# #         return skus

# import scrapy
# from scrapy.http import HtmlResponse
# import requests
# from bs4 import BeautifulSoup

# class NoberoSpider(scrapy.Spider):
#     name = "nobero"
#     start_urls = ['https://nobero.com/pages/men']

#     def parse(self, response):
#         # Using requests to fetch the content
#         page = requests.get(self.start_urls[0])
        
#         # Creating a Scrapy response object from requests content
#         response = HtmlResponse(url=page.url, body=page.text, encoding='utf-8')
        
#         # Extract category URLs
#         categories = response.css('div.custom-page-season-grid-item a::attr(href)').getall()
#         if not categories:
#             self.logger.error("No categories found on the page!")
        
#         for category in categories:
#             full_url = response.urljoin(category.strip())
#             self.logger.info(f"Following category URL: {full_url}")
#             yield scrapy.Request(url=full_url, callback=self.parse_category)

#     def parse_category(self, response):
#         # Using requests to fetch the category page content
#         page = requests.get(response.url)
#         response = HtmlResponse(url=page.url, body=page.text, encoding='utf-8')
        
#         # Extract product URLs
#         product_urls = response.css('a.product_link::attr(href)').getall()
#         if not product_urls:
#             self.logger.error(f"No products found in category: {response.url}")
        
#         for product_url in product_urls:
#             full_product_url = response.urljoin(product_url.strip())
#             self.logger.info(f"Following product URL: {full_product_url}")
#             yield scrapy.Request(url=full_product_url, callback=self.parse_product)

#         # Follow pagination links if available
#         next_page = response.css('a.pagination__next::attr(href)').get()
#         if next_page:
#             yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse_category)

#     def parse_product(self, response):
#         # Using requests to fetch product details
#         page = requests.get(response.url)
#         response = HtmlResponse(url=page.url, body=page.text, encoding='utf-8')
#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Extracting the product details
#         title = soup.find('h1', class_='product-title').text.strip() if soup.find('h1', class_='product-title') else "No Title Found"
#         price = soup.find('h2', {'id': 'variant-price'}).text.strip() if soup.find('h2', {'id': 'variant-price'}) else None
#         mrp = soup.find('span', {'id': 'variant-compare-at-price'}).text.strip() if soup.find('span', {'id': 'variant-compare-at-price'}) else None
       
#         # Extracting additional details (length, pattern, and description)
#         product_info = soup.find_all('div', class_='product-metafields-values')

#         fit = None
#         fabric = None
#         neck = None
#         sleeve = None
#         pattern = None
#         length = None

#         for info in product_info:
#             label = info.find('h4').text.strip().lower()
#             value = info.find('p').text.strip()

#             if 'fit' in label:
#                 fit = value
#             elif 'fabric' in label:
#                 fabric = value
#             elif 'neck' in label:
#                 neck = value
#             elif 'sleeve' in label:
#                 sleeve = value
#             elif 'pattern' in label:
#                 pattern = value
#             elif 'length' in label:
#                 length = value

#         description_tag = soup.find('div', {'id': 'description_content'})
#         description = description_tag.get_text(separator="\n").strip() if description_tag else "No Description Available"

#         item = {
#             "category": response.css('nav.breadcrumb a::text').getall()[-1] if response.css('nav.breadcrumb a::text').getall() else "Unknown",
#             "url": response.url,
#             "title": title,
#             "price": price,
#             "MRP": mrp,
#              "last_7_day_sale": response.css('div.product_bought_count span::text').re_first(r'\d+') or "No Sale Data",
#             "available_skus": self.parse_skus(response),
#             "fit": fit,
#             "fabric": fabric,
#             "neck": neck,
#             "sleeve": sleeve,
#             "length": length,
#             "pattern": pattern,
#             "description": description,
#         }

#         if not item['title']:
#             self.logger.error(f"Failed to scrape product details from: {response.url}")
#         else:
#             self.logger.info(f"Scraped product: {item['title']}")
#         yield item

#     def parse_skus(self, soup):
#         skus = []
#         sku_data = {}

#         # Extract color and corresponding sizes
#         for option in soup.select('select.option-select option'):
#             variant = option['data-variant'].split('-')
#             color = variant[0]
#             size = variant[1]

#             if color not in sku_data:
#                 sku_data[color] = []

#             sku_data[color].append(size)

#         # Format the data into the required structure
#         for color, sizes in sku_data.items():
#             skus.append({
#                 "color": color,
#                 "size": sizes
#             })

#         return skus
import scrapy
from scrapy.http import HtmlResponse
import requests
from bs4 import BeautifulSoup

class NoberoSpider(scrapy.Spider):
    name = "nobero"
    start_urls = ['https://nobero.com/pages/men']

    def parse(self, response):
        # Using requests to fetch the content
        page = requests.get(self.start_urls[0])
        
        # Creating a Scrapy response object from requests content
        response = HtmlResponse(url=page.url, body=page.text, encoding='utf-8')
        
        # Extract category URLs
        categories = response.css('div.custom-page-season-grid-item a::attr(href)').getall()
        if not categories:
            self.logger.error("No categories found on the page!")
        
        for category in categories:
            full_url = response.urljoin(category.strip())
            self.logger.info(f"Following category URL: {full_url}")
            yield scrapy.Request(url=full_url, callback=self.parse_category)

    def parse_category(self, response):
        # Using requests to fetch the category page content
        page = requests.get(response.url)
        response = HtmlResponse(url=page.url, body=page.text, encoding='utf-8')
        
        # Extract product URLs
        product_urls = response.css('a.product_link::attr(href)').getall()
        if not product_urls:
            self.logger.error(f"No products found in category: {response.url}")
        
        for product_url in product_urls:
            full_product_url = response.urljoin(product_url.strip())
            self.logger.info(f"Following product URL: {full_product_url}")
            yield scrapy.Request(url=full_product_url, callback=self.parse_product)

        # Follow pagination links if available
        next_page = response.css('a.pagination__next::attr(href)').get()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse_category)

    def parse_product(self, response):
        page = requests.get(response.url)
        response = HtmlResponse(url=page.url, body=page.text, encoding='utf-8')
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting the product details
        title = soup.find('h1', class_='product-title').text.strip() if soup.find('h1', class_='product-title') else "No Title Found"
        price = soup.find('h2', {'id': 'variant-price'}).text.strip() if soup.find('h2', {'id': 'variant-price'}) else None
        mrp = soup.find('span', {'id': 'variant-compare-at-price'}).text.strip() if soup.find('span', {'id': 'variant-compare-at-price'}) else None

        # Extract SKUs
        available_skus = self.parse_skus(soup)
        product_info = soup.find_all('div', class_='product-metafields-values')

        fit = None
        fabric = None
        neck = None
        sleeve = None
        pattern = None
        length = None

        for info in product_info:
            label = info.find('h4').text.strip().lower()
            value = info.find('p').text.strip()

            if 'fit' in label:
                fit = value
            elif 'fabric' in label:
                fabric = value
            elif 'neck' in label:
                neck = value
            elif 'sleeve' in label:
                sleeve = value
            elif 'pattern' in label:
                pattern = value
            elif 'length' in label:
                length = value

        description_tag = soup.find('div', {'id': 'description_content'})
        description = description_tag.get_text(separator="\n").strip() if description_tag else "No Description Available"

        item = {
            "category": response.css('nav.breadcrumb a::text').getall()[-1] if response.css('nav.breadcrumb a::text').getall() else "Unknown",
            "url": response.url,
            "title": title,
            "price": price,
            "MRP": mrp,
            "last_7_day_sale": response.css('div.product_bought_count span::text').re_first(r'\d+') or "No Sale Data",
            "available_skus": available_skus,
            "fit": fit,
            "fabric": fabric,
            "neck": neck,
            "sleeve": sleeve,
            "length": length,
            "pattern": pattern,
            "description": description,
        }

        yield item

    def parse_skus(self, soup):
        skus = []
        sku_data = {}

        # Extract color and corresponding sizes
        for option in soup.select('select.option-select option'):
            variant = option['data-variant'].split('-')
            color = variant[0]
            size = variant[1]

            if color not in sku_data:
                sku_data[color] = []

            sku_data[color].append(size)

        # Format the data into the required structure
        for color, sizes in sku_data.items():
            skus.append({
                "color": color,
                "size": sizes
            })

        return skus
