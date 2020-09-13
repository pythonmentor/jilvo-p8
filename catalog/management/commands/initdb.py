import requests

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import DatabaseError, IntegrityError
from catalog.models import Category,Product

class Command(BaseCommand):
    help = 'Initializes the database'
    # CATEGORIES = ['yaourts-au-caramel']
    CATEGORIES = ['Viandes', 'Poissons', 'Epicerie', 'Chocolats', 'Pates-a-tartiner', 'Biscuits',  'Vins', 'Boissons-gazeuses', 'Yaourts', 'Pains', 'Glace', 'Fromages-de-france', 'Pizzas', 'Snacks sucrés']

    def create_db(self):

        for category in self.CATEGORIES:
            new_category = Category.objects.create(name=category)
				
            params = {
					'action': 'process',
	            	'json': 1,
				    'page_size': 500,
				    'page': 1,
				    'tagtype_0': 'categories',
			        'tag_contains_0': 'contains',
			        'tag_0': category,
				}

            response = requests.get('https://fr.openfoodfacts.org/cgi/search.pl',
				            params=params)

            data = response.json()
            products = data['products']
            a = 0
            b = 0
            for product in products:
                try:
                    name = product['product_name']
                    nutrition_grade = product['nutrition_grades']
                    url = product['url']
                    brand = product['brands']
                    picture = product['image_url']
                    # nutrition_image = product["image_nutrition_small_url"]
                    nutriments = product['nutriments']
                    # print(a)
                    a+=1 
                    for nutriment in nutriments:
                    # print(b)
                        calories = nutriments["energy-kcal"]
                        lipids = nutriments["fat"]
                        sugar = nutriments["sugars"]
                        proteins = nutriments["proteins_value"]
                        salts = nutriments["salt"]
                        # b+=1
                        # pass

                    # d1 = Product.objects.create(name=name, nutrition_grade=nutrition_grade,image=picture,brand=brand,url=url)
                    d1 = Product.objects.create(name=name, nutrition_grade=nutrition_grade,image=picture,brand=brand,calories=calories,
                    lipids=lipids,sugars=sugar,proteins=proteins,salts=salts,url=url)
                    print(d1)
                    d1.save()

                except Exception as e :
                    print(e)
                    # pass


    def handle(self, *args, **options):
        self.create_db()
