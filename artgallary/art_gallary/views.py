

from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from decimal import Decimal
from .models import artist_sell, Order, Cart, CartItem, Profile, Category, artworks, compitition, Buy, contact_us


# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

class createprofile(CreateView):
    model = Profile
    fields = ['user','category','name','email' ,'mobile_number','bio' ,'image_url','i_am_not_robot']
    success_url = reverse_lazy('art-list')
    template_name = 'profile.html'


class Profileview(LoginRequiredMixin, ListView):
    model = Profile
    context_object_name = 'profiles'
    template_name = 'profileview.html'
    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset().filter(user=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['artist'] = artist_sell.objects.filter(user=user)
        return context

class profile_update(LoginRequiredMixin,UpdateView):
    model = Profile
    fields = ['name','email' ,'mobile_number','bio' ,'image_url']
    success_url = reverse_lazy('profile-view')
    template_name = 'profile.html'


class artlist(ListView):
    model = artist_sell
    context_object_name = 'artist'
    template_name = 'artlist.html'

class artistpaintingview(LoginRequiredMixin, ListView):
    model = artist_sell
    context_object_name = 'artist'
    template_name = 'artistpaintingview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artist'] = context['artist'].filter(user=self.request.user)
        context['count'] = context['artist'].filter(i_am_not_robot=True).count()
        return context
class artcreate(CreateView):
    model = artist_sell
    fields = ['user','Painting_name','mediam','size','description','artcode','price','image_url','art_available','i_am_not_robot']
    success_url = reverse_lazy('art-list')
    template_name = 'artcreate.html'



    def form_valid(self, form):
        form.instance.image_url = self.request.FILES['image_url']
        return super().form_valid(form)


class artview(DetailView):
    model = artist_sell
    context_object_name = 'artist'
    template_name = 'artview.html'

class artupdate(LoginRequiredMixin, UpdateView):
    model = artist_sell
    fields = ['Painting_name', 'mediam', 'size', 'description', 'artcode', 'price', 'image_url', 'art_available']
    template_name = 'artcreate.html'

    def get_success_url(self):
        return reverse_lazy('art-view', kwargs={'pk': self.object.pk})

class artDelete(LoginRequiredMixin,DeleteView):
    model = artist_sell
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('art-list')
    template_name = 'artdelete.html'

class artCheckoutView(DetailView):
    model = artist_sell
    template_name = 'checkout.html'
    context_object_name = 'painting'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data required for the template
        return context





def PaymentComplete(request, pk):
    product = artist_sell.object.get(id=pk)
    Order.objects.create(
        product=product
    )
    return JsonResponse('payment completed', self=False)

class SearchResultsView(ListView):
    models = artist_sell
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('Q')
        return artist_sell.objects.filter(
            Q(Painting_name=query)
        )

@login_required
def cart(request):
    cart_qs = Cart.objects.filter(user=request.user)
    if cart_qs.exists():
        cart_obj = cart_qs.first()
        cart_items = CartItem.objects.filter(cart=cart_obj)
    else:
        cart_obj = None
        cart_items = []

    context = {
        'cart': cart_obj,
        'cart_items': cart_items
    }
    return render(request, 'mycart.html', context)




@login_required
def add_to_cart(request, art_id):
    painting = get_object_or_404(artist_sell, id=art_id)
    cart_qs = Cart.objects.filter(user=request.user)
    if cart_qs.exists():
        cart_obj = cart_qs.first()
    else:
        cart_obj = Cart.objects.create(user=request.user, total_price=Decimal('0.00'))
    cart_item, created = CartItem.objects.get_or_create(painting_name=painting, cart=cart_obj)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    cart_obj.total_price += Decimal(str(painting.price))
    cart_obj.save()
    return redirect('mycart')

@login_required()
def remove_from_cart(request,art_id):
    painting  = get_object_or_404(artist_sell,id =art_id)
    cart_qs = Cart.objects.filter(user=request.user)
    if cart_qs.exists():
        cart_obj = cart_qs.first()
        cart_item_qs = CartItem.objects.filter(painting_name=painting,cart=cart_obj)
        if cart_item_qs.exists():
            cart_item = cart_item_qs.first()
            if cart_item.quantity >1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
            cart_obj.total_price -= Decimal(str(painting.price))
            cart_obj.save()
    return redirect('mycart')

class copititionlist(ListView):
    model = artworks
    context_object_name = 'compitition'
    template_name = 'compitition.html'

class artworkDetailView(DetailView):
    model = artworks
    template_name = 'artwork.html'

class PractiseView(CreateView):
    model = compitition
    fields = ['name', 'email', 'feedback', 'image_url']
    success_url = reverse_lazy('art-list')
    template_name = 'practise.html'

def drowing(request):
    return render(request, 'drowing.html')



def artist_profile(request, user):
    profile = get_object_or_404(Profile, user__username=user)
    art = artist_sell.objects.filter(user__username=user)

    context = {
        'profile': profile,
        'art': art
    }
    return render(request, 'artist_profile.html', context)

def buy(request, pk, user):
    painting = get_object_or_404(artist_sell, id=pk)
    user_dtls = Profile.objects.filter(user__username=user)

    context = {
        'painting': painting,
        'user_dtls': user_dtls,
    }
    return render(request, 'buy.html', context)


from django.views.generic.edit import CreateView
from .models import Buy

class BuyLocation(CreateView):
    model = Buy
    context_object_name = 'painting'
    fields = ['painting', 'user', 'name', 'email', 'phone_no', 'address_1', 'address_2', 'address_3', 'pin', 'nearest_city', 'online_payment', 'cash_on_delivery']
    template_name = 'location.html'

    def form_valid(self, form):
        painting = form.cleaned_data['painting']
        online_payment = form.cleaned_data['online_payment']
        cash_on_delivery = form.cleaned_data['cash_on_delivery']
        if online_payment:
            return redirect('art-checkout', pk=painting.id)
        elif cash_on_delivery:
            return redirect('home')
        else:
            return super().form_valid(form)


class contact(CreateView):
    model = contact_us
    fields = ['name','email','message']
    success_url = reverse_lazy('art-list')
    template_name = 'contact.html'

def review(request):
    return render(request, 'review.html')

