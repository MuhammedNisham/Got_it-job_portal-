from django.db import models

# Create your models here.
class Job(models.Model):
    company_name = models.CharField(max_length=255, blank=True, null=True)
    job_role = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    salary = models.CharField(max_length=255, blank=True, null=True)
    experience = models.CharField(max_length=255, blank=True, null=True)
    job_description = models.CharField(max_length=500, blank=True, null=True)
    responsibilities = models.CharField(max_length=500, blank=True, null=True)
    requirements = models.CharField(max_length=500, blank=True, null=True)
    about_company = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"Product: {self.company_name}"  