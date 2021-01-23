from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name='shop'),
    path("factorytour/", views.factorytour, name='shop'),
    path("contact/", views.contact, name='shop'),
   path("about/", views.about, name='shop'),
   path("faq/", views.faq, name='shop'),
    path("tour/", views.tour, name='shop'),
]