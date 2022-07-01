from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('index1', views.index1, name='home1'),
    path('create1', views.create1, name='create1'),
    path('index2', views.index2, name='home2'),
    path('create2', views.create2, name='create2'),
    path('', views.index4, name='index'),
    path('add', views.add, name='add'),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
]
