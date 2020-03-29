from django.db import models

# Create your models here.



class user(models.Model):
    real_name = models.CharField(max_length=20)
    tz= models.CharField(max_length=50)
  

  
    def __unicode__(self):
        return self.real_name  



class activity_period(models.Model):
	start_time = models.DateField()
	end_time = models.DateField()
	user = models.ForeignKey(user, on_delete=models.CASCADE,related_name='activity_periods')



