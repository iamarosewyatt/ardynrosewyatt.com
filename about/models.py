from django.db.models import Model, ImageField, DateTimeField, DateField, CharField
from django.utils import timezone


class Moment(Model):
    when = DateField()
    what = CharField(max_length=200)
    image = ImageField(upload_to='about/', blank=True)
    created = DateTimeField(editable=False)
    modified = DateTimeField(editable=False)

    def __str__(self):
        return '{}: {}'.format(self.when, self.what)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Moment, self).save(*args, **kwargs)
