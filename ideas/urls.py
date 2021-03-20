from django.urls import path
from .views import (
    # HomePageView,
    IdeaListView,
    IdeaDetailView
    # ArticleUpdateView,
    # ArticleDeleteView,
    # ArticleCreateView,
)

urlpatterns = [
    path('', IdeaListView.as_view(), name='idea_list'),
    path('<int:pk>', IdeaDetailView.as_view(), name='idea_detail')
]
