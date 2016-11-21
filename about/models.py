from ckeditor.fields import RichTextField
from django.db.models import Model, ImageField, DateTimeField, CharField, PositiveSmallIntegerField
from django.utils import timezone
from ordered_model.models import OrderedModel


class Moment(OrderedModel):
    order = PositiveSmallIntegerField()
    when = CharField(max_length=20)
    what = RichTextField(config_name='moment')
    image = ImageField(upload_to='about/', blank=True)
    created = DateTimeField(editable=False)
    modified = DateTimeField(editable=False)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.when

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Moment, self).save(*args, **kwargs)
