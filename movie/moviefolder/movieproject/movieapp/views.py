from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie
# Create your views here.
def index(request):
    movie=Movie.objects.all()
    return render(request,'index.html',{'Result':movie})
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':movie})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        about = request.POST.get('about')
        director = request.POST.get('director')
        img = request.FILES['img']
        movie=Movie(name=name,about=about,director=director,img=img)
        movie.save()
    return render(request,'add.html')
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=="POST":

        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')