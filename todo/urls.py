from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('toggle/<int:pk>/', views.toggle_task, name='toggle_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='todo/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]