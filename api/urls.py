from django.urls import path
from .views import card_detail, cards_list, CardList

urlpatterns = [
    path('cards/<int:pk>/', card_detail),
    path('cards/create/', cards_list),
    path('cards/', CardList.as_view()),
]

