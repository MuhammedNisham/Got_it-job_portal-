from django.db import models

# Create your models here.
class Job(models.Model):
    company_name = models.CharField(max_length=255)
    job_role = models.CharField(max_length=255)
    job_description = models.CharField(max_length=500)
    requirements = models.CharField(max_length=255)

    def __str__(self):
        return f"Product: {self.company_name}" 