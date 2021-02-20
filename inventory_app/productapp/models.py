from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    

    def getImageUrl(self):
        return f"products/{self.image}"

