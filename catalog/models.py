from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=250, verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}: ({self.description})'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):

    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=250, verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='product_images/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price_to_buy = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата последнего изменения', auto_now_add=True)

    def __str__(self):
        return f'{self.name}: ({self.description}; {self.created_at}; {self.updated_at})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
