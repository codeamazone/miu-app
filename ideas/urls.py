from django.urls import path
from .views import (
    # HomePageView,
    IdeaListView,
    IdeaDetailView,
    IdeaUpdateView,
    IdeaCreateView,
    IdeaDeleteView,
)

urlpatterns = [
    path('<int:pk>/edit', IdeaUpdateView.as_view(), name='idea_update'),
    path('<int:pk>', IdeaDetailView.as_view(), name='idea_detail'),
    path('<int:pk>/delete', IdeaDeleteView.as_view(), name='idea_delete'),
    path('new', IdeaCreateView.as_view(), name='idea_new'),
    path('', IdeaListView.as_view(), name='idea_list'),
]
