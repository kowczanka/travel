from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models




class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, is_traveler, password=None):
        if not email:
            raise ValueError("Please add your email")
        if not username:
            raise ValueError("Please add your username")
        if not is_traveler:
            raise ValueError(""" Please, tell us if you are a traveler. 
            Being a traveler gives you more options in our app! """)

        user = self.model(
            email=self.normalize_email(email),
            username = username,
            is_traveler = is_traveler
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    username_validator = UnicodeUsernameValidator()
    first_name = models.CharField(max_length=20, verbose_name="Name*", null=True)
    last_name = models.CharField(max_length=50,verbose_name="Surname*", null=True)
    username = models.CharField(
        ('username'),
        max_length=150,
        unique=True,
        help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
    email = models.EmailField(max_length=60, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_traveler = models.IntegerField(choices=((1, True), (0, False)))

    last_login = models.DateTimeField(verbose_name='Last Login', auto_now=True)
    date_joined = models.DateTimeField(verbose_name='Joined', auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', "is_traveler"]

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm , obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True







