from django.views.generic import ListView, DetailView
# from django.views.generic.edit import UpdateView, DeleteView, CreateView
# from django.urls import reverse_lazy
from .models import Idea


class IdeaListView(ListView):
    model = Idea
    template_name = 'idea_list.html'
    context_object_name = 'idea_list'


class IdeaDetailView(DetailView):
    model = Idea
    template_name = 'idea_detail.html'
