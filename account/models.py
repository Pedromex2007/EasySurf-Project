from tkinter.messagebox import YES
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from easysurfClubs.models import Club


class MainAccountManager(BaseUserManager):
    '''This will manage our account base and ensure proper fields are filled when creating a new user.'''

    def create_user(self, email, username, first_name, last_name, birth_date, password=None):
        if not email:
            raise ValueError("Email not defined for user!")
        if not username:
            raise ValueError("Username not defined!")
        if not first_name:
            raise ValueError("First name not defined!")
        if not last_name:
            raise ValueError("Last name not defined!")
        if not birth_date:
            raise ValueError("Birth date not defined!")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, birth_date, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
        ) 
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    '''This is the account base we're using. You can add/remove/edit any fields as neccessary.'''

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=12)

    home_address = models.CharField(max_length=40)

    active_club = models.ForeignKey(Club,on_delete=models.SET_NULL, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'birth_date']

    objects = MainAccountManager()

    def __str__(self):
        return self.first_name + ", " + self.last_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True