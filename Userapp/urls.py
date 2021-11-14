from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('showcakes/<id>',views.showcakes),
    path('viewdetails/<id>',views.viewdetails),
    path('signup',views.signup),
    path('login',views.login),
    path('logout',views.logout),
    path('addtocart',views.addtocart),
    path('showcartitems',views.showcartitems),
    path('removefromcart',views.removefromcart),
    path('makepayment',views.makepayment),
    path('ev',views.ev),
    ]