from django.urls import path
from .views import current_user, get_money_data
urlpatterns = [
    path('current_user/', current_user),
    path('get_money_data/', get_money_data),
]