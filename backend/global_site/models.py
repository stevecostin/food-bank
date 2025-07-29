from django.db import models

class GlobalConfiguration(models.Model):
    class Meta:
        db_table = 'global_configuration'

    name = models.CharField(max_length=50, default='Food Bank')