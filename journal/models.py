from ckeditor.fields import RichTextField
from django.contrib.sites.models import Site
from django.db.models import Model, CharField, ImageField, DateTimeField, SlugField
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone
from tagging.fields import TagField


class Post(Model):
    title = CharField(max_length=200)
    image = ImageField(upload_to='journal/')
    tags = TagField()
    content = RichTextField()
    created = DateTimeField(editable=True, default=timezone.now)
    modified = DateTimeField(editable=False)
    slug = SlugField(editable=False)

    def __str__(self):
        return self.title

    def permalink(self):
        return 'http://{}{}'.format(Site.objects.get_current(), self.get_absolute_url())

    def get_absolute_url(self):
        return reverse('journal:post', kwargs={
            'year': self.created.year,
            'month': self.created.month,
            'day': self.created.day,
            'slug': self.slug
        })

    def save(self, *args, **kwargs):
        self.modified = timezone.now()
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)
