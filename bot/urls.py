from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.chat, name='chatbot_view'),
]