from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.utils.text import slugify
from decimal import Decimal

SAMPLE_DATA = [
    ("Ноутбуки", [("Acer Aspire 7", "19999.00"), ("ASUS ZenBook 14", "34999.00")]),
    ("Смартфоны", [("Samsung Galaxy S23", "69999.00"), ("Google Pixel 8", "59999.00")]),
    ("Наушники", [("AirPods Pro 2", "24999.00"), ("JBL Tune 760NC", "7999.00")]),
]

class Command(BaseCommand):
    help = "Добавляет тестовые категории и продукты"

    def handle(self, *args, **options):
        created_total = 0
        for cat_name, products in SAMPLE_DATA:
            cat, _ = Category.objects.get_or_create(
                name=cat_name,
                defaults={"slug": slugify(cat_name)}
            )
            for name, price in products:
                _, created = Product.objects.get_or_create(
                    name=name,
                    category=cat,
                    defaults={"slug": slugify(name), "price": Decimal(price), "is_active": True}
                )
                created_total += int(created)
        self.stdout.write(self.style.SUCCESS(f"Добавлено новых продуктов: {created_total}"))
