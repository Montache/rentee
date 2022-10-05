from django.urls import path
from . import views

# from Home.views import Product_info

urlpatterns=[
    path('', views.Homepage, name='home'),
    path('AddListing', views.AddListing, name='addlisting'),
    path('ViewListing/<listing_id>', views.ViewListing, name="listing"),
]
