from django.db import models

from apps.users.models import CustomizerUser

# Create your models here.


class Post(models.Model):

    class PostObjects():
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='img', blank=True, null=True)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(
    max_length=250, unique_for_date='published', null=False, unique=True)
    published = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(
    CustomizerUser, on_delete=models.CASCADE, related_name='post_user')
    status = models.CharField(max_length=50, choices={(
        'draft', 'Draft'), ('published', 'Published')}, default='draft')
    objects = models.Manager()
    post_objects = PostObjects()

    class Meta:
        
        ordering = ('-published',)

    def __str__(self) -> str:
        return f"{self.title}"