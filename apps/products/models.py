from django.db import models
from simple_history.models import HistoricalRecords

from ..base.models import BaseModel

# Create your models here.
class Category(BaseModel):
  description = models.TextField()
  historical = HistoricalRecords()

  @property
  def _history_user(self):
    return self.changed_by

  @_history_user.setter
  def _history_user(self, value):
    self.changed_by = value

  def __str__(self):
    return self.description


class Product(BaseModel):
  name = models.CharField(max_length=100)
  description = models.TextField(null=True, blank=True)
  image = models.ImageField(upload_to='images/products/', null=True, blank=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
  historical = HistoricalRecords()

  @property
  def _history_user(self):
    return self.changed_by

  @_history_user.setter
  def _history_user(self, value):
    self.changed_by = value

  def __str__(self):
    return f'{self.name}: {self.description}'
