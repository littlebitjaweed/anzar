from django.urls import path
from . import views

app_name = 'pos_app'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add_sale/<int:product_id>/', views.add_sale, name='add_sale'),
    path('sales/', views.sales_list, name='sales_list'),
    path('receipt/<int:sale_id>/', views.receipt, name='receipt'),
        
]
