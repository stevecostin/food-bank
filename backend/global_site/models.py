from django.db import models

class SingletonModel(models.Model) :
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class GlobalConfiguration(SingletonModel):
    class Meta:
        db_table = 'global_configuration'

    name = models.CharField(max_length=50, default='Food Bank')