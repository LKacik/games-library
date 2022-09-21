"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from warehouse import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('add/', views.add, name='add'),
    path('remove/', views.remove, name='remove'),
    path('edit/', views.edit, name='edit'),
    path('search/', views.search, name='search'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),
    path('<slug:slug>/', views.SingleView.as_view(), name='single'),
]