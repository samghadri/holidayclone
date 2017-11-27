#members Views
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib import messages
from . models import Group,GroupMember
from . import models

class BuildGroup(LoginRequiredMixin,generic.CreateView):
    fields = ('name', 'description')
    model = Group


class SingleGroup(generic.DetailView):
    model = Group


class ListGroups(generic.ListView):
    model = Group

class JoinGroup(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request, *args,**kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))
        try:
            GroupMember.objects.create(user=self.request.user, group = group)
        except:
            messages.warning(self.request,('Ops! You are already a member'))
        else:
            messages.success(self.request,('You Have Joined!! '))
        return super().get(request,*args, **kwargs)



class LeaveGroup(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self,*args, **kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request, *args, **kwargs):
        try:
            membership = models.GroupMember.objects.filter(user=self.request.user,group__slug=self.kwargs.get('slug')).get()
        except models.GroupMember.DoesNotExist:
            messages.warning(self.request,'You are not a member')
        else:
            membership.delete()
            messages.success(self.request,'You have left the Group')
        return super().get(request,*args,**kwargs)
