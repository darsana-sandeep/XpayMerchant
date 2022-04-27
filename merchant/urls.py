from django.urls import path

from merchant import views

urlpatterns = [
        path('',views.register),
        path('login',views.login),
        path('base',views.base),
        path('logout',views.logout)
]
