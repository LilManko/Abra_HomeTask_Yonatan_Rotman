from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView)

urlpatterns = [
    path('',views.endpionts),
    path('register/', views.register),
    path('login/', TokenObtainPairView.as_view()),
    path('logout/',views.Logout),
    path('send_message/',views.send_message),
    path('read_message/', views.read_message),
    path('get_user_messages/',views.get_user_messages),
    path('get_unread_user_messages/',views.get_unread_user_messages),
    path('delete_message/',views.delete_message),

]