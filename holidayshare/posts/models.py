#Posts Model
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
import misaka
from groups.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts')
    created_date = models.DateTimeField(auto_now =True)
    message = models.TextField(max_length=500)
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group,related_name='posts',null=True,blank=True)
    slug = models.SlugField(allow_unicode=True, unique=True)


    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        self.slug = slugify(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'slug': self.slug})


    def __str__(self):
        return self.message

    class Meta:
        ordering =['created_date']
        unique_together = ['user','message']
