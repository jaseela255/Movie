from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import movie
from . forms import movieForm


# Create your views here.
def demo(request):
    movies=movie.objects.all()
    context={
        'movie_list':movies
    }
    
    return render(request,'index.html',context)

def detail(request,movie_id):
    Movie=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'Movie':Movie})

def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']

        movieS=movie(name=name,desc=desc,year=year,img=img)
        movieS.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,movie_id):
    moviess=movie.objects.get(id=movie_id)
    form=movieForm(request.POST or None,request.FILES,instance=moviess)
    if form.is_valid():
         form.save()
         return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':moviess})


def delete(request,movie_id):
    if request.method=='POST':
        Movies=movie.objects.get(id=movie_id)
        Movies.delete()
        return redirect('/')
    return render(request,'delete.html')