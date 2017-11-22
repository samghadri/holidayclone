#members Views
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.urlresolvers import reverse
from django.views import generic
from . models import Group,GroupMember


class BuildGroup(LoginRequiredMixin,generic.CreateView):
    fields = ('name', 'description')
    model = Group


class SingleGroup(generic.DeleteView):
    model = Group


class ListGroups(generic.ListView):
    model = Group
