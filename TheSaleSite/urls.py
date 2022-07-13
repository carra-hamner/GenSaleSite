from django.urls import path

from . import views

app_name = 'TheSaleSite'
urlpatterns = [
    path('', views.index, name='index'),
    path('listing/', views.listing, name='listing'),
    path('signup/', views.signup, name='signup'),
    path('products/', views.products, name='products'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('cart/', views.cart, name='cart'),
    path('signup_or_login_redirect', views.signup_or_login_redirect, name='signup_or_login_redirect')
]
