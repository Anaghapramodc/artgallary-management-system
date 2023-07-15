from django.contrib import admin
from django.urls import path, include

from .views import artcreate, artlist, artview, artCheckoutView, PaymentComplete, SearchResultsView, cart, \
    createprofile, Profileview, artistpaintingview, artupdate, profile_update, add_to_cart, remove_from_cart, \
    copititionlist, artworkDetailView, PractiseView, artDelete, BuyLocation, contact
from .import views



urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('art-list', artlist.as_view(), name='art-list'),
    path('art_create/', artcreate.as_view(), name='art-create'),
    path('art_view/<int:pk>/', artview.as_view(), name='art-view'),
    path('art_update/<int:pk>/', artupdate.as_view(), name='art-update'),
    path('delete/<int:pk>/', artDelete.as_view(), name='art-delete'),
    path('art-checkout/<int:pk>/', artCheckoutView.as_view(), name='art-checkout'),
    path('complete/', PaymentComplete, name='complete'),
    path('cart/', cart, name='mycart'),
    path('cart/add/<int:art_id>/', add_to_cart, name="add_to_cart"),
    path('cart/remove/<int:art_id>/', remove_from_cart, name="remove_from_cart"),
    path('profile/', createprofile.as_view(), name='profile'),
    path('profile_view/', Profileview.as_view(), name='profile-view'),
    path('profile_update/<int:pk>/', profile_update.as_view(), name='profile-update'),
    path('artist_painting_view',artistpaintingview.as_view(), name='artist-painting--list'),
    path('compitition', copititionlist.as_view(), name='compitition-list'),
    path('artwork/<int:pk>/', artworkDetailView.as_view(), name='artwork-teams'),
    path('practise/', PractiseView.as_view(), name='practise'),
    path('drowing', views.drowing, name='drowing'),
    path('artists/<str:user>/', views.artist_profile, name='artist_profile'),
    path('artists_buy/<str:user>/<int:pk>/', views.buy, name='buy'),
    path('location/<int:pk>/', BuyLocation.as_view(), name='buy-location'),
    path('contact_us/', contact.as_view(), name='contact-us'),
    path('review', views.review, name='review'),

]


