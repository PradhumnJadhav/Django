from django.urls import path
from . import views

urlpatterns = [
     path('<int:id>/details/', views.details, name='details'),
     path('users/', views.users, name='Users'),
    path('free/', views.freeItem, name='freeItem'),
    path('', views.homePage, name='home'),
     path('register/', views.register, name='register'),
     path('login/', views.login_page, name='login'),
      path('logout/', views.logout_page, name='logout'),
       path('account/', views.account_details, name='account'),
       path('account/cart/', views.cart, name='cart'),
        path('account/sell_products/', views.sell, name='sell'),
          path('addToCart/<int:id>/', views.add_to_cart, name='addToCart'),
          path('removeFromCart/<int:id>/', views.rem_from_cart, name='addToCart'),
      
      
]

# pass 123 pradhumn pradhumnjadav@gmail.com

# host pass Pradhumn1234@@@@