from django.urls import path
from .views import SuggestionAPI

urlpatterns = [
    path('', SuggestionAPI.as_view(), name='suggestions-api'),
]