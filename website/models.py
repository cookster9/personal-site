from django.db import models

# Create your models here.
class Modal(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, db_column='title', blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(max_length=2048, db_column='content', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'modal'

# class MyRouter(object):
#     def db_for_read(self, model, **hints):
#         """
#         Reads go to a randomly-chosen replica.
#         """
#         return random.choice(['replica1', 'replica2'])
