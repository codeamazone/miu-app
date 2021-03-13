from django.views.generic import ListView
# from django.views.generic.edit import UpdateView, DeleteView, CreateView
# from django.urls import reverse_lazy
from .models import Idea


class HomePageView(ListView):
    model = Idea
    template_name = 'home.html'
    context_object_name = 'idea_list'
