from django.urls import path 
from . import views

# one urlpattern per line
urlpatterns = [
    path('populate', views.populate, name='populate'),
    path('cards', views.cards, name='allCards'),
    path('cards/<int:card_id>', views.display_card, name='card'),
    path('profile/<int:user_id>', views.user_profile, name='profile'),
    path('card/<int:card_id>/buy/<int:user_id>', views.buy_card, name='buy_card'),
    path('card/<int:card_id>/sell/<int:user_id>', views.sell_card, name='sell_card'),
]