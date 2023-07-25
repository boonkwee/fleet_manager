from django.db import models

# Create your models here.
class RequesterType(models.Model):
  requester_type = models.CharField(primary_key=True, max_length=40,
                                    verbose_name="Requester Type",
                                    db_column='requester_type')

  requester_type_description = models.CharField(blank=True, null=True, max_length=80,
                                                verbose_name="Description",
                                                db_column='requester_type_description')

  requester_type_sortorder = models.IntegerField(default=0,
                                                 verbose_name='Sort Order',
                                                 db_column='requester_type_sortorder')

  requester_type_modified = models.DateTimeField(auto_now=True, verbose_name="Modified")
  requester_type_created = models.DateTimeField(auto_now_add=True, verbose_name="Created")

  class Meta:
    db_table = "tbl_requester_type"
    ordering = ('requester_type_sortorder',)

  def __str__(self):
    return self.requester_type
