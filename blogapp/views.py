from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy
# Create your views here.
# def home(request):
#     return render(request,'blogapp/home.html',{})

class HomeView(ListView):
    model = Post
    template_name = 'blogapp/home.html'
    ordering = ['-publish_date']
    # ordering = ['-id']

    def get_context_data(self,*args,**kwars):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwars)
        context['cat_menu'] = cat_menu
        return context

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request,'blogapp/category_list.html',{'cat_menu_list':cat_menu_list})
    
def CategoryView(request,cats):
    category_posts = Post.objects.filter(category=cats.replace('-',' '))
    return render(request,'blogapp/categories.html',{'cats':cats.title().replace('-' , ' '),'category_posts':category_posts})



class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blogapp/article_detail.html'

    def get_context_data(self,*args,**kwars):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView,self).get_context_data(*args,**kwars)
        context['cat_menu'] = cat_menu
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blogapp/add_post.html'
    # fields = '__all__'

class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'blogapp/add_post.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blogapp/update_post.html'
    # fields = ('title','title_tag','body')

class DeletePostView(DeleteView):
    model = Post
    # form_class = EditForm
    template_name = 'blogapp/delete_post.html'
    success_url = reverse_lazy('home')
    # fields = ('title','title_tag','body')