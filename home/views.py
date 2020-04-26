from django.shortcuts import render, HttpResponse

# Create your views here.
def home_view(request):
    #return HttpResponse('<h1>Hello</h1>')
    #home templatetini ekledikten sonra
    if request.user.is_authenticated:
        context={
            'isim': 'Mert',
        }
    else:
        #Admin paneline giris yapmadiysa misafir yazar
        context = {
            'isim': 'Misafir',
        }
    return render(request, 'home.html', context)