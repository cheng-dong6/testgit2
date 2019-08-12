from django.db import models

# Create your models here.

class personal_information(models.Model):
    personal_ip = models.CharField(max_length=50)
    personal_height = models.IntegerField(verbose_name='身高(/cm)', unique=False)
    personal_weight = models.IntegerField(verbose_name='体重(/kg)', unique=False)
    personal_bmi = models.FloatField(verbose_name='BMI', unique=False,max_length=4)
    time = models.DateTimeField(verbose_name='时间', auto_now_add=True)
    def __str__(self):
        return self.personal_ip
