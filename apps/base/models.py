from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class BaseModel(models.Model):
  id = models.AutoField(primary_key=True)
  is_active = models.BooleanField(default=True)
  created_at = models.DateField(auto_now=False, auto_now_add=True)
  modified_at = models.DateField(auto_now=True, auto_now_add=False)
  deleted_at = models.DateField(auto_now=True, auto_now_add=False)
  historical = HistoricalRecords(user_model='user.User', inherit=True)

  @property
  def _history_user(self):
    return self.changed_by

  @_history_user.setter
  def _history_user(self, value):
    self.changed_by = value
  class Meta:
    abstract = True
