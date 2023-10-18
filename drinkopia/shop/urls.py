from django.urls import path
from . import views

urlpatterns = [
    #Алкогольные напитки
    path('', views.index, name='alkogol'),
    path('vodka',views.vodka, name='vodka'),
    path('vino',views.vino, name='vino'),
    path('pivo',views.pivo, name='pivo'),
    path('koniak',views.koniak, name='koniak'),
    path('rom',views.rom, name='rom'),
    path('tekila',views.tekila, name='tekila'),
    path('liker',views.liker, name='liker'),
    path('shamp',views.shamp, name='shamp'),
    #Безалкогольные напитки
    path('bezal', views.bezal, name='bezal'),
    path('bezalGaz', views.bezalGaz, name='bezalGaz'),
    path('bezalEnerg', views.bezalEnerg, name='bezalEnerg'),
    path('bezalKvas', views.bezalKvas, name='bezalKvas'),
    path('bezalTea', views.bezalTea, name='bezalTea'),
    #Закуски
    path('snake', views.snake, name='snake'),
    path('snakeChip', views.snakeChip, name='snakeChip'),
    path('snakeMore', views.snakeMore, name='snakeMore'),
    path('snakeOresh', views.snakeOresh, name='snakeOresh')
]