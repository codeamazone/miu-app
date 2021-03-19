from django.urls import path
from .views import (
    HomePageView,
    IdeaDetailView
    # ArticleUpdateView,
    # ArticleDetailView,
    # ArticleDeleteView,
    # ArticleCreateView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<int:pk>', IdeaDetailView.as_view(), name='idea_detail')
]
