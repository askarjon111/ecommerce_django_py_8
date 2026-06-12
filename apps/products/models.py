from django.db import models
from apps.common.models import BaseModel
from django.utils.safestring import mark_safe


class Catigory(BaseModel):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='image/catirgory',null=True)

    def __str__(self):
        return self.name
    
    
    def get_icon(self):
        return mark_safe(self.icon)

class Product(BaseModel):
    name = models.CharField(max_length=50)
    disc = models.TextField()
    
    catigory = models.ForeignKey(Catigory,on_delete=models.SET_NULL,null=True,)
    
    price = models.FloatField()
    
    def __str__(self):
        return self.name
    





    
    


