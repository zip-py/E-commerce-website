from . import views
from django.urls import path, include
# from django.contrib.auth.views import LoginView, LogoutView
# from register import views as v

urlpatterns = [
    path("", views.index, name='ShopHome'),
    path("about/", views.about, name='AboutUs'),
    path("contact/", views.contact, name='ContactUs'),
    path("tracker/", views.tracker, name='TrackingStatus'),
    path("search/", views.search, name='Search'),
    path("products/<int:proid>", views.productView, name='ProductView'),
    path("checkout/", views.checkout, name='Checkout'),
    path("paymentstatus/", views.handlerequest, name='HandleRequest'),
    path("menfashion/", views.men, name='MenFashion'),
    path("womenfashion/", views.women, name='MenFashion'),
]
