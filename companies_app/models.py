from django.db import models

class Category(models.Model):
    """Категории"""
    title_cat = models.CharField("Название", max_length=100)

    def __str__(self):
        return self.title_cat

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Company(models.Model):
    """Компании"""
    title_com = models.CharField("Название", max_length=100)#, unique=True)
    description_com = models.TextField("Описание компании")
    company_is_active = models.BooleanField("Статус компании", default=True)

    def __str__(self):
        return self.title_com

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


class Product(models.Model):
    """Продукты"""
    title = models.CharField("Название", max_length=150)
    description_prod = models.TextField("Описание товара")
    category = models.ManyToManyField(Category, verbose_name="Категории", related_name="product_category")
    company = models.ForeignKey(Company, verbose_name="Компании", on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField("Активность", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
