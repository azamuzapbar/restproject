from django.urls import path

from api.views import RestaurantAPIList

urlpatterns = [
    path('api/v1/restaurantlist', RestaurantAPIList.as_view()),
]