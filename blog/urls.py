from django.urls import path
from . import views
urlpatterns = [
    path('post/new/', views.post_new, name='post_new'),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #That means if you enter http://127.0.0.1:8000/post/5/ into your browser, Django will understand that you are looking for a view called post_detail and transfer the information that pk equals 5 to that view
]
