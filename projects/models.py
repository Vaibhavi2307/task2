from django.db import models

class Projects(models.Model):
    project_name=models.CharField(max_length=50)
    project_description=models.TextField()
    project_lead=models.CharField(max_length=20)
    team_size=models.IntegerField()
    programming_language=models.CharField(max_length=20)
    project_start_date=models.DateField()
    project_delivery_date=models.DateField()
    
