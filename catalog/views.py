from django.shortcuts import render
from .models import Story
from . models import Product
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.models import User

class storyListView(generic.ListView):
    model = Story

class storyDetailView(generic.DetailView):
    model = Story

class profile(storyListView):
    template_name = "catalog/profile.html"
    def get_queryset(self):
        return Story.objects.filter(Author=self.request.user)

class instructionsView(storyListView):
    template_name = "instructions.html"
    def get_queryset(self):
        return Story.objects.filter(featured = True )

class productListView(generic.ListView):
    model = Product

class productDetailView(generic.DetailView):
    model = Product

#All the functions needed to create, update and delete storyies
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from PIL import Image #imports Pillow library
import request
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files import File
import datetime

from .forms import NewStoryForm

def NewStory(request):

    #if post request process the form
    if request.method == 'POST':
        #request.Files required for imagefield
        form = NewStoryForm(request.POST, request.FILES)
        if form.is_valid():
            #saves all items this far but commit=false allows us to change Story.Author
            Story = form.save()

            if request.user.is_authenticated:
                Story.Author = request.user

            Story.save()
            if request.user.is_authenticated:
                return HttpResponseRedirect(reverse('user-profile'))
            else:
                return HttpResponseRedirect(reverse('storyList'))

    else:
        form = NewStoryForm()
        return render(request, 'catalog/story_form.html', {'form': form})


class storyUpdate(UpdateView):
    model = Story
    fields = ['title', 'photo', 'story']


class storyDelete(DeleteView):
    model = Story
