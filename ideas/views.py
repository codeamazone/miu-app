from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Idea


class IdeaListView(ListView):
    model = Idea
    template_name = 'idea_list.html'
    context_object_name = 'idea_list'


class IdeaDetailView(DetailView):
    model = Idea
    template_name = 'idea_detail.html'


class IdeaUpdateView(UpdateView):
    model = Idea
    fields = ('idea', 'kind', 'description', 'next_steps', 'status')
    template_name = 'idea_update.html'


class IdeaCreateView(CreateView):
    model = Idea
    fields = ('idea', 'kind', 'description', 'next_steps', 'status')
    template_name = 'idea_new.html'


class IdeaDeleteView(DeleteView):
    model = Idea
    template_name = 'idea_delete.html'
    success_url = reverse_lazy('idea_list')
