from rest_framework import serializers

from .models import Product, Company, Category


class CompanyListSerializer(serializers.ModelSerializer):
    """Список компаний"""

    class Meta:
        model = Company
        fields = ('title_com', 'description_com')


class CompanyDetailSerializer(serializers.ModelSerializer):
    """Отдельная компания"""

    class Meta:
        model = Company
        fields = "__all__"


class CategoryListSerializer(serializers.ModelSerializer):
    """Список категорий"""

    class Meta:
        model = Category
        fields = "__all__"


class CategoryDetailSerializer(serializers.ModelSerializer):
    """Отдельная категория"""

    class Meta:
        model = Category
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):
    """Список продуктов"""
    # Переопределяем поля
    company = serializers.SlugRelatedField(slug_field='title_com', read_only=True)
    category = serializers.SlugRelatedField(slug_field='title_cat', read_only=True, many=True)

    class Meta:
        model = Product
        fields = ("title", "category", "company")


class ProductDetailSerializer(serializers.ModelSerializer):
    """Отдельный продукт"""

    # Переопределяем поля своими сериализаторами, чтобы выводить поную информацию
    company = CompanyDetailSerializer(read_only=True)
    category = CategoryDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ("title", "description_prod", "category", "company", "is_active")
        # exclude = ('is_active', )

################
class CompanyActionSerializer(serializers.ModelSerializer):
    """Добавление, изменение, удаление компании"""

    class Meta:
        model = Company
        fields = "__all__"


class ProductActionSerializer(serializers.ModelSerializer):
    """Добавление, изменение, удаление продукта"""

    class Meta:
        model = Product
        fields = "__all__"


class CategoryActionSerializer(serializers.ModelSerializer):
    """ДДобавление, изменение, удаление категории"""

    class Meta:
        model = Category
        fields = "__all__"


