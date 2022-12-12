from django.urls import path 
from .views import indexPageView, homeListingsView, addListingView, deleteListingView, editListingView, addListing

urlpatterns = [
    path('', indexPageView, name='index'),
    path('listings/', homeListingsView, name = 'listings'),
    path('addlisting/', addListingView, name = 'addListing'),
    path('editlisting/', addListing, name = 'addNewListing'),   
    path('deletelisting/', deleteListingView, name = 'deleteListing'),
    path('editlisting/', editListingView, name = 'editListing'),   

]
