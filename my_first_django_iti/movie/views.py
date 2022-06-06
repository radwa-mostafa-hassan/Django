from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm


def movies_list(request):
    return render(request, template_name='movie/list.html', context={'movies': Movie.objects.all()})


def movie_create(request):
    form = MovieForm(data=request.POST or None, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('movie:list')

    return render(request, template_name='movie/create.html', context={'form': form})


def movie_detail(request, pk):
    return render(request, template_name='movie/detail.html', context={'movie': Movie.objects.get(pk=pk)})
