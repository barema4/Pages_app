from django.urls import path
from .views import HomePostPage

urlpatterns = [
    path('/post', HomePostPage.as_view(), name='post'),
]
