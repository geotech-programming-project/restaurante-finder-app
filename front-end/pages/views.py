from django.shortcuts import render
from django.http import HttpResponse
from restaurants.models import Restaurant
import folium
from restaurants.choices import rating_choices, university_choices

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all().filter(is_published=True)[:3]
    
    context = {
        "restaurants":restaurants,
        "rating_choices" : rating_choices,
        "university_choices": university_choices,
        
    }
    return render(request,"pages/index.html", context)


def about(request):
    return render(request, "pages/about.html")

def map(request):
    restaurants = Restaurant.objects.all()
    
    # create a Foluim map centered on connecticut NOVA IMS
    m_unl = folium.Map(location=[38.732462, -9.159921], zoom_start=13)
    
    # create a Foluim map centered on connecticut Munster
    m_um = folium.Map(location=[51.969412, 7.595780], zoom_start=13)
    
    # create a Foluim map centered on connecticut Jaume I
    m_uji = folium.Map(location=[39.994487, -0.069388], zoom_start=13)
    
    # add a marker to the map for each restaurants in NOVA IMS
    for restaurant in restaurants:
        coordinates = (restaurant.latitude, restaurant.longtitude)
        folium.Marker(coordinates, popup=restaurant.name, color='red').add_to(m_unl)
        
    context = {
        'map_unl':m_unl._repr_html_(),
    }
    return render(request, "pages/map.html",context)

def map_search (request):
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