# store/urls.py

from django.urls import path
from . import views # assuming your views are in store/views.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, pampers_list


urlpatterns = [
    path('', views.home, name='home'),
    path('pampers/', views.pampers_list, name='pampers_list'),
    path('boys/', views.boys_list, name='boys_list'),
    path('girls/', views.girls_list, name='girls_list'),
    path('soaps/', views.soaps_list, name='soaps_list'),
    path('stroller/', views.stroller_list, name='stroller_list'),
    path('bottle/', views.bottle_list, name='bottle_list'),
    path('all-products/', views.all_products, name='all_products'),
    path('offers/', views.offers_list, name='offers_list'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('contact/', views.contact_view, name='contact'),
    path('logout/', views.logout_view, name='logout'),
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/', views.update_cart_item, name='update_cart_item'),
    path('cart/remove/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('order-complete/', views.order_complete, name='order_complete'),
    path('', views.home, name='home'),

    path('search/', views.search, name='search'),
    path('apply-coupon/', views.apply_coupon, name='apply_coupon'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('category/<str:category_name>/', views.category_products, name='category_products'),


]


