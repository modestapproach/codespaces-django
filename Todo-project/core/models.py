from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass

class Todo(models.Model):
    description = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)    

    # def __call__(self, *args: Any, **kwds: Any) -> Any:
    #     return self.description
    
    