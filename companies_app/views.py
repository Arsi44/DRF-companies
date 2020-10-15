# Ссылка на документацию
# https://www.django-rest-framework.org/tutorial/3-class-based-views/

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Product, Company, Category
from .serializers import (ProductListSerializer,
                          ProductDetailSerializer,
                          CompanyListSerializer,
                          CategoryListSerializer,
                          CompanyDetailSerializer,
                          CategoryDetailSerializer,
                          CompanyActionSerializer,
                          ProductActionSerializer,
                          CategoryActionSerializer)

from django_filters.rest_framework import DjangoFilterBackend
from .company_filters import ProductFilter

from rest_framework import generics, permissions


class ProductListView(generics.ListAPIView):
    """Вывод списка продуктов"""
    serializer_class = ProductListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        products = Product.objects.filter(is_active=True)
        return products



class ProductDetailView(generics.RetrieveAPIView):
    """Вывод отдельного продукта"""

    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.AllowAny]


class CompanyListView(generics.ListAPIView):
    """Вывод списка компаний"""
    serializer_class = CompanyListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        companies = Company.objects.filter(company_is_active=True)
        return companies



class CompanyDetailView(generics.RetrieveAPIView):
    """Вывод отдельной компании"""
    queryset = Product.objects.all()
    serializer_class = CompanyDetailSerializer
    permission_classes = [permissions.AllowAny]


class CategoryListView(generics.ListAPIView):
    """Вывод списка категорий"""
    serializer_class = CategoryListSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        cats = Category.objects.all()
        return cats


class CategoryDetailView(generics.RetrieveAPIView):
    """Вывод отдельной категории"""
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [permissions.AllowAny]


# Добавление Компаний, Продуктов и Категорий
#############################################
class CompanyCreateView(APIView):
    """Добавление компании"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        company = CompanyActionSerializer(data=request.data)
        if company.is_valid():
            company.save()
        return Response(status=201)


class ProductCreateView(APIView):
    """Добавление продукта"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        product = ProductActionSerializer(data=request.data)
        if product.is_valid():
            product.save()
        return Response(status=201)


class CategoryCreateView(APIView):
    """Добавление категории"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        category = CategoryActionSerializer(data=request.data)
        if category.is_valid():
            category.save()
        return Response(status=201)


# Обновление Компаний, Продуктов и Категорий
#############################################
class CompanyUpdateView(APIView):
    """Обновление компании"""
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Company

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = CompanyActionSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductUpdateView(APIView):
    """Обновление продукта"""
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Product

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = ProductActionSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryUpdateView(APIView):
    """Обновление категории"""
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Category

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = CategoryActionSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Удаление Компаний, Продуктов и Категорий
#############################################

class CompanyDeleteView(APIView):
    """Удаление компании"""
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Company

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductDeleteView(APIView):
    """Удаление продукта"""
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Product

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryDeleteView(APIView):
    """Удаление категории"""
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Category

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)