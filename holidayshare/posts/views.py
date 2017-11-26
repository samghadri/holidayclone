# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views import generic
django django.http import Http404
from braces.views import SelectRelatedMixin
from . import models
from . import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class PostList(SelectRelatedMixin, generic.ListView):

    model = models.Post
    select_related = ('user','group')
    
