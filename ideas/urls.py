from django.urls import path
from .views import (
    HomePageView,
    # ArticleUpdateView,
    # ArticleDetailView,
    # ArticleDeleteView,
    # ArticleCreateView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home')
]
