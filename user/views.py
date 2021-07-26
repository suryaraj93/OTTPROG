from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from series.forms import LanguageCreateForm, MovieCreateForm, SearchForm
from series.models import Language, Movie
from django.shortcuts import render
from user.forms import OrderForm, RegisterForm,OrderUpdateForm
from user.models import Orders
from django.contrib.auth.decorators import login_required

# USER VIEW MOVIE DETAILS
@login_required(login_url="loginpage")
def usermovieview(request, pk):
    obj = Movie.objects.get(id=pk)
    context = {}
    context['movies'] = obj
    return render(request, "user/userViewMovie.html", context)


# USER INDEX PAGE
@login_required(login_url="loginpage")
def userindex(request):
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
            return render(request, "user/userindex.html", context)

    return render(request, "user/userindex.html", context)


# USER ORDERS
@login_required(login_url="loginpage")
def userorder(request,pk):
    context = {}
    form=OrderForm(initial={'productid':pk,"user":request.user})
    context['form']=form
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"user/thanks.html")
    return render(request,"user/orders.html",context)




#USER REGISTER
def register(request):
    form=RegisterForm
    context={}
    context['form']=form
    if request.method =="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage')
        else:
            context={}
            context['form']=form
            return render(request, "user/registeration.html", context)
    return render(request,"user/registeration.html",context)

#LOGIN
def loginpage(request):
    if request.method=="POST":
        username = request.POST.get("uname")
        password = request.POST.get("pwd")
        if ((username == "admin") & (password == "admin")):
            return redirect('index')
        else:
            user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request, user)
                return redirect('userindex')
        else:
            return redirect('loginpage')
    return render(request, 'series/loginpage.html')

@login_required(login_url="loginpage")
def logOut(request):
    logout(request)
    return redirect("loginpage")


def uservieworders(request):
    qs = Orders.objects.filter(person=request.user)
    context = {}
    context['qs'] = qs
    return render(request, 'user/userviewdetails.html', context)