import uuid

from computedfields.models import ComputedFieldsModel, computed
from django.db import models


class ModelA(ComputedFieldsModel):
    id = models.UUIDField(primary_key=True, default=None, editable=False)

    name = models.CharField(max_length=60, blank=True)

    @computed(
        models.IntegerField(),
        depends=[
            ['modelb_set', ['name']],
        ],
    )
    def number_of_model_a_objects(self):
        return self.modelb_set.count()

    def save(self, *args, **kwargs):
        if self.pk is None:
            # creation of UUID when saving if not provided
            self.id = uuid.uuid4()

        super().save(*args, **kwargs)


class ModelB(models.Model):
    model_a = models.ForeignKey('ModelA', on_delete=models.CASCADE)

    name = models.CharField(max_length=60, blank=True)
