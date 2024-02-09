from django.urls import path
from . import views

urlpatterns = [
    path ("",views.index, name="restaurants"),
    path ("<int:restaurant_id>",views.restaurant,name="restaurant"),
    path ("search",views.search,name="search"),
]