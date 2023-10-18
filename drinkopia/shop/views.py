from django.shortcuts import render


#Алкогольные напитки
def index(request):
    return render(request, 'shop/index.html')
def vodka(request):
    return render(request, 'shop/vodka.html')
def vino(request):
    return render(request, 'shop/vino.html')
def pivo (request):
    return render(request, 'shop/pivo.html')
def koniak (request):
    return render(request, 'shop/koniak.html')
def rom (request):
    return render(request, 'shop/rom.html')
def tekila (request):
    return render(request, 'shop/tekila.html')
def liker (request):
    return render(request, 'shop/liker.html')
def shamp (request):
    return render(request, 'shop/shamp.html')
#Безалкогольные напитки
def bezal(request):
    return render(request, 'shop/bezal.html')
def bezalGaz(request):
    return render(request, 'shop/bezalGaz.html')
def bezalEnerg(request):
    return render(request, 'shop/bezalEnerg.html')
def bezalKvas(request):
    return render(request, 'shop/bezalKvas.html')
def bezalTea(request):
    return render(request, 'shop/bezalTea.html')
#Закуски
def snake(request):
    return render(request, 'shop/snake.html')
def snakeChip(request):
    return render(request, 'shop/snakeChip.html')
def snakeMore(request):
    return render(request, 'shop/snakeMore.html')
def snakeOresh(request):
    return render(request, 'shop/snakeOresh.html')
