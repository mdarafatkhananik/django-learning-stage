from django.shortcuts import render,redirect
from .models import Blog
from .forms import Blog_Form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.

# this is all object get request
def show_blog(request):
    blog_data=Blog.objects.all()
    return render(request,'blog/show_blog.html',{'blog_data':blog_data})

# this is post request
@login_required
def post_blog(request):
    if request.method == 'POST':
        form=Blog_Form(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request,'You Successfuly blog post Created!')
            return redirect('show_blog')
    else:
        form=Blog_Form()
    return render(request,'blog/post_blog.html',{'form':form})

# this is single object get request
def details_blog(request,slug):
    detail=get_object_or_404(Blog,slug_field=slug)
    return render(request,'blog/details_blog.html',{'detail':detail})

# this is update request
@login_required
def update_blog(request,slug):
    post=get_object_or_404(Blog,slug_field=slug)
    
    if request.user != post.user:
        messages.error(request,'You are not allowed to update this post!')
        return redirect('details_blog',slug=post.slug_field)
    if request.method == 'POST':
        form=Blog_Form(request.POST,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfuly updated your blog post!')
            return redirect('details_blog',slug=post.slug_field)
    return redirect('details_blog',slug=post.slug_field)

# this is delete request
@login_required
def delete_blog(request,slug):
    post=get_object_or_404(Blog,slug_field=slug)

    if post.user != request.user:
        messages.error(request, 'You are not allowed to delete this post!')
        return redirect('show_blog')

    if request.method == 'POST':
        post.delete()
        messages.error(request,'Successfuly deleted your blog post!')
        return redirect('show_blog')
    return redirect('details_blog',slug=post.slug_field)
