from .views import *
from django.urls import path

urlpatterns = [
    # path('',home,name='home'),
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article'),
    path('add_post/',AddPostView.as_view(),name='add_post'),
    path('add_category/',AddCategoryView.as_view(),name='add_category'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name='update_post'),
    path('article/delete/<int:pk>',DeletePostView.as_view(),name='delete_post'),
    path('category/<str:cats>',CategoryView,name='category'),
    path('category_list/',CategoryListView,name='category_list'),
]