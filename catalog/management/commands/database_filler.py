from django.core.management import BaseCommand
import json

from django.db import connection

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('catalog/JSON_Exports/category_data.json', 'r', encoding='UTF-8') as category_file:
            data = json.load(category_file)
        return data
    # Здесь мы получаем данные из фикстурв с категориями

    @staticmethod
    def json_read_products():
        with open('catalog/JSON_Exports/product_data.json', 'r', encoding='UTF-8') as product_file:
            data = json.load(product_file)
        return data
    # Здесь мы получаем данные из фикстурв с продуктами

    def handle(self, *args, **options):

        with connection.cursor() as cur:
            cur.execute(f'TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE;')

        Category.objects.all().delete()
        Product.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(name=category['fields']['name'], description=category['fields']['description'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(name=product['fields']['name'],
                        description=product['fields']['description'],
                        # получаем категорию из базы данных для корректной связки объектов
                        category=Category.objects.get(pk=product['fields']['category']),
                        price_to_buy=product['fields']['price_to_buy'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)