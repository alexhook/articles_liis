from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password, role=None):
        user = self.model(email=self.normalize_email(email), role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        # Setting up the "Author" role for full access.
        user.role = 1
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        (1, 'Author'),
        (2, 'Subscriber'),
    )
    
    email = models.EmailField(max_length=255, unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=2)

    is_active = models.BooleanField(
        'Active', 
        default=True,
    )
    is_admin = models.BooleanField(
        'Admin', 
        default=False,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin