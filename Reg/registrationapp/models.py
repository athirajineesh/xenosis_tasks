from django.db import models

# Customising the div Why choose us
class Place(models.Model):
    head=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    description=models.TextField()

class Team(models.Model):
    name=models.CharField(max_length=250)
    photo=models.ImageField(upload_to='pics')
    define=models.TextField()



