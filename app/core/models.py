"""
Database models
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

class UserManager(BaseUserManager):
    """Manager for user profiles."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('Users must have an email address')
        # Create a new user model
        user = self.model(email=self.normalize_email(email), **extra_fields)
        # Set the password
        user.set_password(password)
        # Save the user model
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create, save and return a new superuser."""
        # Create a new superuser with create_user method
        user = self.create_user(email, password)
        # Set the user as a superuser
        user.is_superuser = True
        user.is_staff = True
        # Save the user model
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # is_active is required by Django
    is_active = models.BooleanField(default=True)
    # is_staff is required by Django
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    # Override the default username field to email
    USERNAME_FIELD = 'email'
