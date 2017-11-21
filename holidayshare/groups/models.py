#Groups Models
from django.db import models
from django.utils.text import slugify
import misaka
from django.contrib.auth import get_user_model
User = get_user_model()
from django import template
register = template.Library()

class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='membership')
    user = models.ForeignKey(User,related_name='user_members')
    def __st__(self):
        return self.user.username


    class Meta:
        unique_together = ('group','user')
