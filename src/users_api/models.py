from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

MESSAGE_NO_EMAIL = "Veuillez saisir un mail !"
MESSAGE_NO_PSEUDO = "Veuillez saisir un pseudo !"
# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, pseudo, first_name, last_name, age, email, can_be_contacted, can_data_be_shared, password=None):
        if not pseudo:
            raise ValueError(MESSAGE_NO_PSEUDO)

        if not email:
            raise ValueError(MESSAGE_NO_EMAIL)

        user = self.model(
            pseudo=pseudo,
            first_name=first_name,
            last_name=last_name,
            age=age,
            email=self.normalize_email(email),
            can_be_contacted=can_be_contacted,
            can_data_be_shared=can_data_be_shared,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, pseudo, first_name, last_name, age, email, can_be_contacted, can_data_be_shared, password=None):
        user = self.create_user(pseudo=pseudo, first_name=first_name,
                                last_name=last_name, age=age,
                                email=email,
                                can_be_contacted=can_be_contacted,
                                can_data_be_shared=can_data_be_shared,
                                password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class UserProfile(AbstractBaseUser):
    pseudo = models.CharField(
        unique=True,
        max_length=10,
        blank=False
    )
    first_name = models.CharField(
        max_length=100,
        blank=True
    )
    last_name = models.CharField(
        max_length=100,
        blank=True
    )
    age = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(110),
            MinValueValidator(1)
        ],
        blank = True,
        null = True
    )
    email = models.EmailField(
        unique=True,
        max_length=100,
        blank=False
    )
    can_be_contacted = models.BooleanField(default=True)
    can_data_be_shared = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "pseudo"
    REQUIRED_FIELDS = ["first_name", "last_name", "age", "email", "can_be_contacted", "can_data_be_shared"]
    objects = MyUserManager()

    def save(self, *args, **kwargs):
        if self.age < 15:
            self.can_data_be_shared = False
        super(UserProfile, self).save(*args, **kwargs)
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
