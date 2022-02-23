from django.shortcuts import redirect, render 
from django.views import View
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import  PostCreateUpdateForm
from django.utils.text import slugify


class HomeView(View):
    def get(self , request):
        posts = Post.objects.all()
        return render(request , 'home/index.html' , {'posts': posts})


class PostDetailView(View):
    def get(self, request , post_slug):
        post = Post.objects.get(slug = post_slug)
        return render(request , 'home/post_detail.html', {'post' : post})


class PostDeletelView(LoginRequiredMixin , View):
    def get(self,request, post_id):
        post = Post.objects.get(id = post_id)
        if post.user.id ==request.user.id:
            post.delete()
            messages.success(request , 'post deleted successfully' , 'success')
        else:
            messages.error(request , 'you cannot delete this post!' , 'danger')
        return redirect('home:home')
            

class PostUpdateView(LoginRequiredMixin , View):
    form_class = PostCreateUpdateForm
    def setup(self, request, *args, **kwargs):
        self.post_instance = Post.objects.get(id = kwargs['post_id'])
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        post = self.post_instance
        if not post.user.id == request.user.id:
            messages.error(request , 'you can not update this post' , 'danger')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        post = self.post_instance
        form = self.form_class(instance=post)
        return render(request , 'home/post_update.html' , {'form':form})
    def post(self, request, *args, **kwargs):
        post = self.post_instance
        form = self.form_class(request.POST , instance=post)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(form.cleaned_data['body'][:30])
            new_post.save()
            messages.success(request , 'you updated this post' , 'success')
            return redirect('home:post_detail' , post.slug)
            

class PostCreateView(LoginRequiredMixin , View):
    form_class = PostCreateUpdateForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request , 'home/post_create.html' , {'form':form})
        
    def post(self, request , *args , **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(form.cleaned_data['body'][:30])
            new_post.user = request.user
            new_post.save()
            messages.success(request , 'you created this post' , 'success')
            return redirect('home:post_detail' , new_post.slug)
