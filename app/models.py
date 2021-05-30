from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length=200)
    user_email = models.EmailField(max_length = 254,blank=True,  unique= True)




    def __str__(self):
        return self.first_name, self.last_name,self.user_email
