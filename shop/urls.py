from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('shop/', views.shop, name='shop'),
    path('shop/<int:category_id>/', views.by_category, name='by_category'),
    path('shop/<int:category_id>/<int:subcategory_id>/', views.by_subcategory, name='by_subcategory'),
    path('pagination/', views.pagination_pro, name='pagination_p'),
    path('shop/<int:category_id>/<int:subcategory_id>/<int:product_id>/', views.product_page, name='product_page')
]