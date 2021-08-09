from django.urls import path
from .views import card_detail, cards_list

urlpatterns = [
    path('cards/<int:pk>/', card_detail),
    path('cards/', cards_list),
]

