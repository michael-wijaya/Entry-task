from django.shortcuts import render,redirect, HttpResponse
from .models import Blogs,Like
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    blogs = Blogs.objects.all()
    list_like = []
    all_list = []
    for blog in blogs:
        #p = Blogs.objects.get(pk = blog.id)
        number_of_likes = blog.like_set.all().count()
        list_like.append(number_of_likes)
    for cnt,blog in enumerate(blogs):
        all_list.append((blog,list_like[cnt]))
    return render(request,'home.html',{'blogs':all_list})
def post(request):
    title = str(request.POST['title'])
    desc = str(request.POST['description'])
    username = request.user
    Blogs(title = title, desc = desc, author = username).save()
    return redirect("/")

@login_required
def like(request, pk):
    new_like, created = Like.objects.get_or_create(user=request.user, blog_id=pk)
    if not created:
        Like.objects.filter(user=request.user, blog_id=pk).delete()
        return redirect("/")
    else:
        return redirect("/")
        # oll korrekt

@login_required
def delete(request,pk):
    if(Blogs.objects.filter(author_id=request.user, id=pk)):
        Blogs.objects.filter(author_id=request.user, id=pk).delete()
    return redirect("/")

def read(request,pk):
    blogs = Blogs.objects.filter(id=pk)
    list_like = []
    all_list = []
    for blog in blogs:
        #p = Blogs.objects.get(pk = blog.id)
        number_of_likes = blog.like_set.all().count()
        list_like.append(number_of_likes)
    for cnt,blog in enumerate(blogs):
        all_list.append((blog,list_like[cnt]))
    return render(request,'read.html',{'blogs':all_list})