from django.db import models


class BaseModel(models.Model):
    created_at = models.TimeField(auto_now_add=True)
    upted_at = models.TimeField(auto_now=True)
    
    class Meta:
        abstract = True  