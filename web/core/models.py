from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class ToDoCategory(models.Model):
    name = models.CharField(max_length=20)


class ToDo(models.Model):

    title = models.CharField(max_length=50, blank=False, null=False,)
    content = models.TextField(blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True,)
    is_done = models.BooleanField(default=False)
    category = models.ForeignKey(ToDoCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

