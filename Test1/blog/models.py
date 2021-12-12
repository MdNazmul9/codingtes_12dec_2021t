from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from accounts.models import CustomUser
from django.urls import reverse

class Post(models.Model):
    title= models.CharField(max_length=100)
    # contentent = models.TextField()
    body = RichTextUploadingField()
    # body = RichTextField()
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    class Meta:
        ordering = ('-id',)
    def __str__(self):
        return self.title

    def  get_absolute_url(self):
        return reverse('blog:post_details', kwargs={'pk': self.pk})