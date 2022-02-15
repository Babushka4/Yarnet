from django.db import models

from organization.models import Organization

class Department(models.Model):
  name = models.CharField(max_length=255)
  organizations = models.ManyToManyField(Organization)

  def __str__(self):
        return f"{self.name} [{self.id}]"