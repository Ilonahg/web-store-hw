from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = "Загружает тестовые продукты и категории в БД"

    def handle(self, *args, **kwargs):
        self.stdout.write("Удаляем старые данные...")
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write("Создаём новые категории и продукты...")

        cat1 = Category.objects.create(name="Одежда", description="Мужская и женская")
        Product.objects.create(
            name="Футболка",
            description="Белая",
            price=1000,
            category=cat1,
            image="products/shirt.jpg"
        )

        cat2 = Category.objects.create(name="Обувь", description="Кроссовки, туфли")
        Product.objects.create(
            name="Кроссовки",
            description="Спортивные",
            price=3000,
            category=cat2,
            image="products/shoes.jpg"
        )

        self.stdout.write(self.style.SUCCESS("Тестовые данные успешно загружены!"))
