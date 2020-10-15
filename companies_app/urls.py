from django.urls import path

from . import views

urlpatterns = [
    path('product/', views.ProductListView.as_view()),
    path('product/<int:pk>', views.ProductDetailView.as_view()),
    path('company/', views.CompanyListView.as_view()),
    path('company/<int:pk>', views.CompanyDetailView.as_view()),
    path('category/', views.CategoryListView.as_view()),
    path('category/<int:pk>', views.CategoryDetailView.as_view()),
    path('create_company/', views.CompanyCreateView.as_view()),
    path('create_product/', views.ProductCreateView.as_view()),
    path('create_category/', views.CategoryCreateView.as_view()),
    path('update_company/<int:pk>', views.CompanyUpdateView.as_view()),
    path('update_product/<int:pk>', views.ProductUpdateView.as_view()),
    path('update_category/<int:pk>', views.CategoryUpdateView.as_view()),
    path('delete_company/<int:pk>', views.CompanyDeleteView.as_view()),
    path('delete_product/<int:pk>', views.ProductDeleteView.as_view()),
    path('delete_category/<int:pk>', views.CategoryDeleteView.as_view()),
]