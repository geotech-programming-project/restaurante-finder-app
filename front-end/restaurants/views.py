from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Restaurant
from .choices import rating_choices, university_choices

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    
    paginator = Paginator (restaurants,3)
    page = request.GET.get('page')
    paged_restaurants = paginator.get_page(page)
    context = {
        'restaurants':paged_restaurants
    }
    return render(request,"restaurants/restaurants.html",context)

def restaurant (request,restaurant_id):
    restaurant = get_object_or_404 (Restaurant,pk=restaurant_id)
    
    context = {
        'restaurant':restaurant
    }
    return render(request,"restaurants/restaurant.html", context)
    
def search(request):
    queryset_restaurant = Restaurant.objects.order_by("-rating")
    
    # Keywords
    if "keywords" in request.GET:
        keywords = request.GET["keywords"]
        if keywords:
            queryset_restaurant = queryset_restaurant.filter(type_food__icontains=keywords) # filter for similar match
            
    if "university" in request.GET:
        university = request.GET["university"]
        if university:
            queryset_restaurant = queryset_restaurant.filter(university__iexact=university) #filter for exact match
    
    if "rating" in request.GET:
        rating = request.GET["rating"]
        if rating:
            queryset_restaurant = queryset_restaurant.filter(rating__lte=rating) # lte stands for less than
            
    context = {
        "restaurants": queryset_restaurant, 
        "rating_choices" : rating_choices,
        "university_choices": university_choices,
        "values": request.GET
    }
    return render(request,"restaurants/search.html", context)