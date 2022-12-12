from django.urls import path 
from .views import indexPageView, homeListingsView, addListingView, deleteListingView, editListingView, editListing

urlpatterns = [
    path('', indexPageView, name='index'),
    path('listings/', homeListingsView, name = 'listings'),
    path('addlisting/', addListingView, name = 'addListing'),
    path('deletelisting/<int:house_id>/', deleteListingView, name = 'deleteListing'),
    path('editlisting/<int:house_id>/', editListingView, name = 'editListingView'),   
    path('editlisting/', editListing, name = 'editListing'),   

]
