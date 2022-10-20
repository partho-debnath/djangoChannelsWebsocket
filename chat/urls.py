from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [ 
    path('', views.IndexView.as_view(), name='home'),
    path('group/', views.ChatView.as_view(), name='chat-view'),
]
