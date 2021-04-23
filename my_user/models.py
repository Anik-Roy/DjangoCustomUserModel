from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.utils.translation import ugettext_lazy

# Create your models here.


class UserProfileManager(BaseUserManager):
    """ A Custom Manager to deal with emails as unique identifier """
    def _create_user(self, email, password, **extra_fields):
        """ Create and saves a user with a given email and password """
        if not email:
            raise ValueError('The Email must be set!')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        self._create_user(email, password, **extra_fields)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255)
    is_active = models.BooleanField(
        ugettext_lazy('active'),
        default=True,
        help_text=ugettext_lazy('Designates weather this user should be treated as active. Unselect this insist of deleting account.')
    )
    is_staff = models.BooleanField(
        ugettext_lazy('staff_status'),
        default=False,
        help_text=ugettext_lazy('Designates weather the user can log in this admin site')
    )

    USERNAME_FIELD = 'email'
    objects = UserProfileManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email