from django.db import models
from django.utils import timezone
from django.contrib.sites.models import Site


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="static/images/journal/")
    content = models.TextField()
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)

    def __str__(self):
        return self.title

    def permalink(self):
        return 'http://{}{}'.format(Site.objects.get_current(), self.get_absolute_url())

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('journal.views.post', args=[
            self.created.year,
            self.created.month,
            self.created.day,
            self.id
        ])

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Post, self).save(*args, **kwargs)
