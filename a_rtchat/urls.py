from django.urls import path
from .views import *

urlpatterns = [
    path('', chat_view, name="home"),
    path('<username>', get_or_create_chatgroup, name="private-chat"),
    path('dm/<group_name>', chatroom_view, name="private-chatroom"),
]