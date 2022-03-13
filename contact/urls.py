from django.urls import path, include
from .views import emailView


urlpatterns = [
    path('contact/', emailView, name='contact'),
]