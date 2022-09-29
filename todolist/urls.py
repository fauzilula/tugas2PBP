from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('login/', userlogin, name='login_user'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout_user'),
    path('addtask/', addtodo, name='addtask'),
    path('update/<int:id>', updated, name='update'),
    path('delete/<int:id>', deleted, name='delete'),
]