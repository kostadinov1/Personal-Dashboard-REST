
from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models

from web.accounts.managers import AppUsersManager
from web.common.validators import validate_only_letters, MaxFileSizeInMbImageValidator


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(unique=True, null=False, blank=False,)
    date_joined = models.DateTimeField(auto_now_add=True,)

    has_profile = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False,)
    is_active = models.BooleanField(default=True)

    objects = AppUsersManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    IMAGE_MAX_SIZE = 5
    GENDERS = (('Male', 'Male'), ('Female', 'Female'), ('LGBT+', 'LGBT+'), ('Prefer Not to Tell', 'Prefer Not to Tell'),)

    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH, blank=False, null=False,
                                  validators=(validate_only_letters, MinLengthValidator(2)))
    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH,null=False, blank=False,
                                 validators=(validate_only_letters, MinLengthValidator(2)))
    dob = models.DateField(null=False, blank=False,)
    gender = models.CharField(max_length=30, choices=GENDERS, null=False, blank=False)
    phone = models.CharField(max_length=10, unique=True, null=True, blank=True)
    image_local = models.ImageField(blank=True, null=True, upload_to='profile_images',
                                    validators=(MaxFileSizeInMbImageValidator(IMAGE_MAX_SIZE),))
    image_url = models.URLField(blank=True, null=True)
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key=True,)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

