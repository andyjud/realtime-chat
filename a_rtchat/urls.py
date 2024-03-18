from django.urls import path
from .views import *

urlpatterns = [
    path('', chat_view, name="home"),
    path('<username>', get_or_create_chatgroup, name="home"),
]
