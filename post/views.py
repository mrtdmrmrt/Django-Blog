from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
# Create your views here.
def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html',{'posts': posts})
def post_detail(request, id):
    post = get_object_or_404(Post, id=id) #eger sayfa gelmezse 404 sayfa hatasi vermesi icin
    context = {
        'post':post
    }
    return render(request, 'post/detail.html', context)
def post_create(request):
    return HttpResponse('Burasi Post Create Sayfasi')
def post_update(request):
    return HttpResponse('Burasi Post Update Sayfasi')
def post_delete(request):
    return HttpResponse('Burasi Post Delete Sayfasi')