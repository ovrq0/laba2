from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Films, Category

# Create your views here.
def index(request):
    films = Films.objects.all()
    return render(request, 'index.html', {'films': films})

def create(request):
    create_categories()

    if request.method == 'POST':
        film = Films()
        film.name = request.POST.get('name')
        film.release_date = request.POST.get('release_date')
        film.actors = request.POST.get('actors')
        film.show_date = request.POST.get('show_date')
        film.category_id = request.POST.get('category')
        film.save()
        return HttpResponseRedirect('/')
    
    categories = Category.objects.all()
    return render(request, 'create.html', {'categories': categories})

def edit(request, id):
    try:
        films = Films.objects.get(id=id)

        if request.method == 'POST':
            film.name = request.POST.get('name')
            film.release_date = request.POST.get('release_date')
            film.actors = request.POST.get('actors')
            film.show_date = request.POST.get('show_date')
            film.category_id = request.POST.get('category')
            film.save()
            return HttpResponseRedirect('/')
        else:
            categories = Category.objects.all()
            return render(request, 'edit.html', {'films': films, 'categories': categories})
    except Films.DoesNotExist:
        return HttpResponseNotFond('<h2>Films not found</h2>')

def delete(request, id):
    try:
        film = Films.objects.get(id = id)
        film.delete()
        return HttpResponseRedirect('/')
    except Films.DoesNotExist:
        return HttpResponseNotFond('<h2>Films not found</h2>')

def create_categories():

    if Category.objects.all().count() == 0:
        Category.objects.create(name = 'Дом')
        Category.objects.create(name = 'Земля')
        Category.objects.create(name = 'Воздух')