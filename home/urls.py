from django.urls import path,re_path
from . import views
app_name = 'home'
urlpatterns = [
    re_path('^$', views.index, name='index'),
    re_path('^post$', views.post, name='post'),
    path('<int:pk>/',views.like, name='like'),
    path('delete/<int:pk>/',views.delete, name='delete'),
    path('read/<int:pk>/', views.read, name='read')
]