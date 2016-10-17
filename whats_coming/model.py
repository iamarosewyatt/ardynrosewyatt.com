from django.db.models import Model, CharField, ImageField, DateTimeField
from django.utils import timezone


class Item(Model):
    caption = CharField(max_length=200)
    image = ImageField(upload_to='whats-coming/')
    created = DateTimeField(editable=False)
    modified = DateTimeField(editable=False)

    def __str__(self):
        return self.caption

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Item, self).save(*args, **kwargs)
