from django.shortcuts import render, redirect
from series.forms import LanguageCreateForm, MovieCreateForm, SearchForm
from series.models import Language, Movie
from user.models import Orders
from user.forms import OrderForm,OrderUpdateForm
from django.contrib.auth.decorators import login_required

# CREATE LANGUAGE

def createlanguage(request):
    form = LanguageCreateForm
    context = {}
    context['form'] = form
    qs = Language.objects.all()
    # context = {}
    context['qs'] = qs
    if request.method == "POST":
        form = LanguageCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createlanguage')
    return render(request, "series/createLanguage.html", context)


# EDIT LANGUAGE

def languageedit(request, pk):
    form = Language.objects.get(id=pk)
    form = LanguageCreateForm(instance=form)
    context = {}
    context['form'] = form
    if request.method == "POST":
        form = Language.objects.get(id=pk)
        form = LanguageCreateForm(instance=form, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("createlanguage")
    return render(request, "series/editLanguage.html", context)


# DELETE LANGUAGE

def languagedelete(request, pk):
    entry = Language.objects.get(id=pk)
    entry.delete()
    form = LanguageCreateForm
    context = {}
    context['form'] = form
    qs = Language.objects.all()
    context['qs'] = qs
    return redirect("createlanguage")


# CREATE MOVIE

def createmovie(request):
    form = MovieCreateForm
    context = {}
    context['form'] = form
    movies = Movie.objects.all()
    context['movies'] = movies
    if request.method == "POST":
        form = MovieCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("createmovie")
    return render(request, "series/createMovie.html", context)


# EDIT MOVIE

def movieedit(request, pk):
    form = Movie.objects.get(id=pk)
    form = MovieCreateForm(instance=form)
    context = {}
    context['form'] = form
    if request.method == "POST":
        form = Movie.objects.get(id=pk)
        form = MovieCreateForm(instance=form, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("createmovie")
    return render(request, "series/editMovie.html", context)


# DELETE MOVIE

def moviedelete(request, pk):
    entry = Movie.objects.get(id=pk)
    entry.delete()
    form = MovieCreateForm
    context = {}
    context['form'] = form
    qs = Language.objects.all()
    context['qs'] = qs
    return redirect("createmovie")


# VIEW MOVIE DETAILS

def movieview(request, pk):
    obj = Movie.objects.get(id=pk)
    context = {}
    context['movies'] = obj
    return render(request, "series/viewMovie.html", context)


# INDEX PAGE

def index(request):
    movies = Movie.objects.all()
    # form=MovieCreateForm
    context = {}
    context['movies'] = movies
    form = SearchForm
    context['search'] = form
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            language = form.cleaned_data.get("lang")
            items = Movie.objects.filter(language__lang=language)
            context['movies'] = items
            return render(request, "series/index.html", context)

    return render(request, "series/index.html", context)

def vieworders(request):
    qs = Orders.objects.all()
    context = {}
    context['qs'] = qs
    return render(request, 'series/vieworders.html', context)

def orderdetails(request,pk):
    qs=Orders.objects.get(id=pk)
    form=OrderUpdateForm (instance=qs)
    context={}
    context['form']=form
    if request.method=="POST":
        form = OrderUpdateForm(instance=qs,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("vieworders")
    return render(request,"series/orderdetails.html",context)
