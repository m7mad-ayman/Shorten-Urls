from django.urls import path
from .views import *
urlpatterns = [
    path('shorten/',shortenView,name="short"),
    path('<str:rand>',redirectView),
]