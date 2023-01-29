from django.urls import path

from . import views


urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('list/', views.ImageListView.as_view()),
    path('detail/<int:pk>/', views.ImageDetailView.as_view()),
    path('create/', views.ImageCreateView.as_view()),
    path('update/<int:pk>/', views.ImageUpdateView.as_view()),
    path('delete/<int:pk>/', views.ImageDeleteView.as_view()),
]