from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class ToDo(models.Model):

    title = models.CharField(max_length=50, blank=False, null=False,)
    content = models.TextField(blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True,)
    # user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

