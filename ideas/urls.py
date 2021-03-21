from django.urls import path
from .views import (
    # HomePageView,
    IdeaListView,
    IdeaDetailView,
    IdeaUpdateView,
    # IdeaDeleteView,
    # IdeaCreateView,
)

urlpatterns = [
    path('<int:pk>/edit', IdeaUpdateView.as_view(), name='idea_update'),
    path('<int:pk>', IdeaDetailView.as_view(), name='idea_detail'),
    path('', IdeaListView.as_view(), name='idea_list'),
]
